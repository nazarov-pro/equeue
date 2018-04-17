# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", )

    search_fields = ["name"]

@admin.register(models.WorkingHour)
class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ("company", )
    search_fields = ["company"]

@admin.register(models.WeekDay)
class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ("dayOfWeek",)
    search_fields = ["dayOfWeek"]

@admin.register(models.ExeptionDay)
class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ("date",)
    search_fields = ["date"]