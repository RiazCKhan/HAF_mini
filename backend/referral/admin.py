from django.contrib import admin
from .models import ReferralItem, ReferralOrder, Referral


class ReferralItemAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "quantity",
    )


admin.site.register(ReferralItem, ReferralItemAdmin)


class ReferralOrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "client",
    )


admin.site.register(ReferralOrder, ReferralOrderAdmin)


class ReferralAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "agent",
        "status",
    )


admin.site.register(Referral, ReferralAdmin)
