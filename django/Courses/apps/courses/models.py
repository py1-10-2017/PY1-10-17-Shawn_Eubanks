from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['course_name']) <= 5:
            errors["course_name"] = "Course name must be more than 5 characters"
        return errors

class DescriptionManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['description']) <= 15:
            errors["description"] = "Course description must be more than 15 characters"
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()

class Description(models.Model):
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    course = models.OneToOneField(Course, related_name="description")

    objects = DescriptionManager()