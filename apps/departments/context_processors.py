from .models import AcademicSession, AcademicTerm, SiteConfig

def site_defaults(request):
    current_session = AcademicSession.objects.get(current=True)
    current_term = AcademicTerm.objects.get(current=True)
    vals = SiteConfig.objects.all()
    context = {
        'current_session': current_session.name,
        'current_term': current_term.name
    }
    for val in vals:
        context[val.key] = val.values()

    return context
