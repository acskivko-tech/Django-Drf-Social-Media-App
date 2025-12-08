from django.contrib import admin

from core.models import Genre, Post


# Register your models here.



@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name','author__username')
    list_filter = ('name',)



@admin.register(Post)
class BlogMessageAdmin(admin.ModelAdmin):
    list_display = ('title','author','content','date','genre')
    list_display_links = ('title',)
    list_filter = ('author','date','genre')
    search_fields = ('title','author')
