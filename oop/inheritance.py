from typing import Any


class Employee:
    co_salary = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_co_salary(self):
        self.pay = int(self.pay * self.co_salary)
        return self.pay
    
    def __repr__(self):
        return f"Employee {self.first},{self.last},{self.pay}"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
    
class Developer(Employee):
    co_salary = 1.02
    def __init__(self, first, last, pay, program_lang):
        super().__init__(first, last, pay)
        self.program_lang = program_lang

class Manager(Employee):
    co_salary = 1.5
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employeess = []
        else: self.employeess = employees
    def add_employee(self, emp):
        if emp not in self.employeess:
            self.employeess.append(emp)
    def remove_employee(self, emp):
        self.employeess.remove(emp)
    def print_employee(self):
        for emp in self.employeess:
            print("==>>", emp.fullname())

class Secretary(Employee):
    co_salary = 1.05
    def __init__(self, first, last, pay, job):
        super().__init__(first, last, pay)
        self.job = job

emp1 = Employee("Mac","Luu", 100)
# print(repr(emp1))
# print(str(emp1))
emp2 = Employee("sdfs","ssa", 231)
#print(emp1 + emp2)
print(len(emp1))
print(emp2.__len__())
# import datetime
# today = datetime.datetime.now()
# print(repr(today))
# print(str(today))

dev1 = Developer("A", "B", 300, "Python")
dev2 = Developer("B", "C", 300, "Python")
man1 = Manager("C", "D", 500, [dev1, dev2])
sec1 = Secretary("sfsf","sdfsf", 1000, "an")


