class DashboardManager:
    def __init__(self):
        self.ruta_base = os.path.dirname(__file__)
        self.unidades = {'1': 'Unidad 1', '2': 'Unidad 2'}

    # métodos mostrar_menu, mostrar_codigo, etc.

    def mostrar_sub_menu(self, ruta_unidad):
        # Validación de seguridad añadida en este commit
        if not os.path.exists(ruta_unidad):
            print(f"\n[!] Error: La carpeta '{os.path.basename(ruta_unidad)}' no existe.")
            return

        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
        # resto del código con prints más esteticos

        def registrar_acceso(self, nombre_script):
            """Registra qué script se ejecutó y en qué fecha/hora."""
            from datetime import datetime
            try:
                with open("historial_ejecucion.txt", "a", encoding="utf-8") as log:
                    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.write(f"[{fecha}] Se visualizó/ejecutó: {nombre_script}\n")
            except Exception as e:
                print(f"No se pudo registrar el log: {e}")

        # Luego, llama a self.registrar_acceso(scripts[indice])
        # dentro de mostrar_scripts antes de mostrar el código.