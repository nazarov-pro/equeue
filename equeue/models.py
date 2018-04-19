from django.utils.translation import gettext as _
from django.db import models
from company.models import Company


class WeekDay(models.Model):
    WEEK_CHOICES = (
        ("1", _(u"Monday")),
        ("2", _(u"Tuesday")),
        ("3", _(u"Wednesday")),
        ("4", _(u"Thursday")),
        ("5", _(u"Friday")),
        ("6", _(u"Saturday")),
        ("7", _(u"Sunday")),
    )
    dayOfWeek = models.CharField(_(u"Day Of Week"),
                                 max_length=1,
                                 choices=WEEK_CHOICES, unique=True)

    def __str__(self):
        return dict(self.WEEK_CHOICES).get(self.dayOfWeek)

    class Meta:
        verbose_name = _(u"Week Day")


class WorkingHour(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    weekdays = models.ManyToManyField(WeekDay)
    start = models.TimeField(_(u"Start Time"), default="00:00:00")
    end = models.TimeField(_(u"End Time"), default="23:59:59")

    def __str__(self):
        return self.company.name

    class Meta:
        verbose_name = _(u"Working Hour")


class ExeptionDay(models.Model):

    STATUS_CHOICES = (
        ("W", _(u"Business Day")),
        ("O", _(u"Day Off")),
    )

    company = models.ManyToManyField(Company)
    date = models.DateField(_(u"Date"))
    start = models.TimeField(_(u"Start Time"), default="00:00:00")
    end = models.TimeField(_(u"End Time"), default="23:59:59")
    status = models.CharField(_(u"Status"), max_length=1,
                              choices=STATUS_CHOICES,
                              default="O")

    def __str__(self):
        template = '{0.date} {0.start} {0.end}'
        return template.format(self)

    class Meta:
        verbose_name = _(u"Exception Day")


class Country(models.Model):
    name = models.CharField(_(u"Country"), max_length=25)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    class Meta:
        verbose_name = _(u"Country")


class Holiday(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateField(_(u"Date"))

    def __str__(self):
        template = '{0.country} {0.date}'
        return template.format(self)

    class Meta:
        verbose_name = _(u"Holiday")


