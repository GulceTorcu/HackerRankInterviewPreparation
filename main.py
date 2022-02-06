#!/bin/python3

from HelloWorld import hello_world
from WeirdNumber import weird_number
from ArithmeticOperations import basic_operations, dividing_operations, get_square, print_integers_by_range
from CalendarOperations import is_leap


def main():
    exercise_list = ["Hello World", "Weird Number", "Basic Operations", "Dividing Operations", "Get Square",
                     "Is Leap Year", "Print Numbers"]
    print("This is an easy python program to check the answers for the training questions")
    print("Here are the list of questions")
    for i, val in enumerate(exercise_list):
        print(i, ":", val)
    exercise_chosen = input("Choose the result of the exercise: ")
    if exercise_chosen == '0' or exercise_chosen == 'Hello World':
        hello_world()
    elif exercise_chosen == '1' or exercise_chosen == 'Weird Number':
        weird_number()
    elif exercise_chosen == '2' or exercise_chosen == 'Basic Operations':
        basic_operations()
    elif exercise_chosen == '3' or exercise_chosen == 'Dividing Operations':
        dividing_operations()
    elif exercise_chosen == '4' or exercise_chosen == 'Get Square':
        get_square()
    elif exercise_chosen == '5' or exercise_chosen == 'Is Leap Year':
        print(is_leap())
    elif exercise_chosen == '6' or exercise_chosen == 'Print Numbers':
        print_integers_by_range()


main()
