from django.contrib import admin

from .models import MpesaPayment


class MpesapAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phonenumber','amount', 'organization_balance')

admin.site.register(MpesaPayment, MpesapAdmin)