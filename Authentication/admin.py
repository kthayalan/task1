from django.contrib import admin

# Register your models here.
from Authentication.models import User
admin.site.register(User)