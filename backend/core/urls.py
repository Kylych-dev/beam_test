from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .yasg import urlpatterns as doc_ts
from apps.accounts.consumers import NotificationConsumer


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("api.route")),

]
urlpatterns += doc_ts

websocket_urlpatterns = [
    path("ws/notifications/", NotificationConsumer.as_asgi())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


