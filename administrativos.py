# administrativos.py
from persona import Persona

class Administrativos(Persona):
    def __init__(self):
        super().__init__()
        self._cargo = ""
        self.area = ""

    # Getter y Setter
    def get_cargo(self):
        return self._cargo

    def set_cargo(self, cargo):
        self._cargo = cargo

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Cargo: {self._cargo}, Area: {self.area}"