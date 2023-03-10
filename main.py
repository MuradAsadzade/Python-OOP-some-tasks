# class Player:

#     def __init__(self, name, age,health):
#         self.name = name
#         self.age = age
#         self.health = health

#     def __mul__(self, opponent):
#         count=0
#         opponent.health = opponent.health-self.weapon.power*self.weapon.number
#         print(opponent.health)
#         count+=1
#         if count==3:
#             print("Mermi bitdi")
#             return

# class Weapon:
#     def __init__(self, weapon_name,number):
#         self.weapon_name = weapon_name
#         self.number=number


# class Blowgun(Weapon):
#     power=100


# class Musket(Weapon):
#     power=80


# player1 = Player("Murad", 18, 95)
# weapon1 =Musket('Musket',5)


# player1.weapon=weapon1

# player2 = Player("Ayxan", 13, 90)
# player1*player2
# player1*player2
# player1*player2
# player1*player2


# class Silah:
#     metal = "qizil"

#     def __init__(self, gulle_sayi):
#         self.gulle_sayi = gulle_sayi


# class Avtomat(Silah):
#     power = 150
#     name = "avtomat"


# class Snayper(Silah):
#     power = 200
#     name = "snayper"


# class Soldier:
#     def __init__(self, health, gulle_sayi):
#         self.health = health
#         self.gulle_sayi = gulle_sayi

#     def shoot(self, opponent):
#         opponent.health = opponent.health-self.weapon.power
#         self.weapon.gulle_sayi-=1
#         print(opponent.health)

#     def __len__(self):
#         return self.weapon.gulle_sayi


# avtomat1 = Avtomat(5)
# snayper1 = Snayper(3)


# soldier1 = Soldier(1000, avtomat1.gulle_sayi)
# soldier1.weapon = avtomat1

# soldier2 = Soldier(800, snayper1.gulle_sayi)
# soldier2.weapon = snayper1

# soldier1.shoot(soldier2)
# soldier1.shoot(soldier2)
# # soldier1.shoot(soldier2)
# print(len(soldier1))
# soldier2.shoot(soldier1)


# class Termometr:
#     def __init__(self, celcius:int):
#         self.celcius = celcius
#         self.fahrenheit=self.celcius*1.8+32
#         self.kelvin = self.celcius+273

#     def get_kelvin(self):
#         print( self.kelvin)

#     def get_fah(self):
#         print(self.fahrenheit)

#     def get_celc(self):
#         print(self.celcius)

#     def fah_to_celc(self):
#         self.celcius=(self.fahrenheit-32)/1.8
#         return self.celcius

#     def kel_to_celc(self):
#         self.celcius=self.kelvin-273
#         return self.celcius

#     def celc_to_fah(self):
#         self.fahrenheit=self.celcius*1.8+32
#         return self.fahrenheit

#     def celc_to_kel(self):
#         self.kelvin=self.celcius+273
#         return self.kelvin

#     def add_fah(self, fah):
#         self.fahrenheit += fah
#         return self.fahrenheit

#     def sub_fah(self, fah):
#         self.fahrenheit -= fah
#         return self.fahrenheit

#     def add_kel(self, kel):
#         self.kelvin += kel
#         return self.kelvin

#     def sub_kel(self, kel):
#         self.kelvin += kel
#         return self.kelvin

#     def add_cel(self, cel):
#         self.celcius += cel
#         return self.celcius

#     def sub_cel(self, cel):
#         self.celcius -= cel
#         return self.celcius

#     def __add__(self, celci):
#         self.celcius += celci
#         return self.celcius

#     def __sub__(self, celci):
#         self.celcius -= celci
#         return self.celcius

#     def __mul__(self, celci):
#         self.celcius *= celci
#         return self.celcius

#     def __div__(self, celci):
#         self.celcius /= celci
#         return self.celcius

#     def show_temp(self):
#         print(f"Fahrenheit:{self.fahrenheit},Celci:{self.celcius},Kelvin:{self.kelvin}")


# temperature=Termometr(10)
# # temperature.add_fah(18)
# # temperature.fah_to_celc()
# # temperature.celc_to_kel()
# temperature-5
# temperature.celc_to_fah()
# temperature.celc_to_kel()
# temperature.show_temp()
# temperature.get_fah()
# temperature.get_kelvin()


# CameraSystem classinin each_camera_price adinda hidden bir propertysi olsun. Deyeri 50 verin
# class CameraSystem:
#     each_camera_price=50
#     def get_camera_price(self):
#         self.camera_price=self.each_camera_price*self.camera_count

#     def set_camera_count(self, count):
#         self.camera_count=count

# # MemorySystem classinin each_gb_price adinda hidden bir propertysi olsun. Deyeri 10 verin
# class MemorySystem:
#     each_gb_price=10
#     def set_memory_amount(self, amount):
#         self.memory_amount=amount

#     def get_memory_price(self):
#         self.memory_price=self.each_gb_price*self.memory_amount


# class SmartDevice(CameraSystem,MemorySystem):
#     def __init__(self, camera_count, memory_amount):
#         super().__init__()
#         self.camera_count=camera_count
#         self.memory_amount=memory_amount


# class Phone(SmartDevice):
#     def get_total_price(self):
#        self.total_price=self.memory_amount*self.each_gb_price+self.camera_count*self.each_camera_price
#        return self.total_price

# class PremiumPhone(SmartDevice):
#     def __init__(self, charger_price, camera_count, memory_amount):
#         super().__init__(camera_count, memory_amount)
#         self.charger_price=charger_price
#         self.camera_count=camera_count
#         self.memory_amount=memory_amount

#     def get_total_price(self):
#         self.total_price=self.charger_price+self.camera_count*self.each_camera_price+self.memory_amount*self.each_gb_price
#         return self.total_price

# class Laptop(SmartDevice):
#     def __init__(self, charger_price, camera_count, memory_amount):
#         super().__init__(camera_count, memory_amount)
#         self.charger_price=charger_price
#         self.camera_count=camera_count
#         self.memory_amount=memory_amount


#     def get_total_price(self):
#         self.total_price=self.charger_price+self.camera_count*self.each_camera_price+self.memory_amount*self.each_gb_price
#         return self.total_price

# class Tablet(SmartDevice):
#     def __init__(self, charger_price, camera_count, memory_amount):
#         super().__init__(camera_count, memory_amount)
#         self.charger_price=charger_price
#         self.camera_count=camera_count
#         self.memory_amount=memory_amount


#     def get_total_price(self):
#         self.total_price=self.charger_price+self.camera_count*self.each_camera_price+self.memory_amount*self.each_gb_price
#         return self.total_price

# samsung = Phone(4, 256)
# iphone = PremiumPhone(70, 3, 128)
# dell = Laptop(1,1, 512)
# huawei = Tablet(1,2, 256)

# def calculate_product_prices(*args):
#     total_product_price=0
#     for i in args:
#         total_product_price+=i.get_total_price()
#     return total_product_price

# print(calculate_product_prices(samsung, iphone, dell, huawei))


# class Kontur:
#     qiymetler={"mesaj":5,"zeng":10,"internet":20}
#     min_kontur=4
#     def __init__(self,kontur):
#         self.kontur=kontur

#     def kontur_cix(self,kontur):
#         self.kontur=self.kontur-self.qiymetler[kontur]
#         return self.kontur

#     def kontur_elave(self,kontur):
#         self.kontur=self.kontur+kontur
#         return self.kontur


# class Telefon(Kontur):
#     alinan_mesaj_list=[]
#     gonderilen_mesaj_list=[]
#     def mesaj_gonder(self,friend,mesaj):
#         self.gonderilen_mesaj_list.append(mesaj)
#         self.kontur=self.kontur-5
#         friend.alinan_mesaj_list.append(f'Sizə {mesaj} kontentli bildiriş gəldi')


# telefon1=Telefon(50)
# telefon1.kontur_cix("mesaj")
# telefon1.kontur_elave(10)
# # print(telefon1.kontur)
# telefon2=Telefon(30)
# telefon1.mesaj_gonder(telefon2,"Salam")
# telefon1.mesaj_gonder(telefon2,"Necesen")
# telefon2.mesaj_gonder(telefon1,"Sukur")
# # print(telefon1.gonderilen_mesaj_list)
# # print(telefon2.gonderilen_mesaj_list)
# print(telefon2.alinan_mesaj_list)


# class Termostat:

#     __min_celcius = -5
#     __max_celcius = 40

#     def __init__(self, celcius: float) -> None:
#         self.__celcius = celcius

#     @property
#     def celcius(self) -> float:
#         return self.__celcius

#     @celcius.setter
#     def celcius(self, value: float) -> None:
#         if value > self.__max_celcius:
#             raise ValueError(f'Temperature can\'t be bigger than {self.__max_celcius} Celcius')
#         elif value < self.__min_celcius:
#             raise ValueError(f'Temperature can\'t be lower than {self.__min_celcius} Celcius')
#         else:
#             self.__celcius = value

#     @property
#     def kelvin(self) -> float:
#         return self.celcius_to_kelvin(self.celcius)

#     @kelvin.setter
#     def kelvin(self, value: float) -> None:
#         celcius = self.kelvin_to_celcius(value)
#         if value > self.__max_celcius:
#             raise ValueError(f'Temperature can\'t be bigger than {self.__max_celcius} Kelvin')
#         elif value < self.__min_celcius:
#             raise ValueError(f'Temperature can\'t be lower than {self.__min_celcius} Kelvin')
#         else:
#             self.__celcius = celcius

#     @property
#     def fahrenheit(self) -> float:
#         return self.celcius_to_fahrenheit(self.celcius)

#     @staticmethod
#     def celcius_to_kelvin(celcius: float) -> float:
#         return celcius + 273

#     @staticmethod
#     def kelvin_to_celcius(kelvin: float) -> float:
#         return kelvin - 273

#     @staticmethod
#     def celcius_to_fahrenheit(celcius: float) -> float:
#         return celcius * 1.8 + 32

#     @staticmethod
#     def fahrenheit_to_celcius(fahrenheit: float) -> float:
#         return (fahrenheit - 32)/ 1.8

#     @classmethod
#     def get_termostat_by_kelvin(cls, kelvin: float) -> 'Termostat':
#         celcius = cls.kelvin_to_celcius(kelvin)
#         return cls(celcius)

#     @classmethod
#     def get_termostat_by_fahrenheit(cls, fahrenheit: float) -> 'Termostat':
#         celcius = cls.fahrenheit_to_celcius(fahrenheit)
#         return cls(celcius)


# termostat = Termostat(25)
# termostat2 = Termostat.get_termostat_by_kelvin(276)

# print(termostat2)
# print(termostat.celcius_to_kelvin(25))

# print(Termostat.celcius_to_kelvin(25))

# print(termostat.celcius)
# print(termostat.kelvin)
# print(termostat.fahrenheit)


# Person(name,surname),teacher(experience),student(grade),group(muellimlist,sagirdlist,ortalama qiymetler),School

# School oop

# class Person:
#     def __init__(self, name, surname, age):
#         self.__name = name
#         self.__surname = surname
#         self.__age = age

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @property
#     def surname(self):
#         return self.__surname

#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         self.__age = age


# class Teacher(Person):
#     @property
#     def experience(self):
#         return self.__experience


#     @experience.setter
#     def experience(self, experience):
#         self.__experience = experience


# class Student(Person):
#     def __init__(self, name, surname, age):
#         self.qiymetler = []

#     @property
#     def grade(self):
#         return self.__grade

#     @grade.setter
#     def grade(self, grade):
#         self.__grade = grade

#     @staticmethod
#     def yeni_qiymet(self, *grades):
#         for i in grades:
#             self.qiymetler.append(i)

#     @staticmethod
#     def average(self):
#         return sum(self.qiymetler)/len(self.qiymetler)


# class School:
#     def __init__(self):
#         self.average_qiymetler=[]
#         self.average_experience=[]
#         self.sinif_adlari=[]

#     @staticmethod

#     def class_elave(self,*sinifler):
#         for sinif in sinifler:
#             self.average_qiymetler.append(sinif.ortalama_qiymetler())
#             self.average_experience.append(sinif.average_teachers_experience())
#             self.sinif_adlari.append(sinif.sinif_name)


#     @staticmethod
#     def show_class_names(self):
#         return self.sinif_adlari

#     @staticmethod
#     def average_school_grade(self):
#         return sum(self.average_qiymetler)/len(self.average_qiymetler)

#     @staticmethod
#     def average_school_experience(self):
#         return sum(self.average_experience)/len(self.average_experience)


# class Sinif:
#     def __init__(self,student,teacher,sinif_name):
#         # super().__init__(name, surname, age)
#         self.umumi_qiymetler = [student.average()]
#         self.teacher_experience=[teacher.experience]
#         self.sinif_name=sinif_name

#         # self.qiymetler.append(student.average())
#     @staticmethod
#     def new_teacher_experience(self,*teachers):
#         for i in teachers:
#             self.teacher_experience.append(i)

#     @staticmethod
#     def all_teachers_experience(self):
#         return self.teacher_experience

#     @staticmethod
#     def average_teachers_experience(self):
#         return sum(self.teacher_experience)/len(self.teacher_experience)

#     @staticmethod
#     def yeni_sagird_qiymeti(self, sagird):
#         self.umumi_qiymetler.append(sagird.average())

#     @staticmethod
#     def umumi_qiymetler(self):
#         return self.umumi_qiymetler

#     @staticmethod
#     def ortalama_qiymetler(self):
#         return sum(self.umumi_qiymetler)/len(self.umumi_qiymetler)


# student1 = Student("Murad", "Asadzade", 18)
# student1.yeni_qiymet(5,6,7,8)

# # print(student1.average())

# student2 = Student("Ayxan", "Asadzade", 13)
# student2.yeni_qiymet(3,4,5)

# student3 = Student("Ayxan", "Asadzade", 13)
# student3.yeni_qiymet(1,2,3)

# student4 = Student("Ayxan", "Asadzade", 11)
# student4.yeni_qiymet(3,3,3)

# teacher1=Teacher("Murad","Asadzade",90)
# teacher1.experience=20

# teacher2=Teacher("Murad","Asadzade",100)
# teacher2.experience=30

# sinif1 = Sinif(student1,teacher2,"11a")
# sinif1.yeni_sagird_qiymeti(student2)
# sinif1.new_teacher_experience(20,30,10)
# # print(sinif1.ortalama_qiymetler())
# # print(sinif1.all_teachers_experience())
# # print(sinif1.average_teachers_experience())


# sinif2 = Sinif(student3,teacher1,"10b")
# sinif2.yeni_sagird_qiymeti(student4)
# sinif2.new_teacher_experience(10,30,10)
# # print(sinif1.ortalama_qiymetler())
# # print(sinif2.ortalama_qiymetler())


# school1=School()
# school1.class_elave(sinif1,sinif2)
# print(school1.average_school_grade())
# print(school1.average_school_experience())
# print(school1.show_class_names())


# class Ferma:
#     __pul = 0
#     __yem_sayi = 15

#     def __init__(self, *args):
#         self.heyvanlar = []
#         for i in args:
#             if i == "inek" or i == "qoyun" or i == "toyuq":
#                 self.heyvanlar.append(i)

#     @staticmethod
#     def yumurta_sat(self):
#         self.__yem_sayi = self.__yem_sayi-self.heyvanlar.count("toyuq")
#         self.__pul += self.__yem_sayi*50

#     @staticmethod
#     def sud_sat(self):
#         self.__pul += 200

#     @staticmethod
#     def yun_sat(self):
#         self.__yun += 50


#     qiymetler=[]
#     @staticmethod
#     def heyvanlarin_qiymeti(self):
#         self.inek_qiymeti = 800
#         self.qoyun_qiymeti = 500
#         self.toyuq_qiymeti = 200
#         self.qiymetler = [self.inek_qiymeti,self.qoyun_qiymeti, self.toyuq_qiymeti]
#         return self.qiymetler

#     @property
#     def yem_sayi(self)->float:
#         return self.__yem_sayi

#     @yem_sayi.setter
#     def yem_sayi(self,yem_sayi:int):
#         if yem_sayi<self.yem_sayi:
#             self.__pul+=yem_sayi*15
#         elif yem_sayi>self.yem_sayi:
#             self.__pul+=yem_sayi*25


# soz=input()
# saitler='aeuio'
# hecalar=""
# for i in range(1,len(soz)-2):
#     # if soz[i] in saitler and  not soz[i-1] in saitler and not soz[i+1] in saitler and not soz[i+2] in saitler:
#     #     hecalar+=soz[i-1]+soz[i]+soz[i+1]+"-"
#     # elif soz[i] in saitler and  not soz[i-1] in saitler and not soz[i+1] in saitler and soz[i+2] in saitler:
#     #     hecalar+=soz[i-1]+soz[i]+"-"
#     # elif soz[i] in saitler:
#     #     if soz[i-1] in saitler:
#     #         hecalar+=soz[i]+"-"

#     if soz[i] in saitler:
#         if soz[i+1]


# print(hecalar)


# database class(Iscilerin melumatlari)
# Employee class(Name,age,salary per month,job,hours per week),getEmployeesByName =information,illik maas(),print eliyende melumatlari versin
# Company class add workers(worker),remove workers getHourlySalaryBill,getYearlySalaryBill,average salary,average age,total hours per month,company info cagiranda butun iscileri cixartsin


class Employee:
    def __init__(self, name, age, salary_per_month, job, hours_per_week):
        # self.info_list=[]
        self.name = name
        self.age = age
        self.salary_per_month = salary_per_month
        self.job = job
        self.hours_per_week = hours_per_week
        self.info_list = {"name": self.name, "age": self.age, "salary_per_month": self.salary_per_month,
                          "job": self.job, "hours_per_week": self.hours_per_week}

    def getEmployeeInfo(self):
        return f"Name is {self.name},age is {self.age},salary per month is {self.salary_per_month},job is {self.job},hours per week is {self.hours_per_week}"

    def __str__(self):
        return f"Name is {self.name},age is {self.age},salary per month is {self.salary_per_month},job is {self.job},hours per week is {self.hours_per_week}"
        
    def getHourlySalaryBill(self):
        return self.salary_per_month/(self.hours_per_week*4)
    
    def getYearlySalaryBill(self):
        return self.salary_per_month*12

class Company:
    def __init__(self):
        self.workers_list = []

    def add_worker(self, employee):
        self.workers_list.append(employee.info_list)

    def add_workers(self, *employees):
        for employee in employees:
            self.workers_list.append(employee.info_list)


    def remove_worker(self, employee):
        self.workers_list.remove(employee.info_list)

    def show_workers(self):
        for i in self.workers_list:
            print(i)
            
    def average_salary(self):
        cem=0
        for i in self.workers_list:
            cem+=i['salary_per_month']
        return cem/len(self.workers_list)
    
    def average_age(self):
        cem=0
        for i in self.workers_list:
            cem+=i['age']
        return cem/len(self.workers_list)
        


company1 = Company()
employee1 = Employee("Murad", 18, 4000, "Full stack developer", 20)
employee2 = Employee("Ayxan", 13, 3000, "Backend developer", 10)
employee3 = Employee("Eli", 28, 5000, "Hekim", 30)

company1.add_worker(employee1)
company1.add_worker(employee2)
company1.add_worker(employee3)
company1.remove_worker(employee1)


company1.show_workers()
print(company1.average_salary())
print(company1.average_age())


# print(employee1)

# class Database:
#     def __init__(self):
#         self, name, surname, age, experience):
#         self.name = name
#         self.surname = self.surname
#         self.age = age
#         self.experience = experience
#         self.information = []
#         self.my_dic = {"name": self.name, "surname":self.surname,"age":self.age,"experience":self.experience}
