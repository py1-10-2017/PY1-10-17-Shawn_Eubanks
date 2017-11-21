from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name can't be fewer than 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name can't be fewer than 2 characters"
        if len(postData['email_address']) < 1:
            errors["email_address"] = "Email must be specified"
        else:
            if not re.match(EMAIL_REGEX,postData['email_address']):
                errors["email_address"] = "Email address invalid"
            else:
                if len(self.filter(email_address=postData['email_address'])) >= 1:
                    errors["email_address"] = "Email already in use"
        if len(postData['password']) < 6:
            errors["password"] = "Password can't be fewer than 6 characters"
        else:
            if postData['password'] != postData['password_confirm']:
                errors["password"] = "Password confirmation does not match password"

        if len(errors) == 0:
            first_name = postData['first_name']
            last_name = postData['last_name']
            email_address = postData['email_address']

            password_raw = postData['password']
            password_hash = bcrypt.hashpw(password_raw.encode(), bcrypt.gensalt())

            User.objects.create(first_name=first_name, last_name=last_name, email_address=email_address, password=password_hash)

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()