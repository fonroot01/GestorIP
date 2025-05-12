# GestorIP - Cambia tu IP con un par de clics

GestorIP es una herramienta gráfica desarrollada en Python actualmente disponible solo para Windows que permite cambiar la dirección IP de forma rápida y sencilla sin necesidad de usar la consola. Ideal para administradores de red, técnicos de soporte o entusiastas que necesitan modificar su configuración de red con frecuencia.

## Características

- Interfaz gráfica amigable con `Tkinter` y `ttk`.
- Cambia la IP y máscara de subred fácilmente.
- Restaura la configuración DHCP con un clic.
- Lista automáticamente las interfaces de red disponibles.
- Solicita permisos de administrador automáticamente.
- Guarda la configuración anterior en un archivo de respaldo (`ip_backup.txt`).
- Incluye soporte para ícono personalizado (`.ico`).

## Requisitos

- Sistema operativo: Windows 10/11
- Python 3.x instalado
- Ejecutar como administrador (el script lo solicitará automáticamente)

## Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/fonroot01/GestorIP.git

### Ejecuta el script:

python Gestor_IP.py

Si no tienes permisos de administrador, el script te pedirá autorización para reiniciarse con los privilegios necesarios.

¿Cómo se usa?
Abre la aplicación.

Selecciona la interfaz de red que deseas configurar.

Ingresa la nueva IP y la máscara de subred.

Haz clic en Cambiar IP.

Para volver a la configuración automática, presiona Restaurar DHCP.

Personalización
Puedes agregar tu propio ícono modificando esta línea:

root.iconbitmap("ruta/a/tu/icono.ico")

⚠️ Nota
El script debe ejecutarse como administrador para aplicar cambios en la configuración de red. Si no lo haces, el sistema te pedirá permisos.

Autor
Desarrollado por Alfonso Mosquera
