from django.urls import path, include
# from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('board.urls')),
    path('user/', include('user.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static('upload', document_root=settings.MEDIA_ROOT)