from django.contrib import admin
from .models import Registrant


class RegistrantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'payment_method',
                    'amount', 'transaction_id', 'approved', 'registration_date')
    list_filter = ('approved', 'payment_method')
    search_fields = ('full_name', 'email', 'mobile')

admin.site.register(Registrant, RegistrantAdmin)
