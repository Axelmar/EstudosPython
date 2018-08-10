# Classe com valor default de odometer
class Car():

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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

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

# Declarando classe filha
class ElectricCar(Car):
    """Representa aspectos de um carro especificos de veiculos eletricos."""

    def __init__(self, make, model, year):
        """Inicializa os atributos da classe-pai."""
        super().__init__(make, model, year)
        self.battery = Battery()            # Utilizando instacia como atributo


my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()