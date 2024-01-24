from django import forms
from .models import SocietyMember
from .models import Announcement
from django.contrib.auth.forms import UserCreationForm

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'content']

# class SocietyMemberAdminForm(forms.ModelForm):
#     class Meta:
#         model = SocietyMember
#         fields = '__all__'


class SignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = SocietyMember
        fields = ('username', 'password1', 'password2', 'full_name', 'contact_number', 'email')