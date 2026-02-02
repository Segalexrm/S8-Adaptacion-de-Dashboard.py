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