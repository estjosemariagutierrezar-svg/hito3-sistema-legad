import os
import re
import hashlib
import json
import tkinter as tk
from tkinter import messagebox, ttk

# -------------------------------------------------------------------
# SISTEMA LEGADO DE AUTENTICACIÓN Y VALIDACIÓN SEGURA DE DATOS
# Caso de uso: Migración y sanitización de datos de un sistema legado.
# -------------------------------------------------------------------

DB_FILE = "legacy_secure_db.json"

def hash_password(password: str) -> str:
    """Genera un hash SHA-256 seguro para proteger contraseñas almacenadas."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def cargar_datos_legados():
    """Carga los registros existentes o inicializa la base de datos simulada."""
    if not os.path.exists(DB_FILE):
        datos_iniciales = {
            "admin": hash_password("Admin123!"),
            "usuarios": []
        }
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(datos_iniciales, f, indent=4)
        return datos_iniciales
    
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_datos(datos):
    """Guarda los datos de forma segura en almacenamiento persistente."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

# -------------------------------------------------------------------
# VALIDACIONES DE SEGURIDAD (ENTRADAS DE USUARIO)
# -------------------------------------------------------------------

def validar_email(email: str) -> bool:
    """Valida el formato estándar de un correo electrónico."""
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(patron, email))

def validar_codigo_legado(codigo: str) -> bool:
    """Valida que el código del sistema legado coincida con el formato LEG-XXXXX."""
    patron = r'^LEG-\d{4,6}$'
    return bool(re.match(patron, codigo))

def sanitizar_texto(texto: str) -> str:
    """Sanitiza entradas para prevenir inyecciones de código o caracteres inválidos."""
    return re.sub(r'[<>&"\']', '', texto).strip()

# -------------------------------------------------------------------
# INTERFAZ GRÁFICA (TK
