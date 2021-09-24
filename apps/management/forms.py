from django import forms
from django.db.models import fields
from django.forms import ModelForm, modelformset_factory

from .models import (AcademicSession, AcademicTerm, Department, SiteConfig, Subject, Stud_Class,
                     SubjectAssignToStudent, SubjectAssignToTeacher)

SiteConfigForm = modelformset_factory(
    SiteConfig,
    fields=("key", "value"),
    extra=0,
)


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class AcademicSessionForm(ModelForm):
    prefix = 'Academic Session'

    class Meta:
        model = AcademicSession
        fields = ["name", "current"]


class AcademicTermForm(ModelForm):
    prefix = 'Academic Term'

    class Meta:
        model = AcademicTerm
        fields = ["name", "current"]


class SubjectForm(ModelForm):
    prefix = 'Subject'

    class Meta:
        model = Subject
        fields = ['name']


class SubjectAssignToTeacherForm(ModelForm):
    class Meta:
        model = SubjectAssignToTeacher
        fields = '__all__'


class SubjectAssignToStudentForm(ModelForm):
    class Meta:
        model = SubjectAssignToStudent
        fields = '__all__'


class Stud_ClassForm(ModelForm):
    prefix = 'Class'

    class Meta:
        model = Stud_Class
        fields = ["name"]


class CurrentSessionForm(forms.Form):
    current_session = forms.ModelChoiceField(
        queryset=AcademicSession.objects.all(),
        help_text='Click <a href="/session/create/?next=current-session/">here</a> to add new session',
    )
    current_term = forms.ModelChoiceField(
        queryset=AcademicTerm.objects.all(),
        help_text='Click <a href="/term/create/?next=current-session/">here</a> to add new term',
    )

