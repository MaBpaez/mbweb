from django.contrib import admin
from .models import Work, CategoryWork


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author__username")
    search_fields = ("title", "body", "autor__username", "categories__name")
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ("status", "-publish")


@admin.register(CategoryWork)
class CategoryWorkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
