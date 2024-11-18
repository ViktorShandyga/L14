class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added to the {self.name} department.")

    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)
                print(f"Employee {employee_name} removed from the {self.name} department.")
                return
        print(f"Employee {employee_name} not found in the {self.name} department.")

    def calculate_total_salary(self):
        return sum(employee.salary for employee in self.employees)

    def list_employees(self):
        print(f"Employees in {self.name} department:")
        for employee in self.employees:
            print(employee)

if __name__ == "__main__":
    # Створення відділу
    it_department = Department("IT")

    emp1 = Employee("Viktor", "Developer", 50000)
    emp2 = Employee("Bob", "Tester", 40000)
    emp3 = Employee("Vova Adidas", "Manager", 100000)

    it_department.add_employee(emp1)
    it_department.add_employee(emp2)
    it_department.add_employee(emp3)

    it_department.list_employees()

    it_department.remove_employee("Bob")

    it_department.list_employees()

    total_salary = it_department.calculate_total_salary()
    print(f"Total salary in {it_department.name} department: {total_salary}")
