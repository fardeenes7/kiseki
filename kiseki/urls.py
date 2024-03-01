from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer.views import about, terms, privacy

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("product.urls")),
    path("user/", include("customer.urls")),
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),
    path('about/', about, name='about'),
    path('terms', terms, name='terms'),
    path('privacy', privacy, name='privacy'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


