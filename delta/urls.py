from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar
from app.views import *

# /admin с двухфакторным входом
##########################################
from django_otp.admin import OTPAdminSite

class OTPAdmin(OTPAdminSite):
	pass

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice	
from app.models import Sponsor, Schedule, Feedback, Faq, Coach, History, Post
from app.admin import SponsorAdmin, ScheduleAdmin, FeedbackAdmin, FaqAdmin, CoachAdmin, HistoryAdmin, PostAdmin

admin_site = OTPAdmin(name='OTPAdmin')
# admin_site.register(User) # or admin.site.unregister(User)
admin_site.register(Sponsor, SponsorAdmin)
admin_site.register(Schedule, ScheduleAdmin)
admin_site.register(Feedback, FeedbackAdmin)
admin_site.register(Faq, FaqAdmin)
admin_site.register(Coach, CoachAdmin)
admin_site.register(History, HistoryAdmin)
admin_site.register(Post, PostAdmin)
# admin_site.register(Comment, CommentAdmin)
# admin_site.register(TOTPDevice)

# настройка в админке
admin_site.index_title = 'Админка сайта'
admin_site.site_title = 'Детский футбольный клуб Дельта'  
admin_site.site_header = 'ДФК Дельта'
###########################################		

urlpatterns = [
    path('admin/', admin_site.urls),
    path('myadmin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('account/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('app.urls', namespace='app')),
    path('__debug__/', include(debug_toolbar.urls)),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# подключение static и media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

# 404 ошибка
handler404 = pageNotFound
# handler500, handler403, handler400

# настройка в админке
admin.site.index_title = 'Админка сайта'
admin.site.site_title = 'Детский футбольный клуб Дельта'  
admin.site.site_header = 'ДФК Дельта'    