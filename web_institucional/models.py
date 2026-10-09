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


# ==============================================================================
# ESTRUCTURA INVISIBLE DEL OBSERVATORIO DE LA JUSTICIA (Abib System)
# ==============================================================================

class AbogadoMatriculado(models.Model):
    CIRCUNSCRIPCIONES = [
        ('I', 'I - Capital'),
        ('II', 'II - Goya'),
        ('III', 'III - Curuzú Cuatiá'),
        ('IV', 'IV - Paso de los Libres'),
        ('V', 'V - Santo Tomé'),
    ]
    
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    matricula = models.CharField(max_length=50, unique=True, verbose_name="Número de Matrícula (Tomo/Folio)")
    circunscripcion = models.CharField(max_length=5, choices=CIRCUNSCRIPCIONES, verbose_name="Circunscripción")
    correo_electronico = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    
    # Control de seguridad e histórico para la secretaria del Consejo
    esta_validado = models.BooleanField(default=False, verbose_name="Cuenta Validada por Mail")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Abogado Registrado"
        verbose_name_plural = "Observatorio - Padrón de Abogados"
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre_completo} - Mat: {self.matricula} ({self.get_circunscripcion_display()})"



class VotoEncuesta(models.Model):
    OPCIONES_CALIFICACION = [
        ('A', 'Óptimo / Satisfactorio'),
        ('B', 'Regular / Necesita Reformas'),
        ('C', 'Deficiente / Colapso Institucional'),
    ]
    
    # Campo para organizar por los semestres históricos que pidió la presidenta
    periodo_semestral = models.CharField(max_length=30, verbose_name="Período (Ej: 2026-2S)")
    circunscripcion_juzgado = models.CharField(max_length=5, verbose_name="Circunscripción del Juzgado")
    fuero_afectado = models.CharField(max_length=50, verbose_name="Fuero con Mayor Retraso")
    
    # Guarda el poroto de la calificación general para armar el gráfico de torta
    calificacion_global = models.CharField(max_length=1, choices=OPCIONES_CALIFICACION, verbose_name="Calificación del Juzgado")
    fecha_voto = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Voto Anónimo del Observatorio"
        verbose_name_plural = "Observatorio - Bolsa de Votos Anónimos"

    def __str__(self):
        return f"Voto {self.periodo_semestral} - Fuero: {self.fuero_afectado} ({self.get_calificacion_global_display()})"
