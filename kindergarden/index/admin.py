from allauth.socialaccount.models import SocialApp
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from parler.admin import TranslatableAdmin

# from django.contrib.modeladmin.options import ModelAdmin
from .models import *

# Register your models here.
# class PeopleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'child')
#
# class KindergardInline(admin.TabularInline):
#      model = Kindergard.childrens.through
# #
# @admin.register(Children)
# class ChildAdmin(admin.ModelAdmin):
#      model=Children
#      inlines = [
#          KindergardInline
#      ]
admin.site.register(Perents)
# admin.site.register(Children)
admin.site.register(Children)
admin.site.register(Kindergarden,TranslatableAdmin)
admin.site.register(AdditLes)
admin.site.register(Child)

class UseAdmin(admin.ModelAdmin):
    list_display = ('last_name','address', 'phone', 'email')
admin.site.register(User,UseAdmin)
# admin.site.register(Membership)

# class SocialAppAdmin(ModelAdmin):
#     model = SocialApp
#     menu_icon = 'placehold'
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     list_display = ('name','provider')
#
#
# class SocialAuthGroup(ModelAdmin):
#     menu_label = 'Social Accounts'
#     menu_icon = 'users'
#     menu_order = 1200
#     items = (SocialAppAdmin,)
#
# admin.site.register(SocialAppAdmin)