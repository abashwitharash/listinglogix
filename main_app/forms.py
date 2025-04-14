from django import forms
from .models import UserProfile, ListingImage

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'phone', 'agency', 'photo']


class ListingImageForm(forms.ModelForm):
    class Meta:
        model = ListingImage
        fields = ['image']