from django.contrib import admin

from atoi.models import AtoiLog

@admin.register(AtoiLog)
class AtoiLogAdmin(admin.ModelAdmin):
    list_display = ['transaction_date','atoi_string','atoi_number']

