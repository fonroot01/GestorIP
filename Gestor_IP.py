# Este script permite cambiar la IP de una interfaz de red en Windows y restaurar la configuración DHCP.
# Requiere permisos de administrador para ejecutar comandos de red.
# Soy Alfonso, saludos!!1

import os
import sys
import ctypes
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk

# Verificar si el script tiene permisos de administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Solicitar permisos si no los tiene
if not is_admin():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    respuesta = messagebox.askyesno("Permisos de administrador requeridos",
                                    "Este script necesita permisos de administrador para cambiar la IP.\n\n¿Deseas otorgarlos ahora?")
    if respuesta:
        # Relanza el script como administrador
        params = " ".join([f'"{arg}"' for arg in sys.argv])
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    else:
        messagebox.showinfo("Salida", "El script se cerrará porque no tiene permisos.")
    sys.exit()


def main():
    root = tk.Tk()
    root.title("Gestor de IP - Windows")  # Título de la ventana
    root.geometry("600x400")  # Tamaño de la ventana
    root.iconbitmap(r"C:\PROYECTOS_Python\Cambio de IP temporalmente\logo.ico")
# Función para ejecutar comandos
def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout.strip(), result.stderr.strip(), result.returncode

# Obtener interfaces de red
def get_interfaces():
    cmd = 'netsh interface show interface'
    out, err, code = run_cmd(cmd)
    interfaces = []
    if code == 0:
        lines = out.splitlines()[3:]  # Saltamos encabezados
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 4:
                interface_name = " ".join(parts[3:])
                interfaces.append(interface_name)
    return interfaces

# Establecer IP estática sin gateway
def set_static_ip():
    iface = iface_combo.get()
    ip = ip_entry.get()
    mask = mask_entry.get()

    if not all([iface, ip, mask]):
        messagebox.showerror("Error", "Debes llenar todos los campos.")
        return

    # Guardar configuración actual
    out, err, code = run_cmd(f'netsh interface ip show config name="{iface}"')
    if code == 0:
        with open("ip_backup.txt", "w") as f:
            f.write(out)

    # Comando para aplicar nueva IP sin gateway
    cmd = f'netsh interface ip set address name="{iface}" static {ip} {mask} none'
    out, err, code = run_cmd(cmd)
    if code == 0:
        messagebox.showinfo("Éxito", f"IP cambiada a {ip}")
    else:
        messagebox.showerror("Error", f"No se pudo cambiar la IP:\n{err}")

# Restaurar DHCP
def restore_dhcp():
    iface = iface_combo.get()
    if not iface:
        messagebox.showerror("Error", "Selecciona una interfaz.")
        return

    cmds = [
        f'netsh interface ip set address name="{iface}" source=dhcp',
        f'netsh interface ip set dnsservers name="{iface}" source=dhcp'
    ]
    for cmd in cmds:
        out, err, code = run_cmd(cmd)
        if code != 0:
            messagebox.showerror("Error", f"Error al restaurar DHCP:\n{err}")
            return

    messagebox.showinfo("Éxito", "Configuración restaurada a DHCP.")

# Interfaz gráfica
root = tk.Tk()
root.title("Gestor de IP - Windows")
root.geometry("420x270")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

interfaces = get_interfaces()

ttk.Label(frame, text="Selecciona interfaz:").grid(row=0, column=0, sticky="e")
iface_combo = ttk.Combobox(frame, values=interfaces, width=27, state="readonly")
iface_combo.grid(row=0, column=1)
if interfaces:
    iface_combo.set(interfaces[0])

ttk.Label(frame, text="Nueva IP:").grid(row=1, column=0, sticky="e")
ip_entry = ttk.Entry(frame, width=25)
ip_entry.grid(row=1, column=1)

ttk.Label(frame, text="Máscara de subred:").grid(row=2, column=0, sticky="e")
mask_entry = ttk.Entry(frame, width=25)
mask_entry.grid(row=2, column=1)

ttk.Button(frame, text="Cambiar IP", command=set_static_ip).grid(row=4, column=0, pady=15)
ttk.Button(frame, text="Restaurar DHCP", command=restore_dhcp).grid(row=4, column=1)

root.mainloop()

if __name__ == "__main__":
    main()