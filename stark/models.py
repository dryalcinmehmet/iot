# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model



class CassandraConstruction(Model):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    values1 = columns.Integer()
    values2 = columns.Float()
    values3 = columns.Float()
    values4 = columns.Float()
    values5 = columns.Float()
    values6 = columns.Float()

    def __unicode__(self):
        return self.example_id


class iot6(Model):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    voltaj = columns.Float()
    akim = columns.Float()
    aktif= columns.Float()
    reaktif = columns.Float()
    faz_acisi = columns.Float()
    sicaklik= columns.Float()



    def __unicode__(self):
        return self.example_id

class fipy2(Model):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    voltaj = columns.Text()

    def __unicode__(self):
        return self.example_id


class Project(models.Model):
    name = models.CharField(max_length=30)
    project_manager = models.CharField(max_length=30)
    number = models.CharField(max_length=50)
    company = models.CharField(max_length=60)
    investor = models.CharField(max_length=30)
    cost = models.CharField(max_length=50)
    cdate = models.DateTimeField(default=timezone.now)
    pdate = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name

class Worker(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __unicode__(self):
        return self.first_name


class DatabaseForm(models.Model):
    db_name       = models.CharField(max_length=30)
    db_ip         = models.CharField(max_length=40)
    db_port       = models.CharField(max_length=4)
    kullanici_adi = models.CharField(max_length=10)
    parola        = models.CharField(max_length=10)

    def __unicode__(self):
        return self.db_name