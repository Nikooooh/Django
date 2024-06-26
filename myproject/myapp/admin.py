from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ["title",]

admin.site.register(Post, PostAdmin)
