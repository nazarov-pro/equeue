from django.contrib import admin
from . import models


@admin.register(models.WorkingHour)
class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ("company", "start", "end",)
    search_fields = ["company"]


@admin.register(models.WeekDay)
class WorkingDayAdmin(admin.ModelAdmin):
    list_display = ("dayOfWeek",)
    search_fields = ["dayOfWeek"]


@admin.register(models.ExeptionDay)
class ExceptionAdmin(admin.ModelAdmin):
    list_display = ("date", "status", "start", "end",)
    search_fields = ["date"]


@admin.register(models.Country)
class ExceptionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ["name"]


@admin.register(models.Holiday)
class ExceptionAdmin(admin.ModelAdmin):
    list_display = ("country", "date",)
    search_fields = ["date"]
