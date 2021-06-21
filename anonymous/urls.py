from django.urls import path, include

urlpatterns = [
    path('', include('board.urls')),
    path('user/', include('user.urls')),
]
