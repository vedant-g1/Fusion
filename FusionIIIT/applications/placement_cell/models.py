# imports
import datetime

from django.db import models
from django.utils.translation import gettext as _

from applications.academic_information.models import Student

# Class definations:


class Constants:
    RESUME_TYPE = (
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
    )
    ACHIEVEMENT_TYPE = (
        ('EDUCATIONAL', 'Educational'),
        ('OTHER', 'Other'),
    )
    INVITATION_TYPE = (
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('PENDING', 'Pending'),
    )
    PLACEMENT_TYPE = (
        ('PLACEMENT', 'Placement'),
        ('PBI', 'PBI'),
        ('HIGHER STUDIES', 'Higher Studies'),
        ('OTHER', 'Other'),
    )
    PLACED_TYPE = (
        ('ON CAMPUS', 'On Campus'),
        ('PPO', 'PPO'),
        ('OFF CAMPUS', 'Off Campus'),
    )
    DEBAR_TYPE = (
        ('DEBAR', 'Debar'),
        ('NOT DEBAR', 'Not Debar'),
    )


class Project(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=40, default='')
    project_status = models.CharField(max_length=20, choices=Constants.RESUME_TYPE,
                                      default='COMPLETED')
    summary = models.CharField(max_length=500, default='', null=True, blank=True)
    project_link = models.CharField(max_length=200, default='', null=True, blank=True)
    sdate = models.DateField(_("Date"), default=datetime.date.today)
    edate = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.project_name)


class Language(models.Model):
    language = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.language


class Know(models.Model):
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('language_id', 'unique_id'),)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.language_id.language)


class Skill(models.Model):
    skill = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.skill


class Has(models.Model):
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    skill_rating = models.IntegerField(default=80)

    class Meta:
        unique_together = (('skill_id', 'unique_id'),)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.skill_id.skill)


class Education(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    degree = models.CharField(max_length=40, default='')
    grade = models.CharField(max_length=10, default='')
    institute = models.CharField(max_length=250, default='')
    stream = models.CharField(max_length=150, default='', null=True, blank=True)
    sdate = models.DateField(_("Date"), default=datetime.date.today)
    edate = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.degree)


class Experience(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=20, choices=Constants.RESUME_TYPE,
                              default='COMPLETED')
    description = models.CharField(max_length=500, default='', null=True, blank=True)
    company = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    sdate = models.DateField(_("Date"), default=datetime.date.today)
    edate = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.company)


class Course(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=250, default='', null=True, blank=True)
    license_no = models.CharField(max_length=100, default='', null=True, blank=True)
    sdate = models.DateField(_("Date"), default=datetime.date.today)
    edate = models.DateField(null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.course_name)


class Publication(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    publication_title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=250, default='', null=True, blank=True)
    publisher = models.CharField(max_length=250, default='')
    publication_date = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.publication_title)


class Coauthor(models.Model):
    publication_id = models.ForeignKey(Publication, on_delete=models.CASCADE)
    coauthor_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{} - {}'.format(self.publication_id.publication_title, self.coauthor_name)


class Patent(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    patent_name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=250, default='', null=True, blank=True)
    patent_office = models.CharField(max_length=250, default='')
    patent_date = models.DateField()

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.patent_name)


class Coinventor(models.Model):
    patent_id = models.ForeignKey(Patent, on_delete=models.CASCADE)
    coinventor_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{} - {}'.format(self.patent_id.patent_name, self.coinventor_name)


class Interest(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    interest = models.CharField(max_length=100, default='')

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.interest)


class Achievement(models.Model):
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    achievement = models.CharField(max_length=100, default='')
    achievement_type = models.CharField(max_length=20, choices=Constants.ACHIEVEMENT_TYPE,
                                        default='OTHER')
    description = models.CharField(max_length=250, default='', null=True, blank=True)
    issuer = models.CharField(max_length=200, default='')
    date_earned = models.DateField(_("Date"), default=datetime.date.today)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.achievement)


class MessageOfficer(models.Model):
    message = models.CharField(max_length=100, default='')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class NotifyStudent(models.Model):
    placement_type = models.CharField(max_length=20, choices=Constants.PLACEMENT_TYPE,
                                      default='PLACEMENT')
    company_name = models.CharField(max_length=100, default='')
    ctc = models.DecimalField(default='', decimal_places=2, max_digits=5)
    description = models.CharField(max_length=1000, default='', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.company_name, self.timestamp)


class PlacementStatus(models.Model):
    notify_id = models.ForeignKey(NotifyStudent, on_delete=models.CASCADE)
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    invitation = models.CharField(max_length=20, choices=Constants.INVITATION_TYPE,
                                  default='PENDING')
    placed = models.CharField(max_length=20, choices=Constants.INVITATION_TYPE,
                              default='PENDING')
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('notify_id', 'unique_id'),)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.notify_id.company_name)


class PlacementRecord(models.Model):
    placement_type = models.CharField(max_length=20, choices=Constants.PLACEMENT_TYPE,
                                      default='PLACEMENT')
    name = models.CharField(max_length=100, default='')
    ctc = models.DecimalField(default='', decimal_places=2, max_digits=5, null=True, blank=True)
    year = models.IntegerField(default='')
    test_score = models.IntegerField(default='', null=True, blank=True)
    test_type = models.CharField(max_length=30, default='', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.year)


class StudentRecord(models.Model):
    record_id = models.ForeignKey(PlacementRecord, on_delete=models.CASCADE)
    unique_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('record_id', 'unique_id'),)

    def __str__(self):
        return '{} - {}'.format(self.unique_id.id, self.record_id.name)


class ChairmanVisit(models.Model):
    company_name = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=100, default='')
    visiting_date = models.DateField(_("Date"), default=datetime.date.today)
    description = models.CharField(max_length=1000, default='', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class ContactCompany(models.Model):
    company_name = models.CharField(max_length=100, default='')
    hr_mail = models.CharField(max_length=100, default='', null=True, blank=True)
    reference = models.CharField(max_length=1000, default='', null=True, blank=True)
    description = models.CharField(max_length=500, default='', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.company_name, self.timestamp)


class PlacementSchedule(models.Model):
    notify_id = models.ForeignKey(NotifyStudent, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    placement_date = models.DateField(_("Date"), default=datetime.date.today)
    location = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500, default='', null=True, blank=True)
    time = models.TimeField()

    def __str__(self):
        return '{} - {}'.format(self.notify_id.company_name, self.placement_date)


class StudentPlacement(models.Model):
    unique_id = models.OneToOneField(Student, primary_key=True, on_delete=models.CASCADE)
    debar = models.CharField(max_length=20, choices=Constants.DEBAR_TYPE, default='NOT DEBAR')
    future_aspect = models.CharField(max_length=20, choices=Constants.PLACEMENT_TYPE,
                                     default='PLACEMENT')
    placed_type = models.CharField(max_length=20, choices=Constants.PLACED_TYPE,
                                   default='', null=True, blank=True)
    placement_date = models.DateField(_("Date"), default=datetime.date.today, null=True,
                                      blank=True)
    package = models.DecimalField(default='', decimal_places=2, max_digits=5, null=True,
                                  blank=True)

    def __str__(self):
        return self.unique_id.id
