from django.contrib import admin
from djoser.conf import User

from users.models import Genders, Country, CustomUser


# Register your models here.

@admin.register(Genders)
class GendersAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
    search_fields = ('country_name',)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','gender','age','country_born')
    list_display_links = ('username',)
    search_fields = ('username',)
    list_filter = ('is_staff','gender','age','country_born')
