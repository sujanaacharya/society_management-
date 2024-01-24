

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import SocietyMember, Event, Announcement, Comment

@admin.register(SocietyMember)
class SocietyMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'contact_number', 'email', 'is_approved')
    list_filter = ('is_approved',)
    search_fields = ('full_name', 'contact_number', 'user__email') 

    actions = ['approve_selected_users']

    def approve_selected_users(self, request, queryset):
        queryset.update(is_approved=True)

    approve_selected_users.short_description = "Approve selected users"

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'event_time', 'created_by')
    list_filter = ('created_by',)
    search_fields = ('title',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'posted_on', 'is_approved')
    list_filter = ('posted_by', 'is_approved')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'posted_by', 'posted_on', 'related_announcement')
    list_filter = ('posted_by', 'posted_on')
    search_fields = ('text',)


# admin.py


