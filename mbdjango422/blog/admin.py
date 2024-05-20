from django.contrib import admin
from .models import Category, Post, Comment
from core.notification import enviar_notificacion


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',
                    'PostCategories')
    list_filter = ('status', 'created', 'publish', 'author__username')
    search_fields = ('title', 'body', 'autor__username', 'categories__name')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', '-publish')

    def PostCategories(self, obj):
        return ', '.join(
            [c.name for c in obj.categories.all().order_by('name')])

    PostCategories.short_description = 'Categorías'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        enviar_notificacion(
            request,
            objeto=obj,
            key='blog',
            contents_es='Nuevo artículo añadido.',
            web_buttons_text='Ir al artículo.',
        )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active', 'politica')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
