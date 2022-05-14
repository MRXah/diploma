from django.contrib import admin

from .models import Contact, Place

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
    list_display_links = ('name', 'contact')
    search_fields = ('name', 'contact')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Place)
