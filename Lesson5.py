# to ceate a class
class Person():
    country = 'USA'
    def __init__(self, fname, lname):
        # dynamic fields
        self.fname = fname
        self.lname = lname
        # static fields
        # color = 'Bff53'

    def hello(self):
        return f'{self.fname} says hello'

    def learn(self):
        return f'I\'m learning'

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country
        return(cls.country)

# creating a subclass
class Programmer(Person):
    def __init__(self, fname, lname, language, job_title, salary):
        # to inherit the methods
        super().__init__(fname, lname)
        # public attribute
        self.language = language
        # protected attribute
        self._job_title = job_title
        # to make attribute private
        self.__salary = salary
    def coding(self):
        return f'I am coding with {self.language}'
    # to call a private attribute you need to put it into a method
    def get_salary(self):
        return self.__salary

    # to reassign the value
    def set_salary(self, new_salary):
        self.__salary = new_salary

    def learn(self):
        return f'I\'m learning coding'

class Junior(Programmer):
    def __init__(self, fname, lname, language, job_title, salary, age):
        super().__init__(fname, lname, language, job_title, salary)
        self.age = age

class Tester(Person):
    def __init__(self, fname, lname, framework, job_title):
        # to inherit the methods
        super().__init__(fname, lname)
        self.framework = framework
        self.job_title = job_title
    def testing(self):
        return f'I\'m testing with {self.framework}'
    def learn(self):
        return f'I\'m learning testing'

person_1 = Person('Alex', 'Baker')
print(person_1.learn())
# print(person_1.lname)
# print(person_1.hello())
# print(person_1.country)
# person_1.fname = 'Alexander'
# print(person_1.fname)
# print(person_1.__dict__)

#
# person_2 = Person('Kevin', 'Smith')
# print(person_2.lname)
# print(person_2.__dict__)
# print(person_2.hello())
#
coder_1 = Programmer('Jack', 'Beker', 'JavaScript', 'Software Engineer', 100000)
# print(coder_1.lname)
# print(coder_1.language)
# print(coder_1.hello())
# print(coder_1.coding())
# print(coder_1.get_salary())
# # with private methods we cannot reassign the value
# coder_1.__salary = 200000
# print(coder_1.get_salary())
# # reassigning the value using a different method
# coder_1.set_salary(200000)
# print(coder_1.get_salary())
# # to get the value of the private attribute
# print(coder_1._Programmer__salary)
# # to get the value of the protected attribute
# print(coder_1._job_title)
print(coder_1.learn())

#
tester_1 = Tester('Josh', 'Bekerson', 'PyTest', 'Software QA Engineer')
# print(tester_1.lname)
# print(tester_1.job_title)
# print(tester_1.hello())
# print(tester_1.testing())
print(tester_1.learn())
tester_1.change_country('Canada')
print(tester_1.country)

