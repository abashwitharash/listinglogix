from django.contrib import admin

from .models import Property
from .models import UserProfile

admin.site.register(Property)
admin.site.register(UserProfile)
