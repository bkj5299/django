from django.contrib import admin

# Register your models here.
from first_app.models import Accessrecord,Webpage,Topic,Userprofileinfo
admin.site.register(Accessrecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(Userprofileinfo)
