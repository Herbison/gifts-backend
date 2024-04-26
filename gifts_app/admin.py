from django.contrib import admin
from .models import Member, Gift, Link

class LinkInline(admin.TabularInline):
    model = Link
    extra = 1

class GiftAdmin(admin.ModelAdmin):
    inlines = [LinkInline]

admin.site.register(Gift, GiftAdmin)
admin.site.register(Member)
admin.site.register(Link)