from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import User, Group
from .models import Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]


# To unregister Group model.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
