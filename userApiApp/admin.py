from django.contrib import admin
from .models import UserData
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class StudentResource(resources.ModelResource):
   class Meta:
      model = UserData

class UserDataAdmin(ImportExportModelAdmin):
   resource_class = StudentResource

admin.site.register(UserData, UserDataAdmin)