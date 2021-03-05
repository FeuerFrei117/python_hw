"""
1) Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

2) Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.

3) Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


class OfficeEquipmentWarehouse:
    pass


class ComputerEquipment:
    pass


class Other:
    pass


class OfficeEquipment:
    goods = {}

    def __init__(self, country, mains_voltage, compatibility):
        self.country = country
        self.mains_voltage = mains_voltage
        self.compatibility = compatibility

    '''Может быть неправильно реализовал, но она работает. Логика в том, что ее мы вызываем в классе с полностью
     описанным товаром и пишем только колличеество товара'''
    def acceptance_of_goods(self, amount):
        while True:
            try:
                self.goods[self.company_name, self.device_type, self.model] = int(amount)
                break
            except ValueError:
                amount = input('Вы ввели строку при приемке товара, а необходимо число!\nВведите число: ')

    """Так же, как и метод сверху, но все работает. Записывает все перемещения в файл и отнимает перемещенное кол. 
    оргтехники от факта(goods). Через 'try' не сообразил как тут сделать обработку ошибки"""
    def the_movement_of_goods(self, amount, company_division):
        while type(amount) == int:
            with open('the_movement_of_goods.txt', 'a', encoding='utf-8') as file:
                file.write(f'{self.company_name} {self.device_type} {self.model} в количестве {amount} было перемещено'
                           f' {company_division}\n')
                break
        else:
            amount = input('Вы ввели строку при приемке товара, а необходимо число!\nВведите число: ')

        self.goods[self.company_name, self.device_type, self.model] = self.goods[self.company_name, self.device_type,
                                                                                 self.model] - int(amount)


class Consumables:
    pass


class Printer(OfficeEquipment):
    def __init__(self, country, mains_voltage, compatibility, company_name, device_type, model, printing_technology,
                 print_color, print_speed_str_min):
        super().__init__(country, mains_voltage, compatibility)
        self.company_name = company_name
        self.device_type = device_type
        self.model = model
        self.printing_technology = printing_technology
        self.print_color = print_color
        self.print_speed_str_min = print_speed_str_min


class Scanner(OfficeEquipment):
    def __init__(self, country, mains_voltage, compatibility, company_name, device_type, model, sensor_type,
                 scan_speed_str_min):
        super().__init__(country, mains_voltage, compatibility)
        self.company_name = company_name
        self.device_type = device_type
        self.model = model
        self.sensor_type = sensor_type
        self.scan_speed_str_min = scan_speed_str_min


class Copier(OfficeEquipment):
    def __init__(self, country, mains_voltage, compatibility, company_name, device_type, model, max_resolution_dpi,
                 max_number_of_copies_per_cycle):
        super().__init__(country, mains_voltage, compatibility)
        self.company_name = company_name
        self.device_type = device_type
        self.model = model
        self.max_resolution_dpi = max_resolution_dpi
        self.max_number_of_copies_per_cycle = max_number_of_copies_per_cycle


printer_one = Printer('China', '220V', 'Linux, Windows, Mac OS', 'Pantum', 'printer', 'P2500NW', 'laser',
                      'black and white', '22')
scanner_one = Scanner('China', '220V', 'Linux, Windows, Mac OS', 'Canon', 'scanner', 'CanoScan LiDe 300', 'CIS', '6')
copier_one = Copier('China', '220V', 'Linux, Windows, Mac OS', 'HP', 'copier', 'Neverstop Laser 1200w', '600x600', '99')

printer_one.acceptance_of_goods(5)
scanner_one.acceptance_of_goods(10)
copier_one.acceptance_of_goods(7)
print(OfficeEquipment.goods)

printer_one.the_movement_of_goods(1, 'HR')
scanner_one.the_movement_of_goods(5, 'Office')
copier_one.the_movement_of_goods(2, 'Dir')
print(OfficeEquipment.goods)
