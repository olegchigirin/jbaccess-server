from django.contrib import admin
from jba_core import models


# Register your models here.


admin.site.register(models.Person)
admin.site.register(models.Door)
admin.site.register(models.Key)
admin.site.register(models.AclType)
admin.site.register(models.BaseACLEntry)
admin.site.register(models.PersonACLEntry)
admin.site.register(models.Controller)
admin.site.register(models.Place)
admin.site.register(models.Role)
admin.site.register(models.RoleACLEntry)
admin.site.register(models.SimpleRecurringPattern)
