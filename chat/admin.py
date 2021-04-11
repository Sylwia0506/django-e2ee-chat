from django.contrib import admin
from django import forms

from chat.models import Profile, Invite


class InviteForm(forms.ModelForm):
    invite = forms.CharField(max_length=8, min_length=8)

    class Meta:
        model = Invite
        fields = ['invite']


class InviteAdmin(admin.ModelAdmin):
    form = InviteForm


admin.site.register(Invite, InviteAdmin)

# TODO: Make Profile readonly
# TODO: Hide public key and session key
admin.site.register(Profile)
