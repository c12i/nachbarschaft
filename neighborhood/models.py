from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify
from django.db.models import Q
# from accounts.models import User

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()



class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=144)
    slug = models.SlugField(allow_unicode=True, unique=True)
    police_contact = models.PositiveIntegerField()
    hospital_contact = models.PositiveIntegerField()
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("neighborhood:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships")
    user = models.ForeignKey(User,related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")


class Business(models.Model):
    group = models.ForeignKey(Group, related_name="businesses")
    name = models.CharField(max_length=144)
    description = models.TextField()
    category = models.CharField(max_length=144)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.filter(id = business_id)

    def get_absolute_url(self):
        return reverse("neighborhood:single", kwargs={"slug": self.group.slug})