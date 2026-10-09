from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from web_institucional.views import inicio, detalle_noticia, autoridades, reglamentos_view, mision_funcion_view , registro_observatorio_oculto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('noticia/<int:noticia_id>/', detalle_noticia, name='detalle_noticia'),
    path('autoridades/', autoridades, name='autoridades'),
    path('reglamentos/', reglamentos_view, name='reglamentos'),
    path('mision-funcion/', mision_funcion_view, name='mision_funcion'),
    path('observatorio/registro/', registro_observatorio_oculto, name='registro_observatorio_oculto'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
