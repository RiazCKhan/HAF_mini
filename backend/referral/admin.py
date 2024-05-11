from django.contrib import admin
from .models import ReferralItem, Referral


class ReferralItemAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "quantity",
    )


admin.site.register(ReferralItem, ReferralItemAdmin)


class ReferralAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "agent",
        "status",
    )


admin.site.register(Referral, ReferralAdmin)
