from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ChannelAddAdmin(admin.ModelAdmin):
    list_display = ('id', 'channel_name', 'slug', 'get_html_photo', 'time_update', 'user')
    list_display_links = ('id', 'channel_name')
    search_fields = ('channel_name',)
    list_filter = ('user',)
    fields = ('channel_name', 'slug', 'channel_url', 'channel_desc', 'photo', 'get_html_photo', 'time_create', 'time_update', 'user')
    readonly_fields = ('get_html_photo', 'time_create', 'time_update', 'user')
    prepopulated_fields = {"slug": ("channel_name",)}

    list_editable = ('slug',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50 >",)

    get_html_photo.short_description = 'Фото'


admin.site.register(Channel)
admin.site.register(ChannelAdd, ChannelAddAdmin)

admin.site.site_title = "Админка"
admin.site.site_header = "Админка для этого сайта"
