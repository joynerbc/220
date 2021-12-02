"""
Name: Brianna Joyner
sales_person.py

Problem: This program creates the SalesPerson class.

Certification of Authenticity:
I certify that this assignment is entirely my own work, with help from the CSL and Angela.
"""

class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        acc = 0
        for num in self.sales:
            acc = acc + float(num)
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True
        return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        elif self.total_sales() > other.total_sales():
            return 1
        else:
            return 0

    def __str__(self):
        return str(self.employee_id) + "-" + self.name + ":" + str(self.total_sales())

    def __repr__(self):
        return str(self.employee_id) + "-" + self.name + ":" + str(self.total_sales())

def main(): # to test the class
    first_person = SalesPerson(498, "John Doe")
    print(first_person.get_id())
    print(first_person.get_id())
    first_person.set_name("Park Jimin")
    print(first_person.get_name())
    sale = 75.0
    first_person.enter_sale(sale)
    print(first_person.total_sales())
    print(first_person.get_sales())
    print(first_person.met_quota(100.0))
    print(first_person.met_quota(5.0))
    second_person = SalesPerson(953, "Jane Doe")
    second_person.enter_sale(200.0)
    second_person.enter_sale(15.0)
    print(second_person.get_sales())
    print(second_person.total_sales())
    print(first_person.compare_to(second_person))
    print(second_person.compare_to(first_person))

if __name__ == '__main__':
    main()
