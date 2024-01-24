from django.urls import path
from . import views

urlpatterns = [
    # General views accessible to all users
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),

    # Admin views
    path('approve_member/<int:member_id>/', views.approve_member, name='approve_member'),
    path('create_event/', views.create_event, name='create_event'),
    path('post_announcement/', views.post_announcement, name='post_announcement'),

    # signup
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('approve_user/<int:member_id>/', views.approve_user, name='approve_user'),

    # Authenticated user views
    path('view_approved_announcements/', views.view_approved_announcements, name='view_approved_announcements'),
    path('view_events/', views.view_events, name='view_events'),
     path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('post_comment/<int:announcement_id>/', views.post_comment, name='post_comment'),
    # path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
]
