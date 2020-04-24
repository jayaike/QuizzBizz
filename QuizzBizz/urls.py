from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quiz.urls')),
    path('api/auth/', include('accounts.urls')),
    path('nested_admin', include('nested_admin.urls')),
]
