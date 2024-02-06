from django.contrib import admin

# Register your models here.
from OTS.models import *
admin.site.register(Candidate)
admin.site.register(Question)
admin.site.register(Result)