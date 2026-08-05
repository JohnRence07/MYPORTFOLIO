from django.contrib import admin
from .models import Project, PersonalInformation, Inquiry, Testimony

admin.site.register(Project)
admin.site.register(PersonalInformation)
admin.site.register(Inquiry)
admin.site.register(Testimony)
