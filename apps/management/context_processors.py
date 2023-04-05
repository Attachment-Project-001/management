from .models import AcademicSession, AcademicTerm, SiteConfig

'''default contexts'''
def site_defaults(request):
    current_session = AcademicSession.objects.filter(current=True)[:1].get()
    current_term = AcademicTerm.objects.filter(current=True)[:1].get()
    vals = SiteConfig.objects.all()
    context = {
        'current_session': current_session.name,
        'current_term': current_term.name
    }
    for val in vals:
        context[val.key] = val.value

    return context
