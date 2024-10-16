# Clase base Vehiculo
class Vehiculo:
    def mover(self):
        """Método base que debe ser sobrescrito por las clases hijas."""
        raise NotImplementedError("Este método debe ser sobrescrito en una clase hija")


class Coche(Vehiculo):
    def mover(self):
        """El coche se mueve por la carretera."""
        return "El coche se está moviendo por carretera."


class Barco(Vehiculo):
    def mover(self):
        """El barco se mueve por el agua."""
        return "El barco se está moviendo por el agua."


class Avion(Vehiculo):
    def mover(self):
        """El avión vuela en el aire."""
        return "El avión está volando en el aire."


class Bicicleta(Vehiculo):
    def mover(self):
        """La bicicleta se mueve pedaleando."""
        return "La bicicleta se está moviendo por la vía ciclista."


vehiculos = [Coche(), Barco(), Avion(), Bicicleta()]

for vehiculo in vehiculos:
    print(vehiculo.mover())