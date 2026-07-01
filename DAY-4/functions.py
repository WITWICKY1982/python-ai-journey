def greet(name):
    print("GOOD MORNING",name)
greet("DHRUV")

def emp_details(salary,gender):
    print("EMPLOYEE SALARY IS ",salary)
    print("EMPLOYEE GENDER IS",gender)
emp_details(1000,"MALE")

def nat(**new):
    for key, value in new.items():
        print(f"{key},"==",{value}")

nat(BMW=10,AUDI = 100)

def car_details(**details):
    for key, value in details.items():
        print(f"{key} == {value}")
car_details(MODEL = "BMW",YEAR = 2012,ENGINE = "PETROl")
