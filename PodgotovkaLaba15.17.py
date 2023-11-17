##################################################
# 1) Первое задание
# class Book:
#
#     def __init__(self, heading, name, name_publisher):
#         self.heading = heading
#         self.name = name
#         self.name_publisher = name_publisher
#
#     def get_info(self):
#         return f'''
# Заголовок: {self.heading}
# Имя автора: {self.name}
# Имя издателя: {self.name_publisher}'''
#     def change_heading(self, value):
#         self.heading = value
#
#     def change_name(self, value):
#         self.name = value
#
#     def change_name_publisher(self, value):
#         self.name_publisher = value
#
#     def __str__(self):
#         return f'{self.heading}, {self.name}, {self.name_publisher}'
# d = Book('Гарри Поттер', 'Дмитрий Чугунов', 'Огонек')
# print(d.get_info())
# d.change_heading('Изумрудный город')
# d.change_name('Илья Иванович')
# d.change_name_publisher('Холодок')
# print(d.get_info())
# print(d)
#
###########################################################################
# 2) Второе задание
# class Pet:
#
#     def __init__(self, name, animal_type, age):
#         self._name = name
#         self._animal_type = animal_type
#         self._age = age
#
#
#     def set_name(self, value):
#         self._name = value
#
#     def set_animal_type(self, value):
#         self._animal_type = value
#
#     def set_age(self, value):
#         self._age = value
#
#     def get_name(self):
#         return f'Имя: {self._name}'
#
#     def get_animal_type(self):
#         return f'Тип: {self._animal_type}'
#
#     def get_age(self):
#         return f'Возраст: {self._age}'
#
# pet1 = Pet(input('Имя: '), input('Тип: '), input('Возраст: '))
# print(pet1.get_name(), pet1.get_animal_type(), pet1.get_age())
# pet1.set_name(input('Введите имя для изменения: '))
# pet1.set_animal_type(input('Введите тип для изменения:'))
# pet1.set_age(input('Введите возраст для изменения: '))
# print(pet1.get_name(), pet1.get_animal_type(), pet1.get_age())
#
###########################################################################
# 3) Третье задание
# class Car:
#
#     def __init__(self, year_model, rttake, speed):
#         self._year_model = year_model
#         self.rttake = rttake
#         self._speed = speed
#
#     def accelerate(self):
#         self._speed += 5
#
#     def break_speed(self):
#         self._speed -= 5
#
#     def get_speed(self):
#         print( f'Текущая скорость автомобиля: {self._speed}')
#
# car1 = Car('Lada Granta', 'LADA', 100)
#
# car1.accelerate()
# car1.get_speed()
# car1.accelerate()
# car1.get_speed()
# car1.accelerate()
# car1.get_speed()
# car1.accelerate()
# car1.get_speed()
# car1.accelerate()
# car1.get_speed()
# car1.break_speed()
# car1.get_speed()
# car1.break_speed()
# car1.get_speed()
# car1.break_speed()
# car1.get_speed()
# car1.break_speed()
# car1.get_speed()
# car1.break_speed()
# car1.get_speed()
#
###########################################################################
# 4) Четвертое задание
# class Infoпnation:
#
#     def __init__(self, name, address, age, number):
#         self.name = name
#         self.address = address
#         self.age = age
#         self.number = number
#
#     def get_inf(self):
#         return f'''
# Имя: {self.name}
# Адрес: {self.address}
# Возраст: {self.age}
# Телефон: {self.number}'''
#
#     def set_name(self, value):
#         self.name = value
#
#     def set_adress(self, value):
#         self.address = value
#
#     def set_age(self, value):
#         self.age = value
#
#     def set_number(self, value):
#         self.number = value
#
# Dima = Infoпnation('Дмитрий', 'Г.Брянск', 15, '+79803328307')
# print(Dima.get_inf())
# Zena = Infoпnation('Евгений', 'Г.Севастополь', 18, '+7987631792')
# print(Zena.get_inf())
# Ilia = Infoпnation('Илья', 'Г.Шахтерск', 16, '+79103318330')
# print(Ilia.get_inf())
# Dima.set_name('Дмитрий Чугунов')
# Dima.set_adress('Г.Брянск ул новозыбковская д.16 кв.15')
# Dima.set_age('15 лет')
# Dima.set_number('+79155340924')
# print(Dima.get_inf())
#
###########################################################################
# 5) Пятое задание
# class Employee:
#
#     def __init__(self, name, number, department, rank):
#         self.name = name
#         self.number = number
#         self.department = department
#         self.rank = rank
#
#     def get_info(self):
#         return f'''
# Имя: {self.name}
# Идентификационный Номер: {self.number}
# Отдел: {self.department}
# Должность: {self.rank} '''
#
# name1 = Employee("Сьюзен", '47899', 'Бухгалтерия', 'Вице-президент')
# print(name1.get_info())
# name2 = Employee("МаркДжоунс", '39119', 'ИТ', 'Программист')
# print(name2.get_info())
# name3 = Employee("Джой Роджемс", '81774', ' Производственный', 'Инженер')
# print(name3.get_info())
#
############################################################################
# 6) Шестое задание
# class Retailitem:
#
#     def __init__(self, description, quantity, price):
#         self.description = description
#         self.quantity = quantity
#         self.price = price
#
#     def get_info(self):
#         return f'''
# Описание: {self.description}
# Количество на складе: {self.quantity}
# Цена: {self.price}'''
#
#
# product1 = Retailitem("Пиджак", 12, 59.95)
# print(product1.get_info())
# product2 = Retailitem("Дизайнерские джинсы", 40, 34.95)
# print(product2.get_info())
# product3 = Retailitem("Рубашка", 20, 24.95)
# print(product3.get_info())
#
###########################################################################
# 7) Седьмое задание
# class Patient:
#
#     def __init__(self, name, patronymic, surname, address, city, area, index_number, number, name_emergency, number_emergency):
#         self.name = name
#         self.patronymic = patronymic
#         self.surname = surname
#         self.address = address
#         self.city = city
#         self.area = area
#         self.index_number = index_number
#         self.number = number
#         self.name_emergency = name_emergency
#         self.number_emergency = number_emergency
#         self.procedures = []
#     def set_name(self, value):
#         self.name = value
#
#     def set_patronymic(self, value):
#         self.patronymic = value
#
#     def set_surname(self, value):
#         self.surname = value
#
#     def set_address(self, value):
#         self.address = value
#
#     def set_city(self, value):
#         self.city = value
#
#     def set_area(self, value):
#         self.area = value
#
#     def set_index_number(self, value):
#         self.index_number = value
#
#     def set_number(self, value):
#         self.number = value
#
#     def set_name_emergency(self, value):
#         self.name_emergency = value
#
#     def set_number_emergency(self, value):
#         self.number_emergency = value
#
#     def get_name(self):
#         return f'''Имя Пациента: {self.name}'''
#
#     def get_patronymic(self):
#         return f'''Отчество Пациента: {self.patronymic}'''
#
#     def get_surname(self):
#         return f'''Фамилия Пациента: {self.surname}'''
#
#     def get_address(self):
#         return f'''Адрес Пациента: {self.address}'''
#
#     def get_city(self):
#         return f'''Город Пациента: {self.city}'''
#
#     def get_area(self):
#         return f'''Область Пациента: {self.area}'''
#
#     def get_index_number(self):
#         return f'''Почтовый индекс Пациента: {self.index_number}'''
#
#     def get_number(self):
#         return f'''Номер Пациента: {self.number}'''
#
#     def get_name_emergency(self):
#         return f'''Имя контактного лица для экстренной связи: {self.name_emergency}'''
#
#     def get_number_emergency(self):
#         return f'''Телефон контактного лица для экстренной связи: {self.number_emergency}'''
#
#     def add_procedure(self, procedure):
#         self.procedures.append(procedure)
#
#     def get_procedures(self):
#         result = ""
#         for procedure in self.procedures:
#             result += f'{procedure.get_procedure()}, {procedure.get_data_procedure()}, {procedure.get_name_doctor()}, {procedure.get_price_procedure()}\n'
#         return result
#
# class Procedure:
#
#     def __init__(self, procedure, data_procedure, name_doctor, price_procedure):
#         self.procedure = procedure
#         self.data_procedure = data_procedure
#         self.name_doctor = name_doctor
#         self.price_procedure = price_procedure
#
#     def set_procedure(self, value):
#         self.procedure = value
#
#     def set_data_procedure(self, value):
#         self.data_procedure = value
#
#     def set_name_doctor(self, value):
#         self.name_doctor = value
#
#     def set_price_procedure(self, value):
#         self.price_procedure = value
#
#     def get_procedure(self):
#         return f'''Название процедуры: {self.procedure}'''
#
#     def get_data_procedure(self):
#         return f'''Дата: {self.data_procedure}'''
#     def get_name_doctor(self):
#         return f'''Врач: {self.name_doctor}'''
#     def get_price_procedure(self):
#         return f'''Стоимость: {self.price_procedure}'''
#
# def get_price(procedures):
#     all_price = 0
#
#     for procedure in procedures:
#         all_price += procedure.price_procedure
#
#     return f'Общая цена: {all_price}'
# patient1 = Patient('Дмитрий', 'Александрович', 'Чугунов', 'ул.новозыбковская д.16 кв.15', 'Брянск', 'Брянская Область', 241414523, '+79803328307', 'Александр', '+79155340924')
# print(patient1.get_name(),patient1.get_patronymic(), patient1.get_surname(), patient1.get_address(), patient1.get_city(), patient1.get_area(), patient1.get_index_number(), patient1.get_number(), patient1.get_name_emergency(), patient1.get_number_emergency())
# patient1.set_name('Илья')
# patient1.set_patronymic('Федорович')
# patient1.set_surname('Хоборов')
# patient1.set_address('Шахтерск')
# patient1.set_city('Шахтерск')
# patient1.set_area('Хабаровская область')
# patient1.set_index_number(325252436)
# patient1.set_number('+79103318330')
# patient1.set_name_emergency('Дмитрий')
# patient1.set_number_emergency('+79803328307')
# print(patient1.get_name(),patient1.get_patronymic(), patient1.get_surname(), patient1.get_address(), patient1.get_city(), patient1.get_area(), patient1.get_index_number(), patient1.get_number(), patient1.get_name_emergency(), patient1.get_number_emergency())
# procedure_patient1 = Procedure('врачебный осмотр', 'сегодняшняя', 'Ирвин', 250.00)
# procedure_patient2 = Procedure('рентгеноскопия', 'сегодняшняя', 'Джемисон', 500.00)
# procedure_patient3 = Procedure('анализ крови', 'сегодняшняя', 'Смит', 200.00)
# patient1.add_procedure(procedure_patient1)
# patient1.add_procedure(procedure_patient2)
# patient1.add_procedure(procedure_patient3)
# print(patient1.get_procedures())
# print(get_price(patient1.procedures))
#######################################################################################################
