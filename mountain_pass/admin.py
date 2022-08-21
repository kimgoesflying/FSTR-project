from django.contrib import admin
from mountain_pass.models import *
# Register your models here.


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    list_display = [
        'get_full_name', 'email', 'phone',
    ]


admin.site.register(MountainPass)
admin.site.register(Coordinates)
admin.site.register(MountainPassImage)
