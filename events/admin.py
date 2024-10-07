from django.contrib import admin

from .models import Event, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]


admin.site.register(Event, EventAdmin)
