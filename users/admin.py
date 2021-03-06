from django.contrib import admin
from users import models as user_models


# Register your models here.
@admin.register(user_models.LmsUser)
class LmsUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'leave_issuer', 'department')
