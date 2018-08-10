from car import Car

class Battery():
    """Uma tentativa simples de modelar uma bateria para um carro eletrico."""
    
    def __init__(self, battery_size=70):
        """Inicializa os atributos da bateria."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Exibe uma frase sobre a distancia que o carro é capaz de percorrer com essa bateria."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Modela aspectos de um carro especifico de veiculos eletricos."""

    def __init__(self, make, model, year):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos especificos de um carro eletrico.
        """
        super().__init__(make, model, year)
        self.battery = Battery()