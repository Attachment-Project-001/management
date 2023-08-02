# Use the official Python 3.10 slim image as the base image for the build stage
FROM python:3.10-slim as python-build-stage
ARG APP_HOME=/app
WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

# Copy only the requirements.txt to utilize Docker cache efficiently
COPY ./requirements.txt ./

# Install system dependencies and Python packages
RUN apt-get update && apt-get install --no-install-recommends -y \
        # dependencies for building Python packages
        build-essential wget \
        # psycopg2 dependencies
        libpq-dev postgis gdal-bin libgdal-dev \
    && pip wheel --wheel-dir /usr/src/app/wheels -r requirements.txt

# Use the official Python 3.10 slim image as the base image for the runtime stage
FROM python:3.10-slim as python-run-stage
ARG APP_HOME=/app
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install -y \
        # psycopg2 dependencies
        libpq-dev \
        # Translations dependencies
        gettext \
        # wget
        wget xvfb \
        # npm and nodejs
        curl postgis gdal-bin libgdal-dev gnupg2 wget \
        # build dependencies
        python3 automake autoconf libtool nasm \
    && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python wheels from the build stage
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# Install Python dependencies using wheels
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

# Copy project
COPY --from=python-build-stage ${APP_HOME} ${APP_HOME}

# Copy entrypoint and setup scripts
COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# Set the entrypoint for the container
ENTRYPOINT ["/entrypoint"]
