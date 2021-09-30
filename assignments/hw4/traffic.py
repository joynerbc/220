"""
Name: Brianna Joyner
traffic.py

Problem: This program will analyze traffic patterns.

Certification of Authenticity:
I certify that this assignment is entirely my own work, with help from the CSL.
"""
import math

def main():
    total_vehicle_num = 0
    num_roads = eval(input("Enter the number of roads surveyed: "))
    for _ in range(num_roads):
        num_days = eval(input("Enter the number of days the road was surveyed: "))
        total_cars = 0
        for _ in range(num_days):
            num_cars = eval(input("Enter the number of cars traveled: "))
            total_cars = total_cars + num_cars
        avg_cars = total_cars / num_days
        print(round(avg_cars, 1))
        total_vehicle_num = total_vehicle_num + total_cars
    print(total_vehicle_num)
    total_vehicle_avg = total_vehicle_num / num_roads
    print(round(total_vehicle_avg, 2))

if __name__ == '__main__':
    main()
