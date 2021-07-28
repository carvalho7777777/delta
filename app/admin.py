from django.contrib import admin
from . models import Sponsor, Schedule, Feedback, Faq, Coach, History, Post, AttendanceRecord
from django.contrib.sessions.models import Session
from django.contrib.admin import ModelAdmin


@admin.register(AttendanceRecord)
class Attendancerecord(admin.ModelAdmin):
    """Вход выход пользователей"""
    list_display = ['user', 'login_time', 'logout_time']


@admin.register(Session)
class SessionAdmin(ModelAdmin):
    """Сессии"""
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    """Партнеры - Спонсоры"""	
    list_display = ['ordernumber', 'name', 'admin_logo', 'url', 'active',]
    fields = ['ordernumber', 'name', 'image', 'admin_logo', 'description', 'url', 'active', 'date_joined', ]
    list_display_links = ['name', 'admin_logo']
    readonly_fields = ('date_joined', 'admin_logo')
    list_editable = ['active']
    save_on_top = True


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Расписание занятий"""	
    list_display = ['ordernumber', 'years', 'admin_logo', 'district', 'address', 'schedule', 'post', 'contact', 'phone', 'active']
    list_editable = ['active']
    list_display_links = ['years', 'admin_logo']
    save_on_top = True

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Форма обратной связи"""
    list_display = ['name', 'email', 'phone', 'text', 'date']
    save_on_top = True

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    """Часто задаваемые вопросы"""
    list_display = ['ordernumber', 'title', 'text', 'active']
    list_display_links = ['title',]
    list_display_links = ['title',]
    list_editable = ['active']
    save_on_top = True


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    """Тренерский штаб"""
    list_display = ['ordernumber', 'name', 'post', 'admin_logo', 'bith', 'active']
    list_display_links = ['name', 'admin_logo']
    fields = ['ordernumber', 'name', 'post', 'bith', 'image', 'admin_logo', 'instagram', 'facebook', 'twitter', 'active', 'date_joined',]
    list_editable = ['active']
    readonly_fields = ('date_joined', 'admin_logo')
    save_on_top = True


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    """История клуба"""
    list_display = ['year', 'admin_logo', 'name', 'description', 'active',]
    #list_display_links = ['name', 'admin_logo']
    fields = ['year', 'name', 'description','image', 'active', 'date_joined',]
    list_editable = ['active']
    readonly_fields = ('date_joined',)
    save_on_top = True    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Посты блога"""
    list_display = ['title', 'content_upload', 'active', 'head', 'date_joined']
    fields = ['title', 'image', 'content_upload', 'slug', 'active', 'head', 'date_joined']
    list_editable = ['active', 'head']
    readonly_fields = ('date_joined',)
    save_on_top = True

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     """комментарии к постам"""
#     list_display = ['__str__', 'post', 'user', 'body', 'date']
#     # fields = ['title', 'image', 'content_upload', 'slug', 'active', 'head', 'date_joined']
#     # list_editable = ['active', 'head']
#     # readonly_fields = ('date_joined',)
#     # save_on_top = True