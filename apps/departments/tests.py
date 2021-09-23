from django.test import TestCase

from .models import (
    AcademicSession,
    AcademicTerm,
    SiteConfig,
    Subject,
    Stud_Class,
)


class SiteConfigTest(TestCase):
    def test_siteconfig(self):
        site_config = SiteConfig.objects.create(key="akey", value="aname")
        self.assertEqual(str(site_config), "akey")


class AcademicSessionTest(TestCase):
    def test_academicsession(self):
        session = AcademicSession.objects.create(name="test session", current=True)
        self.assertEqual(str(session), "test session")


class AcademicTermTest(TestCase):
    def test_academicterm(self):
        term = AcademicTerm.objects.create(name="test Term", current=True)
        self.assertEqual(str(term), "test Term")


class SubjectTest(TestCase):
    def test_subject(self):
        subject = Subject.objects.create(name="a_subject")
        self.assertEqual(str(subject), "a_subject")

class ClassTest(TestCase):
    def test_class(self):
        stud_class = Stud_Class.objects.create(name="test stud_class")
        self.assertEqual(str(stud_class), "test stud_class")
