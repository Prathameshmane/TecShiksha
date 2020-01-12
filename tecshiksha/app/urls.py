from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('index',views.index, name = 'index'),
    path('about',views.about, name = 'about'),
    path('blog',views.blog, name = 'blog'),
    path('workshops',views.workshops, name = 'workshops'),
    path('internship',views.internship, name = 'internship'),
    path('about',views.about, name = 'about'),
    path('contact',views.contact, name = 'contact'),
    path('services',views.services, name = 'services'),
    path('courses',views.courses, name = 'courses'),
    # path('artificialintelligence-course',views.ai_page, name = 'artificialintelligence-course'),
    # path('iot-course',views.iot_page, name = 'iot-course'),
    # path('androidapp-course',views.android_app_page, name = 'androidapp-course'),
    # path('python-course',views.python_page, name = 'python-course'),
    # path('iosapp-course',views.ios_app_page, name = 'iosapp-course'),
    # path('webdesigning-course',views.web_designing_page, name = 'webdesigning-course'),
]
