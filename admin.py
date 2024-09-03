from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register the User model with the custom UserAdmin
admin.site.register(User, UserAdmin)

# Register the Property model
# @admin.register(Property)
# class PropertyAdmin(admin.ModelAdmin):
#     list_display = ('name', 'property_type', 'address', 'price')
#     search_fields = ('name', 'property_type', 'address')
#     list_filter = ('property_type',)
