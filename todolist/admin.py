from django.contrib import admin

from todolist.models import Item, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'completed', 'deadline', 'update_date')
    list_display_links = ('id', )
    list_editable = ('content', 'completed', 'deadline')
    list_filter = ('completed', 'deadline')
    search_fields = ('content', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name', )
    search_fields = ('name', )
