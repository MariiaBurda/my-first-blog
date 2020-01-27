from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail')
]




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