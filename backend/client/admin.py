from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
  list_display = ("full_name", "agent", "phone_number", "address",)

admin.site.register(Client)
