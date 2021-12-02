"""
Name: Brianna Joyner
sales_force.py

Problem: This program creates the SalesForce class.

Certification of Authenticity:
I certify that this assignment is entirely my own work, with help from the CSL and Angela.
"""
from sales_person import SalesPerson

class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        lines = infile.readlines()
        for i in range(len(lines)):
            data = lines[i].split(",")
            person = SalesPerson(eval(data[0]), data[1])
            sale = data[2].split()
            for i in range(len(sale)):
                person.enter_sale(sale[i])
            self.sales_people.append(person)

    def quota_report(self, quota):
        report = []
        for i in range(len(self.sales_people)):
            report.append(
                [self.sales_people[i].get_id(), self.sales_people[i].get_name(), self.sales_people[i].total_sale(),
                 self.sales_people[i].total_sale() > quota])
        return report

    def top_seller(self):
        top_seller = self.sales_people[0]
        seller_list = []
        for i in range(1, len(self.sales_people), -1):
            if self.sales_people[i].compare_to(top_seller) < 0:
                top_seller = self.sales_people[i]
                seller_list = []
            elif self.sales_people[i].compare_to(top_seller) == 0:
                seller_list.append(self.sales_people[i])
        seller_list.append(top_seller)
        return seller_list

    def individual_sales(self, employee_id):
        for i in range(len(self.sales_people)):
            if self.sales_people[i].get_id() == employee_id:
                return self.sales_people[i]
        return None

def main(): # to test the class
    target_sale = SalesForce()
    target_sale.add_data("salesData.txt")
    print(target_sale.quota_report(600))
    print(target_sale.top_seller())
    print(target_sale.individual_sales(498))

if __name__ == '__main__':
    main()
