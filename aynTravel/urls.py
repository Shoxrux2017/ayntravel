from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from aynTravelApp.views import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aynTravelApp.url')),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    