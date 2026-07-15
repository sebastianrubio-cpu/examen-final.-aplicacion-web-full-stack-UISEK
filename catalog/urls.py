from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.core_urls if hasattr(admin.site, 'core_urls') else admin.site.urls),
    path('api/', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/v1/catalog/', include('catalog.urls')),
    path('favicon.ico', lambda _: HttpResponse(status=204)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)