class Soda:
    def __init__(self, ingredient):
        self.ingredient = ingredient

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')


soda = Soda(ingredient=input('Введите ингредиент:'))
soda.show_my_drink()
