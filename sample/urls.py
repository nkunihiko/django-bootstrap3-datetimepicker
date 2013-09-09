from django.conf import settings
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'.*', 'sample.todo_app.views.edit'),
)

from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)