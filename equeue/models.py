from django.utils.translation import gettext as _
from django.db import models
from django.utils import timezone

class Company(models.Model):
    STATUS_CHOICES = (
        ("ACTIVATED", _("Activated")),
        ("TERMINATED", _("Terminated")),
        ("SUSPENDED", _("Suspended")),
        ("CLOSED", _("Closed")),
    )
    name = models.CharField(_(u"Name"), max_length=200)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=15, default="TERMINATED")
    email = models.EmailField
    telephone = models.CharField(max_length=25)
    isWorkOnHolidays = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class WeekDay(models.Model):
    WEEK_CHOICES = (
        ("1", _("Monday")),
        ("2", _("Tuesday")),
        ("3", _("Wednesday")),
        ("4", _("Thursday")),
        ("5", _("Friday")),
        ("6", _("Saturday")),
        ("7", _("Sunday")),
    )
    dayOfWeek = models.CharField(max_length=1, choices=WEEK_CHOICES, unique=True)

    def __str__(self):
        return dict(self.WEEK_CHOICES).get(self.dayOfWeek)

class WorkingHour(models.Model):
    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)
    weekdays = models.ManyToManyField(WeekDay)
    start = models.TimeField(_(u"Start_Time"), default="00:00:00")
    end = models.TimeField(_(u"End_Time"), default="23:59:59")
    def __str__(self):
        return self.company.name

class ExeptionDay(models.Model):
    company = models.ManyToManyField(Company)
    date = models.DateField(_("Date"))
    start = models.TimeField(_("Start_Time"), default="00:00:00")
    end = models.TimeField(_("End_Time"), default="23:59:59")

    def __str__(self):
        template = '{0.date} {0.start} {0.end}'
        return template.format(self)