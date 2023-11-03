from django.contrib import admin
from django.urls import path
from job import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path('about',views.aboutpage,name='about'),
    path('contact',views.contactus,name='contact'),

    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),

    path('homepage',views.home1, name='homepage'),
    path('about1',views.aboutfirst,name='about1'),
    path('contact1',views.contactfirst,name='contact1'),

    path('profile', views.profile, name='profile'),
    path('update', views.update, name='update'),

    path('result/', views.result, name='result'),
    path('job_application_form/<int:job_id>/', views.job_application_form, name='job_application_form'),

    path('job_applications_by_category/<str:category_name>/', views.job_applications_by_category, name='job_applications_by_category'),
    path('job_application_details/<int:application_id>/', views.job_application_details, name='job_application_details'),

    path('logout/', views.user_logout, name='logout'),
]
