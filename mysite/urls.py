"""mysite URL Configuration

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
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]




# from django.conf.urls import include, url
# from django.contrib import admin
#
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'', include('blog.urls')),
# ]
#
#
#
#
# from django.urls import path, re_path
#
# from . import views
#
# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
#     re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
#     re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
# ]