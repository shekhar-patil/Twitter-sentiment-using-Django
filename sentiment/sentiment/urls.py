from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('TwitterSentiment/', include('TwitterSentiment.urls')),
    path('admin/', admin.site.urls),
]