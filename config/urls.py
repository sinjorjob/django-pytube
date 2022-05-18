from django.contrib import admin
from django.urls import path, include  #includeを追加
from django.conf import settings #追加
from django.conf.urls.static import static #追加
from YTVdownloader import views #追加


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.YoutubeDownloader.as_view(), name="index")  #追加
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #追加