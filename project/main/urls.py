from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar
from django.views.generic import TemplateView


urlpatterns = [
    path('',
         TemplateView.as_view(template_name='index.html'),
         name='main_menu'),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls', namespace='about')),
]

handler404 = 'core.views.page_not_found'
handler403 = 'core.views.permission_denied'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
