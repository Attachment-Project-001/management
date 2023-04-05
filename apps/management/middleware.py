from .models import AcademicSession, AcademicTerm


class SiteWideConfigs:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_session = AcademicSession.objects.filter(current=True)[:1].get()
        current_term = AcademicTerm.objects.filter(current=True)[:1].get()

        request.current_session = current_session
        request.current_term = current_term

        response = self.get_response(request)

        return response
