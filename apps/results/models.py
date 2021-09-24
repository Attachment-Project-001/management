from django.conf import settings
from django.db import models

from apps.students.models import Student
from apps.management.models import AcademicSession, AcademicTerm, Stud_Class, Subject


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    term = models.ForeignKey(AcademicTerm, on_delete=models.CASCADE)
    current_class = models.ForeignKey(Stud_Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_score = models.IntegerField(default=0)
    exam_score = models.IntegerField(default=0)
    created_by = models.ForeignKey( settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        ordering = ["subject"]
        unique_together = ['subject', 'student']

    def __str__(self):
        return f"{self.student} {self.session} {self.term} {self.subject} {self.grade}"

    def total_score(self):
        return self.test_score + self.exam_score

    def grade(self):
        if 80 <= self.total_score() <= 100:
            return 'A'
        elif 60 <= self.total_score() < 80:
            return 'B'
        elif 50 <= self.total_score() < 60:
            return 'C'
        elif 40 <= self.total_score() < 50:
            return 'D'
        else:
            return 'F'
            