from django.urls import path, re_path
from django.contrib.staticfiles import views as vew
from django.conf import settings
from .  import views

    
urlpatterns = [
    path('',views.Index.as_view(), name='index'),
    path('artist/<str:artist_name>', views.artist_detail, name='artist'),
    path('album/<int:album_id>',views.album_detail, name="album"),

]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', vew.serve),
    ]
    
