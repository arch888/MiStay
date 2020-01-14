





from django.contrib import admin
from django.urls import path



#Custom Imports
from django.conf.urls.static import static
from django.conf import settings
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)