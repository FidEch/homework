class Vehicle:
    def __init__(self, name, model, color, engine_power):
        self.name = name
        self.model = model
        self.engine_power = engine_power
        self.color = color
        self.COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        return f'Модель: {self.model}'
    def  get_horsepower(self):
        return f'Мощность двигателя: {self.engine_power}'
    def get_color(self):
        return f'Цвет транспорта: {self.color}'
    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f'Имя владельца: {self.name}', sep='\n')

    def set_color(self, new_color):
        if new_color.lower() in self.COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на', new_color)
    def owner (self, new_name):
        self.name = new_name




class Sedan(Vehicle):
        PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()