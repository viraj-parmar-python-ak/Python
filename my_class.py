class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.email = fname + "." + lname + "@armakuni.com"
        self.salary = salary
    
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    
    def emp_email(self):
        return self.email
    
emp1 = Employee("Viraj", "Parmar", "100000")

print(emp1.fullname())
print(Employee.emp_email(emp1))
