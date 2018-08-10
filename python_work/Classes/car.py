"""Uma classe que pode ser usada para representar um carro."""

class Car():
    """Uma tentaiva simples de representar um carro."""

    def __init__(self, make, model, year):
        """Inicializa os atributos que descrevem um carro."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ Exibe uma frase que mostra a milhagem do carro."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Define o valor de leitura do hodometro com o valor especificado
        Rejeita alteracao se for tentativa de definir um valor menor para o hodometro
        """

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Soma a quantidade especificada ao valor de leitura do hodometro."""
        self.odometer_reading += miles