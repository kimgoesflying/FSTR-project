from django.contrib import admin
from django import forms
from mountain_pass.models import *
# Register your models here.


@admin.register(Tourist)
class TouristAdmin(admin.ModelAdmin):
    eadonly_fields = ('id', )
    list_display = [
        'id', 'get_full_name', 'email', 'phone',
    ]


class MountainPassImageForm(forms.ModelForm):

    binary_image = forms.FileField(required=False)

    def save(self, commit=True):
        if self.cleaned_data.get('binary_image') is not None \
                and hasattr(self.cleaned_data['binary_image'], 'file'):
            data = self.cleaned_data['binary_image'].file.read()
            self.instance.binary_image = data
        return self.instance

    def save_m2m(self):
        # FIXME: this function is required by ModelAdmin, otherwise save process will fail
        pass


@admin.register(MountainPassImage)
class MountainPassImageAdmin(admin.ModelAdmin):
    form = MountainPassImageForm
    readonly_fields = ('id', )
    list_display = ('id',  'binary_image_tag', 'title',)


@admin.register(MountainPass)
class MountainPassAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ('id', 'title',)
