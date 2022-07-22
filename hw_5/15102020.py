# def print_human_name(human):
#     print(human['name'])
#
#
# h1 = {'name': 'Roman'}
# h2 = {'name': 'Alexey'}
#
# print_human_name(h1)
#
# h3 = {'full_name': 'qwe'}
# print_human_name(h3)

# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def print_human_name(self):
#         print(self.name)
#
# human = Human('Roman')
# human.print_human_name()




class Phone:  # CamelStyle
    qwe = 0

    def __init__(self, phone_model):
        self.phone_model = phone_model
        self.__id = 984345
        self._loading()

    def call(self, number):
        self.last_calling_number = number
        print(f'calling {number}...')

    def _loading(self):
        print(self.phone_model, 'loading...')

    def get_id(self):
        return self.__id


# my_list1 = list()
# my_list2 = list()
# phone1 = Phone('nokia1100')
# phone1.__id = 0
# phone1._Phone__id = 0  # object._ClassName__foo
# print(phone1.get_id())
# phone1._loading()
# phone1.loading()

# print(phone1.phone_model)
# print(phone1.id)

# phone2 = Phone()
# phone1.call(8999999999)
# phone2.call(123)

class SmartPhone(Phone):
    def sms(self):
        print('sms sending')

    def email(self):
        print('email sending')


# my_sphone = SmartPhone('nokia6600')
# my_sphone.sms()
# print(my_sphone.get_id())

class Iphone(SmartPhone):

    def __init__(self, phone_model):
        super().__init__(phone_model)
        print('show logo')

    def player(self):
        print('player')

    def browser(self):
        print('browser')

    def sms(self):
        print('Imessage sending')


# iphone = Iphone('6')
# iphone.sms()


class Huawei(Iphone):
    pass


class Samsung(Iphone):
    pass


class Player:
    def player_method(self):
        print('Родительский класс player_method')

    def qwe_method(self):
        print('пришло от Player')


class Navigator:
    def navigator_method(self):
        print('Родительский класс navigator_method')

    def qwe_method(self):
        print('пришло от Navigator')


class MobilePhone(Player, Navigator):
    def mobile_phone(self):
        print('Дочерний mobile_phone')


# mp = MobilePhone()
# mp.mobile_phone()
# mp.navigator_method()
# mp.player_method()
# mp.qwe_method()

class Auto:
    def auto_start(self, param1, param2=None):
        if param2:
            print(param1 + param2)
        else:
            print(param1)


a = Auto()
a.auto_start(10)
a.auto_start(10, 20)
