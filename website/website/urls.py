"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from school import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.site.site_header = "Bhashyam Admin"
admin.site.site_title = "Bhashyam Admin Portal"
admin.site.index_title = "Welcome to Bhashyam Admin Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('pre',views.pre),
    path('middle',views.middle),
    path('high',views.high),
    path('events',views.event),
    path('approach/<title>',views.display_approach),
    path('events/<title>',views.display_event),
    path('gallery',views.gallery),
    path('gallery/<name>',views.gallery_group),
    path('blog',views.blog_page),
    path('blog/<title>',views.single_blog),
    path('about',views.about),
    path('contact',views.contact),
    path('school/<text>',views.school_text)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
