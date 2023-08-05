class Employe(object):
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = int(age)
        self.position = position
        self.salary = float(salary)

    def raise_salary(self):
        self.salary += 1000
        print('Зарплата была увеличена!')

    def get_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.salary)


employee = Employe('ilya', 23, 'programmer', 1000)
employee.raise_salary()
employee.get_info()

