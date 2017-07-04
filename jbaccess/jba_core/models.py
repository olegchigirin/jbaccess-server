from django.db import models


class AclType:
    ACL_ALLOW = 1
    ACL_DENY = 2

    acl_choices = {
        (ACL_ALLOW, 1),
        (ACL_DENY, 2)
    }


class Door(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    access_id = models.CharField(max_length=255, unique=True)


class Controller(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    controller_id = models.CharField(max_length=255, null=False, unique=True)
    doors = models.ManyToManyField(Door)


class Place(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    doors = models.ManyToManyField(Door)


class Role(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)


class Person(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    roles = models.ManyToManyField(Role)


class Key(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    access_key = models.CharField(max_length=255, null=False)
    person = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)


class BaseACLEntry(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    type = models.IntegerField(null=False)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=False)


class PersonACLEntry(BaseACLEntry):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)


class RoleACLEntry(BaseACLEntry):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)


class RecurringPattern(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    acl = models.ForeignKey(BaseACLEntry, on_delete=models.CASCADE, null=False, default=None)

    class Meta:
        abstract = True


class SimpleRecurringPattern(RecurringPattern):
    from_time = models.DurationField(null=False)
    until_time = models.DurationField(null=False)
    days_of_week = models.CharField(null=False, max_length=255)
    days_of_month = models.CharField(null=False, max_length=255)
    months = models.CharField(null=False, max_length=255)
