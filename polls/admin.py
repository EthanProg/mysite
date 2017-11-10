from django.contrib import admin

# Register your models here.

from .models import Question


# Make the poll app modifiable in the admin
admin.site.register(Question)
