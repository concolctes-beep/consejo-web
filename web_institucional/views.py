from django.shortcuts import render
from .models import Noticia, Circunscripcion, AlertaEmergente, Autoridad, Reglamento, Institucional
from django.core.mail import send_mail


def inicio(request):
    # 1. Buscamos las últimas 3 noticias publicadas
    noticias = Noticia.objects.all()[:3]
    
    # 2. Buscamos todas las circunscripciones de Corrientes (Goya, Capital, etc.)
    circunscripciones = Circunscripcion.objects.all()
    
    # 3. Buscamos si hay alguna alerta urgente activa
    alerta_activa = AlertaEmergente.objects.filter(activo=True).order_by('-fecha_creacion').first()
    
    # 4. Buscamos específicamente los datos de la Sede Central para el pie de página
    sede_central = Circunscripcion.objects.filter(nombre__icontains="Sede Central").first()
    
    # Empaquetamos todo en el "contexto" para mandarlo a la pantalla
    context = {
        'noticias': noticias,
        'circunscripciones': circunscripciones,
        'alerta_activa': alerta_activa,
        'sede_central': sede_central,  # <--- Enviamos la sede a la pantalla
    }
    
    return render(request, 'web_institucional/inicio.html', context)

def detalle_noticia(request, noticia_id):
    # Buscamos la noticia exacta por su número de documento (ID) en la base de datos
    noticia = Noticia.objects.get(id=noticia_id)
    # Se la mandamos empaquetada a la pantalla que creamos recién
    return render(request, 'web_institucional/detalle_noticia.html', {'noticia': noticia})

def autoridades(request):
    if request.method == 'POST':
        # 1. El cerebro agarra lo que el abogado escribió en las casillas
        nombre = request.POST.get('nombre_completo')
        correo_usuario = request.POST.get('email')
        asunto_motivo = request.POST.get('asunto')
        mensaje_cuerpo = request.POST.get('mensaje')

        # 2. Armamos el paquete del mail formal
        contenido_completo = f"Nombre: {nombre}\nCorreo: {correo_usuario}\n\nMensaje:\n{mensaje_cuerpo}"
        
        # 3. Mandamos el correo de verdad a la casilla del Consejo
        send_mail(
            subject=f"Contacto Web: {asunto_motivo}",
            message=contenido_completo,
            from_email=None,  # Usa el correo que configuramos en settings
            recipient_list=['Consejosupctes@hotmail.com'],  # A dónde va a llegar

            fail_silently=False,
        )

    comision = Autoridad.objects.all()
    return render(request, 'web_institucional/autoridades.html', {'comision': comision})

def reglamentos_view(request):
    lista_reglamentos = Reglamento.objects.all()
    return render(request, 'web_institucional/reglamentos.html', {'reglamentos': lista_reglamentos})


def mision_funcion_view(request):
    textos_institucionales = Institucional.objects.all()
    return render(request, 'web_institucional/mision_funcion.html', {'textos': textos_institucionales})

