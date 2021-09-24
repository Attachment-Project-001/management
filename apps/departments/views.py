from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import ListView, TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import (CurrentSessionForm, SiteConfigForm, AcademicSessionForm,
                    AcademicTermForm, Stud_ClassForm, SubjectForm)
from .models import (AcademicSession, AcademicTerm, SiteConfig,
                     Stud_Class, Subject)


class SessionListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicSession
    template_name = 'departments/session_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AcademicSessionForm()
        return context


class SiteConfigView(LoginRequiredMixin, View):
    '''Site Config View'''
    form_class = SiteConfigForm
    template_name = "departments/siteconfig.html"

    def get(self, request, *args, **kwargs):
        formset = self.form_class(queryset=SiteConfig.objects.all())
        context = {"formset": formset}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        formset = self.form_class(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, "Configurations successfully updated")
        context = {"formset": formset, "title": "Configuration"}
        return render(request, self.template_name, context)

class SessionListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicSession
    template_name = "departments/session_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AcademicSessionForm()
        return context


class SessionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AcademicSession
    form_class = AcademicSessionForm
    template_name = 'departments/core_form.html'
    success_url = reverse_lazy('sessions')
    success_message = "New session successfully added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add new session"
        return context


class SessionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AcademicSession
    form_class = AcademicSessionForm
    template_name = 'departments/core_form.html'
    success_url = reverse_lazy('sessions')
    success_message = "Session successfully updated"

    def form_valid(self, form):
        obj = self.object
        if obj.current == False:
            sessions = (
                AcademicSession.objects.filter(current=True)
                .exclude(name=obj.name).exists()
            )
            if not sessions:
                messages.warning(
                    self.request, "You must set a session to current.")
                return redirect("session-list")
        return super().form_valid(form)


class SessionDeleteView(LoginRequiredMixin, DeleteView):
    model = AcademicSession
    template_name = "departments/core_confirm_delete.html"
    success_url = reverse_lazy('sessions')
    success_message = "The session {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(
                request, "Cannot delete session as it is set to current")
            return redirect('sessions')
        messages.success(self.request, self.success_message.format(obj.name))
        return super(SessionDeleteView, self).delete(request, *args, **kwargs)


class TermCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = AcademicTerm
    form_class = AcademicSessionForm
    template_name = 'departments/core_form.html'
    success_url = reverse_lazy('terms')
    success_message = "New term successsfully added"


class TermListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = AcademicTerm
    template_name = 'departments/term_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AcademicTermForm()
        return context


class TermUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AcademicTerm
    form_class = AcademicTermForm
    success_url = reverse_lazy('terms')
    success_message = "Term successfully updated."
    template_name = 'departments/core_form.html'

    def form_valid(self, form):
        obj = self.get_object
        if obj.current == False:
            terms = (
                AcademicTerm.objects.filter(current=True)
                .exclude(name=obj.name).exists()
            )
            if not terms:
                messages.warning(
                    self.request, "You must set a term to current")
                return redirect('term')
        return super().form_valid(form)


class TermDeleteView(LoginRequiredMixin, DeleteView):
    model = AcademicTerm
    success_url = reverse_lazy('terms')
    template_name = 'departments/core_form_delete.html'
    success_message = 'The term {} has been deleted with all attached content'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.current == True:
            messages.warning(request, "Cannot delete term set to current.")
            return redirect('terms')
        messages.success(self.request, self.success_message.format(obj.name))
        return super(TermDeleteView, self).delete(request, *args, **kwargs)


class ClassCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Stud_Class
    form_class = Stud_ClassForm
    template_name = 'departments/core_form.html'
    success_url = reverse_lazy('classes')
    success_message = "New class successfully added"


class ClassListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Stud_Class
    template_name = 'departments/class_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Stud_ClassForm()
        return context


class ClassUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Stud_Class
    fields = ['name']
    success_url = reverse_lazy('classes')
    success_message = "Class successfully updated."
    template_name = 'departments/core_form.html'


class ClassDeleteView(LoginRequiredMixin, DeleteView):
    model = Stud_Class
    success_url = reverse_lazy('classes')
    template_name = 'departments/core_confirm_delete.html'
    success_message = 'The class {} has been deleted with all its content'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        print(obj.name)
        messages.success(self.request, self.success_message.format(obj.name))
        return super(ClassDeleteView, self).delete(request, *args, **kwargs)


class SubjectCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "departments/core_form.html"
    success_url = reverse_lazy("subjects")
    success_message = "New subject successfully added"


class SubjectListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Subject
    template_name = "departments/subject_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SubjectForm()
        return context


class SubjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Subject
    fields = ["name"]
    success_url = reverse_lazy("subjects")
    success_message = "Subject successfully updated."
    template_name = "departments/core_form.html"


class SubjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy("subjects")
    template_name = "departments/core_confirm_delete.html"
    success_message = "The subject {} has been deleted with all its attached content"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message.format(obj.name))
        return super(SubjectDeleteView, self).delete(request, *args, **kwargs)


class CurrentSessionAndTermView(LoginRequiredMixin, View):
    form_class = CurrentSessionForm
    template_name = 'departments/current_session.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(
            initial={
                "current_session": AcademicSession.objects.get(current=True),
                "current_term": AcademicTerm.objects.get(current=True),
            }
        )
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            session = form.cleaned_data['current_session']
            term = form.cleaned_data['current_term']
            AcademicSession.objects.filter(name=session).update(current=True)
            AcademicSession.objects.exclude(name=session).update(current=False)
            AcademicTerm.objects.filter(name=term).update(current=True)
        return render(request, self.template_name, {"form": form})
