from django.test import TestCase
from faker import Faker

from apps.management.models import (
    AcademicSession,
    AcademicTerm,
    DailyAttendance,
    Department,
    SiteConfig,
    Stud_Class,
    Subject,
    SubjectAssignToStudent,
    SubjectAssignToTeacher,
)
from apps.staff.models import Designation, Staff
from apps.students.models import Student

fakegen = Faker()


class SiteConfigTest(TestCase):
    def test_siteconfig(self):
        site_config = SiteConfig.objects.create(key="akey", value="aname")
        self.assertEqual(str(site_config), "akey")
        self.assertEqual(site_config.value, "aname")
        self.assertEqual(site_config.key, "akey")


class AcademicSessionTest(TestCase):
    def test_academicsession(self):
        session = AcademicSession.objects.create(name="test session", current=True)
        self.assertEqual(str(session), "test session")
        self.assertEqual(session.current, True)
        self.assertEqual(session.name, "test session")


class AcademicTermTest(TestCase):
    def test_academicterm(self):
        term = AcademicTerm.objects.create(name="test Term", current=True)
        self.assertEqual(str(term), "test Term")
        self.assertEqual(term.current, True)
        self.assertEqual(term.name, "test Term")


class SubjectTest(TestCase):
    def test_subject(self):
        subject = Subject.objects.create(name="a_subject")
        self.assertEqual(str(subject), "a_subject")
        self.assertEqual(subject.name, "a_subject")


class ClassTest(TestCase):
    def test_class(self):
        stud_class = Stud_Class.objects.create(name="test stud_class")
        self.assertEqual(str(stud_class), "test stud_class")
        self.assertEqual(stud_class.name, "test stud_class")


class DepartmentTest(TestCase):
    def test_department(self):
        designation = Designation.objects.create(title="test designation")
        staff = Staff.objects.create(
            first_name=fakegen.first_name(),
            surname=fakegen.last_name_nonbinary(),
            last_name=fakegen.last_name(),
            mobile_number="+254740576086",
            email=fakegen.email(),
            address=fakegen.address(),
            designation=designation,
        )
        department = Department.objects.create(
            name="test department", code="test code", head=staff
        )
        self.assertEqual(str(department), "test department")
        self.assertEqual(department.name, "test department")
        self.assertEqual(department.code, "test code")
        self.assertEqual(department.head, staff)


class DailyAttendanceTest(TestCase):
    def test_dailyattendance(self):
        designation = Designation.objects.create(title="test designation")
        student = Student.objects.create(
            first_name=fakegen.first_name(),
            surname=fakegen.last_name_nonbinary(),
            last_name=fakegen.last_name(),
            registration_number=fakegen.random_int(min=10000, max=99999, step=1),
            student_mobile="+254740576086",
            parent_mobile="+254740576086",
        )
        staff = Staff.objects.create(
            first_name=fakegen.first_name(),
            surname=fakegen.last_name_nonbinary(),
            last_name=fakegen.last_name(),
            mobile_number="+254740576086",
            email=fakegen.email(),
            designation=designation,
            address=fakegen.address(),
        )

        dailyattendance = DailyAttendance.objects.create(
            date="2020-01-01",
            student=student,
            teacher=staff,
        )
        self.assertEqual(dailyattendance.student, student)
        self.assertEqual(dailyattendance.teacher, staff)
        self.assertEqual(dailyattendance.is_present, False)


class StaffTest(TestCase):
    def test_staff(self):
        designation = Designation.objects.create(title="test designation")
        staff = Staff.objects.create(
            first_name=fakegen.first_name(),
            surname=fakegen.last_name_nonbinary(),
            last_name=fakegen.last_name(),
            mobile_number="+254740576086",
            email=fakegen.email(),
            designation=designation,
            address=fakegen.address(),
        )
        self.assertEqual(staff.current_status, "permanent")
        self.assertEqual(staff.gender, "male")
        # self.assertEqual(staff.designation, designation)

    def test_designation(self):
        designation = Designation.objects.create(title="test designation")
        self.assertEqual(str(designation), "test designation")
        self.assertEqual(designation.title, "test designation")


class SubjectAssignToStudentTest(TestCase):
    def test_subjectassigntostudent(self):
        student = Student.objects.create(
            first_name=fakegen.first_name(),
            surname=fakegen.last_name_nonbinary(),
            last_name=fakegen.last_name(),
            registration_number=fakegen.random_int(min=10000, max=99999, step=1),
            student_mobile="+254740576086",
            parent_mobile="+254740576086",
        )
        subject = Subject.objects.create(name="test subject")
        subjectassigntostudent = SubjectAssignToStudent.objects.create(subject=subject)
        subjectassigntostudent.student.add(student)
        self.assertEqual(subjectassigntostudent.subject, subject)
        self.assertEqual(str(subjectassigntostudent), subject.name)
        assert student in subjectassigntostudent.student.all()


class SubjectAssignToTeacherTest(TestCase):
    def test_subjectassigntoteacher(self):
        designation = Designation.objects.create(title="test designation")
        staff = Staff.objects.create(
            first_name=fakegen.first_name(),
            surname=fakegen.last_name_nonbinary(),
            last_name=fakegen.last_name(),
            mobile_number="+254740576086",
            designation=designation,
            email=fakegen.email(),
            address=fakegen.address(),
        )
        subject = Subject.objects.create(name="test subject")
        subjectassigntoteacher = SubjectAssignToTeacher.objects.create(subject=subject)
        subjectassigntoteacher.teacher.add(staff)
        assert staff in subjectassigntoteacher.teacher.all()
        self.assertEqual(subjectassigntoteacher.subject, subject)
        self.assertEqual(str(subjectassigntoteacher), subject.name)
