from django.contrib import admin

from .models import Category
from .models import Post
from .models import Comment
from .models import Tag

class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra =1

class PostAdmin(admin.ModelAdmin):
    list_display =('pk', 'title', 'created_at',)
    list_display_links = ('pk', 'title',)
    ordering = ('-id',)
    inlines =[CommentInlineAdmin]
    search_fields = ('title', 'content',)
    list_filter =('category',)
    date_hierarchy = ('created_at')

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
