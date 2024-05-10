from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
  list_display = ("full_name", "agency", "email", "phone_number")

admin.site.register(Agent)
