from django.urls import path
from . import views
# from .views import CommentsDeleteView

app_name = 'app'


urlpatterns = [
    path('', views.main, name='main'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('news/', views.news, name='news'),
    path('post-detail/<slug:slug>/', views.post_detail, name='detail'),
    # path('delete/<int:pk>/', views.CommentsDeleteView.as_view(), name='comment_delete'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('team/', views.team, name='team'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('support/', views.support, name='support'),
    path('privacy/', views.privacy, name='privacy'),
]
