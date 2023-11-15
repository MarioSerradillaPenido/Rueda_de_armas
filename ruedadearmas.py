class arma:
    def __init__(self, tipo, nombre, ammo, daño, recarga, rango):
        self.tipo = tipo
        self.nombre = nombre
        self.ammo = ammo
        self.daño = daño
        self.recarga = recarga
        self.rango

class pistola(arma):
    def __init__(self, tipo, nombre, ammo, daño, recarga, rango):
        super().__init__(tipo, nombre, ammo, daño, recarga, rango)
