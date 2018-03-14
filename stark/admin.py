# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from models import Project, Worker, DatabaseForm

class ProjectAdmin(admin.ModelAdmin):
    list_display=('name','project_manager','number','company','cost')
    search_fields = ['name']

class WorkerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','position','phone','email')
    search_fields = ['name']

class DatabaseFormAdmin(admin.ModelAdmin):
    list_display=('db_name','db_ip','db_port','kullanici_adi','parola')
    search_fields = ['db_name']



admin.site.register(Project,ProjectAdmin)
admin.site.register(Worker,WorkerAdmin)
admin.site.register(DatabaseForm,DatabaseFormAdmin)
