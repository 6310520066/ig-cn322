
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('instagram.urls')),
    path('direct_message/', include("direct_message.urls")),
   
]
