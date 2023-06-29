class PC:
    def __init__(self, brand, CPU):
        self.brand = brand
        self.CPU = CPU

    def work(self):
        print(self.brand)
        print(self.CPU)


class GamingPC(PC):
    def __init__(self, brand, CPU, GPU, RAM):
        super().__init__(brand, CPU)
        self.GPU = GPU
        self.RAM = RAM

    def game(self):
        print(self.brand)
        print(self.CPU)
        print(self.GPU)
        print(self.RAM)


pc = PC('HP', 'i-9')
gaming = GamingPC('ASUS', 'Ryzen', 'Nvidia', '32 GB')

comp = input('Введите какой компьютер Вам нужен(игровой, рабочий)')
if comp == 'игровой':
    gaming.game()
elif comp == 'рабочий':
    pc.work()
else:
    print('Ошибка!Проверьте правильность написания запроса')


