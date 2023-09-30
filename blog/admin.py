from django.contrib import admin

from .models import Blog, BlogAuthor, BlogComment


class BlogInline(admin.TabularInline):
    model = Blog
    extra = 0


class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "name",
        "post_date",
    )
    list_filter = ("author", "post_date")
    fields = (
        "author",
        "name",
        "description",
        "post_date",
    )
    inlines = [BlogCommentInline]


@admin.register(BlogAuthor)
class BlogAuthorAdmin(admin.ModelAdmin):
    inlines = [BlogInline]


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("description", "blog", "author", "post_date")
    list_filter = ("author", "post_date")
    fields = (
        "author",
        "blog",
        "description",
        "post_date",
    )
