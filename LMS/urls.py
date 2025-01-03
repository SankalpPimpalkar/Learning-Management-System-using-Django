from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from .views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing_page'),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('app.urls')),
    
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)