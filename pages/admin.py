from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated')
    ordering = ('title',)
    search_fields = ('title',)


admin.site.register(Page, PageAdmin)
