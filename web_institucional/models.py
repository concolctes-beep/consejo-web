from django.db import models

class Circunscripcion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Circunscripción")
    autoridad_local = models.CharField(max_length=150, verbose_name="Presidente / Autoridad")
    enlace_oficial = models.URLField(verbose_name="Enlace Oficial (Link)", blank=True, null=True)
    direccion = models.CharField(max_length=200, verbose_name="Dirección Física", blank=True)
    telefono = models.CharField(max_length=50, verbose_name="Teléfono de Contacto", blank=True)
    email = models.EmailField(verbose_name="Correo Electrónico", blank=True)

    class Meta:
        verbose_name = "Circunscripción"
        verbose_name_plural = "Circunscripciones"

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título de la Noticia")
    contenido = models.TextField(verbose_name="Contenido de la Circular / Noticia")
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Publicación")

    foto_principal = models.ImageField(upload_to='noticias/', verbose_name="Foto Principal", blank=True, null=True)
    
    class Meta:
        verbose_name = "Noticia / Circular"
        verbose_name_plural = "Noticias y Circulares"
        ordering = ['-fecha_publicacion']  # Esto hace que la más nueva aparezca primero automáticamente



    def __str__(self):
        return self.titulo

class AlertaEmergente(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Comunicado Urgente")
    contenido = models.TextField(verbose_name="Texto de la Alerta / Información")
    imagen = models.ImageField(upload_to='alertas/', verbose_name="Imagen del Cartel (Opcional)", blank=True, null=True)
    activo = models.BooleanField(default=False, verbose_name="¿Mostrar este cartel en la web ahora mismo?")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Alerta Emergente (Pop-up)"
        verbose_name_plural = "Alertas Emergentes (Pop-up)"

    def __str__(self):
        return f"Alerta: {self.titulo} - [{'ACTIVA' if self.activo else 'APAGADA'}]"


class Autoridad(models.Model):
    nombre_completo = models.CharField(max_length=200, verbose_name="Nombre Completo")
    cargo = models.CharField(max_length=100, verbose_name="Cargo / Función")
    foto = models.ImageField(upload_to="autoridades/", blank=True, null=True, verbose_name="Foto de Perfil")
    orden_visual = models.IntegerField(default=0, verbose_name="Orden de aparición")

    class Meta:
        verbose_name = "Autoridad / Miembro Directivo"
        verbose_name_plural = "Comisión Directiva - Autoridades"
        ordering = ['orden_visual']

    def __str__(self):
        return f"{self.cargo} - {self.nombre_completo}"


class Reglamento(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título del Reglamento / Estatuto")
    archivo_pdf = models.FileField(upload_to="reglamentos/", verbose_name="Archivo PDF Oficial")
    fecha_subida = models.DateField(auto_now_add=True, verbose_name="Fecha de publicación")

    class Meta:
        verbose_name = "Reglamento / Estatuto"
        verbose_name_plural = "Estatutos y Reglamentos Oficiales"
        ordering = ['-fecha_subida']

    def __str__(self):
        return self.titulo


class Institucional(models.Model):
    titulo = models.CharField(max_length=200, default="Misión y Función", verbose_name="Título de la Sección")
    contenido = models.TextField(verbose_name="Texto Institucional / Leyes de Creación")
    fecha_actualizacion = models.DateField(auto_now=True, verbose_name="Última actualización")

    class Meta:
        verbose_name = "Texto de Misión y Función"
        verbose_name_plural = "Contenido de Misión y Función"

    def __str__(self):
        return self.titulo
