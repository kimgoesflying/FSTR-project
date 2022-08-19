from django.contrib import admin
from mountain_pass.models import Tourist
# Register your models here.


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = [
        'get_full_name', 'email', 'phone',
    ]
