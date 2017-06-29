from django.db import models

ACL_ALLOW = "allow"
ACL_DENY = "deny"

ACL_TYPE = {
    ACL_ALLOW: 1,
    ACL_DENY: 2
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

    class Meta:
        abstract = True


class PersonACLEntry(BaseACLEntry):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)


class RoleACLEntry(BaseACLEntry):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)
