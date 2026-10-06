from django.contrib import admin
from .models import Circunscripcion, Noticia, AlertaEmergente, Autoridad, Reglamento, Institucional

@admin.register(Circunscripcion)
class CircunscripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autoridad_local', 'telefono', 'email')
    search_fields = ('nombre', 'autoridad_local')
    list_filter = ('nombre',)

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido')
    list_filter = ('fecha_publicacion',)
    date_hierarchy = 'fecha_publicacion'  # Agrega una barra de navegación por fechas arriba

# Pegá esto abajo de todo para habilitar el formulario interactivo:
@admin.register(AlertaEmergente)
class AlertaEmergenteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'activo', 'fecha_creacion')
    list_editable = ('activo',)  # Esto te permite prender/apagar el cartel con un clic en el listado
    search_fields = ('titulo', 'contenido')


# Dejá tus registros viejos como están y pegá esta configuración abajo de todo:

@admin.register(Autoridad)
class AutoridadAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'nombre_completo', 'orden_visual')
    list_editable = ('orden_visual',)
    search_fields = ('nombre_completo', 'cargo')

@admin.register(Reglamento)
class ReglamentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_subida')
    search_fields = ('titulo',)

@admin.register(Institucional)
class InstitucionalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_actualizacion')
