#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from qr.devices.models import Devices, Sorts


class DevicesAdmin(admin.ModelAdmin):
    fields = ('sort', 'name', 'location', 'others', 'model', 'img')
    list_filter = ("sort","location")
    list_display = ('name', 'sort', 'location', 'model', 'create_date',)
    search_fields = ('name', 'location')

class SortsAdmin(admin.ModelAdmin):
    list_display = ("name", "information")

admin.site.register(Devices, DevicesAdmin)
admin.site.register(Sorts, SortsAdmin)
