# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", )

    search_fields = ["name"]

@admin.register(models.Working_Hour)
class WorkingHourAdmin(admin.ModelAdmin):
    list_display = ("dayOfWeek", )
    search_fields = ["dayOfWeek"]