from django.contrib import admin
from django.urls import path, include
from django.conf import settings
import debug_toolbar

from .view import universal_page_test_pages


urlpatterns = [
    # т.к. в примерах я не использую named url,
    # но в реальном проекте бы использовал
    path('', universal_page_test_pages),
    path('news/', universal_page_test_pages),
    path('news/it/ai/', universal_page_test_pages),
    path('news/it/', universal_page_test_pages),
    path('photo/', universal_page_test_pages),
    path('news/politics/', universal_page_test_pages),


    path('admin/', admin.site.urls),
    path('about/', include('about.urls', namespace='about')),
]

handler404 = 'core.views.page_not_found'
handler403 = 'core.views.permission_denied'
handler500 = 'core.views.server_error'

if settings.DEBUG:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
