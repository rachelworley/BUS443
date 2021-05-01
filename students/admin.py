from django.contrib import admin
from students.models import Studentdetails
from students.models import Courseinfo
from students.models import Registrar

# Register your models here.
admin.site.register(Studentdetails)
admin.site.register(Courseinfo)
admin.site.register(Registrar)