from django.db import models
import uuid
from datetime import datetime
from xml.dom.xmlbuilder import DOMBuilder

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.

class Admins(models.Model):
    '''
        first you need to add first admin with this query :

        INSERT INTO "Reminder_admins" (admin_id,admin_name,admin_lastname,admin_phone,admin_password,admin_permissions,
        other_information,admin_create_date) VALUES ('4e00a512-6835-4150-bd0e-b102b200578b','admin','admin',
        '09351111111','1234',ARRAY['Self','Admin','User','Reminder'],'{}','2022-03-26T18:14:29Z');

    '''
    admin_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_name = models.CharField(max_length=200)
    admin_lastname = models.CharField(max_length=200)
    admin_phone = models.CharField(max_length=20, unique=True)
    admin_password = models.CharField(max_length=200)
    admin_permissions = ArrayField(models.CharField(max_length=100))
    other_information = models.JSONField()
    admin_create_date = models.DateTimeField(
        default=datetime.now, blank=True)

    def as_dict(self):
        return {
            "admin_id": self.admin_id,
            "admin_name": self.admin_name,
            "admin_lastname": self.admin_lastname,
            "admin_phone": self.admin_phone,
            "admin_password": self.admin_password,
            "admin_permissions": self.admin_permissions,
            "other_information": self.other_information,
            "admin_create_date": self.admin_create_date
        }


class Users(models.Model):
    user_admin = models.ForeignKey(Admins, on_delete=models.CASCADE)
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=200, null=True)
    user_lastname = models.CharField(max_length=200, null=True)
    user_phone = models.CharField(max_length=20, unique=True)
    user_password = models.CharField(max_length=200, null=True)
    other_information = models.JSONField(null=True)
    user_create_date = models.DateTimeField(
        default=datetime.now, blank=True)

    def as_dict(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "user_lastname": self.user_lastname,
            "user_phone": self.user_phone,
            "user_password": self.user_password,
            "other_information": self.other_information,
            "user_create_date": self.user_create_date,
        }


class Reminder(models.Model):
    reminder_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reminder_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    reminder_title = models.TextField()
    reminder_message = models.CharField(max_length=200)
    reminder_creat_time = models.DateTimeField(
        default=datetime.now, blank=True)
    reminder_showtime = models.DateTimeField()
    reminder_alarm_time = models.DateTimeField(null=True, blank=True)

    def as_dict(self):
        reminder_user_info = {
            "user_id": self.reminder_user.as_dict()['user_id'],
            "user_name": self.reminder_user.as_dict()['user_name'],
            "user_phone": self.reminder_user.as_dict()['user_phone'],
        }
        return {
            "reminder_user_info": reminder_user_info,
            "reminder_id": self.reminder_id,
            "reminder_title": self.reminder_title,
            "reminder_message": self.reminder_message,
            "reminder_creat_time": self.reminder_creat_time,
            "reminder_showtime": self.reminder_showtime,
            "reminder_alarm_time": self.reminder_alarm_time,
        }
