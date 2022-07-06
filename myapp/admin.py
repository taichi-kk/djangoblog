from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'created_at')
    list_display_links = ('title',)
    ordering = ('-created_at', )
