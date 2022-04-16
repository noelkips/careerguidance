import datetime
from email.mime import image
from unicodedata import name

from django.db import models
import os
from django.conf import settings

from django.urls import reverse


class University(models.Model):
    name = models.CharField(max_length=200)
    Univ_no = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="static/images/universities", null=True, blank=True)
    university_types = (
        ('public', 'public'),
        ('private', 'private'),
    )
    category = models.CharField(choices=university_types, default='public', max_length=30)
    location = models.CharField(max_length=200)
    about = models.URLField(max_length=2083)

    def __str__(self):
        return self.name[:50]

    def get_absolute_url(self):
        return reverse('course:university_detail', args=[str(self.pk)])


class Category(models.Model):
    name = models.CharField(max_length=30)
    category_no = models.AutoField(primary_key=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name[:50]


class Course(models.Model):
    name = models.CharField(max_length=30)
    course_no = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/images/courses/", null=True, blank=True)
    first_sub = models.CharField(max_length=300)
    second_sub = models.CharField(max_length=300)
    third_sub = models.CharField(max_length=300)
    fourth_sub = models.CharField(max_length=300)
    career = models.CharField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=50,
                            help_text='value that help users find course')

    def __str__(self):
        return self.name[:50]

    def get_absolute_url(self):
        return reverse('course:course_detail', args=[str(self.course_no)])


class Entry(models.Model):
    entry_no = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cut_off = models.FloatField(null=False, default=0.0, )
    cut_off_max = models.FloatField(null=False, default=12.0, )
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('course:entry_detail', args=[str(self.pk)])
