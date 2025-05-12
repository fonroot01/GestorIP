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
```

### Ejecuta el script:
```bash
python Gestor_IP.py
```

Si no tienes permisos de administrador, el script te pedirá autorización para reiniciarse con los privilegios necesarios.

### ¿Como se usa?

1. Abre la aplicación.

2. Selecciona la interfaz de red que deseas configurar.

3. Ingresa la nueva IP y la máscara de subred.

4. Haz clic en Cambiar IP.

![ejecutando el programa](https://github.com/user-attachments/assets/eb092b60-15f6-4193-bcac-1a226b9f7c15)

"IP cambiada" -->> ![IP cambiada](https://github.com/user-attachments/assets/b78ad666-12d7-4380-b8fa-51548d895c3c)

5. Para volver a la configuración automática, presiona Restaurar DHCP.

![restaurada](https://github.com/user-attachments/assets/6a379ce6-b545-4893-b724-fd85d7b9d1b3)

"IP restablecida" -->> ![IP consola](https://github.com/user-attachments/assets/142163b7-d0d4-449c-93bc-83fbd28f5776)

### Personalización
Puedes agregar tu propio ícono modificando esta línea:
```bash
root.iconbitmap("ruta/a/tu/icono.ico")
```

⚠️ Nota
El script debe ejecutarse como administrador para aplicar cambios en la configuración de red. Si no lo haces, el sistema te pedirá permisos.

### Autor
Desarrollado por Alfonso Mosquera

### Licencia
Este proyecto es de código abierto bajo la licencia MIT.
¡Puedes modificarlo, usarlo y compartirlo libremente!
