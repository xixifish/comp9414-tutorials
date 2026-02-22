import string
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Write a Python program that finds all the prime numbers
# between 1 and 1000 (inclusive) and stores them in a list.
def loops_3_1():
    prime_numbers = []
    for i in range(2, 1001):
        is_prime = True

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
    return prime_numbers


# Write a Python program that counts the number of digits of
# a natural number n, i.e., n is a positive, integer number
def while_3_1(n):
    number_digits = 0
    while n != 0:
        number_digits += 1
        n //= 10  # // divides and keeps only the integer part
    return number_digits


# Write a Python program that takes a user's age as input
# and determine the ticket price for a theme park based on the
# following critieria:
# Children aged 3 and below enter for free
# Children aged 4 to 10 pay $10
# Adults aged 11 to 17 pay $15
# Adults aged 18 to 59 pay $20
# Seniors aged 60 and above pay $12
# The problem should also consider whether the user has a membership.
# If a user has a membership, they receive a 20% discount on the ticket
# price.
def if_3_2(age, has_membership):
    ticket_price = 0
    if age <= 3:
        ticket_price = 0
    elif age <= 10:
        ticket_price = 10
    elif age <= 17:
        ticket_price = 15
    elif age <= 59:
        ticket_price = 20
    else:
        ticket_price = 12

    if has_membership:
        ticket_price *= 0.8

    return ticket_price


# Write a Python program that checks if a given string is a palindrome
# or not.(3.3.2)
def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    translator = str.maketrans("", "", string.punctuation)
    result_text = cleaned_text.translate(translator)
    return result_text == result_text[::-1]


# Consider a simple banking system. Write a Python program that models a
# Bank Account class. The BankAccount class should have the following
# functionalities:
# - Initialize the account with an account number and an initial balance
# - Allow deposits and withdrawals
# - Display the current balance
# What are the other features that we can add to the bank account class?


class BankAccount:
    def __init__(self, account_number, balance):
        """Initialize account number and balance"""
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Allow deposit"""
        self.balance += amount

    def withdrawal(self, amount):
        """Allow withdrawal"""
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Current balance: ${self.balance}")

    def __str__(self):
        return f"Account {self.account_number}: Balance ${self.balance}"


# Consider a library management system. Write a Python program that models
# the following entities: Library, Book, and Memeber
# The Library class should have the following functionalities:
# - Keep track of a collection of Book objects
# - Allow memebers to borrow if they are available
# - Keep a record of borrowed books and their due dates (members can borrow
# a book for 14 days)
# - Allow memebers to return books.
# The Book class should have the following attributes:
# - Title.
# - Author.
# - Availability status.
# The Member class should have the following attributes:
# - Full name.
# - Member ID.
class Book:
    def __init__(self, title, author):
        """Initialize book object"""
        self.title = title
        self.author = author
        self.status = True  # True = available
        self.borrow_time = None
        self.due_time = None
        self.borrower = None


class Member:
    def __init__(self, name, member_id):
        """Initialize member"""
        self.name = name
        self.id = member_id


class Library:
    def __init__(self, books, members):
        """Initialize collection of books and memebers"""
        self.books = books
        self.members = members

    def borrow_book(self, book, member):
        if book.status:
            self.books.book.status = False
            book.borrow_time = datetime.now()
            book.due_time = book.borrow_time + timedelta(days=14)
            book.borrower = member
        else:
            print("The book is not available now.")

    def return_book(self, book):
        book.status = True
        book.borrow_time = None
        book.due_time = None
        book.borrower = None


# Write a Python program that generates a random matrix of size NxN,
# where N is a use-specified positive integer. The program should then
# find the sum of each row and each coloum of the matix using the numpy
# library.
def random_matrix(n):
    if n <= 0 or not isinstance(n, int):
        return "n should be a positive integer."

    # Create a random matrix
    matrix = np.random.randint(0, 10, (n, n))
    row_sums = np.sum(matrix, axis=1)
    column_sums = np.sum(matrix, axis=0)

    return row_sums, column_sums


# Consider a dataset containing the performance metrics (accuracy, precision,
# recall) of multiple machine learning models on a classcification task given
# to you. Write a Python program that performs the following tasks:
# - Calculate the mean and standard deviation of each metric across all models
# - Visualize the mean performance of each metric using a bar chart, with the
# x-axis representing the metrics and the y-axis representing the mean values
# - PLot error bars on the bar chart to represent the standard deviation of
# each metric
# - Compare the performance of each model on a specific metric using a line plot,
# with the x-axis representing the models and the y-axis representing the metric
# value
data = {
    "Model": ["Model A", "Model B", "Model C", "Model D", "Model E"],
    "Accuracy": [0.91, 0.88, 0.95, 0.89, 0.92],
    "Precision": [0.87, 0.85, 0.90, 0.88, 0.91],
    "Recall": [0.90, 0.84, 0.93, 0.86, 0.89],
}
df = pd.DataFrame(data)


def matplotlib_5_1(df):

    models = df["Model"]
    metrics = ["Accuracy", "Precision", "Recall"]
    means = [df[m].mean() for m in metrics]
    stds = [df[m].std() for m in metrics]

    # First figure
    plt.figure(1)
    plt.bar(metrics, means, yerr=stds, capsize=5)
    plt.xlabel("Metrics")
    plt.ylabel("Means")
    plt.title("Bar Plot - Mean of Metrics")
    plt.show()

    # Second figure
    plt.figure(2)
    for metric in metrics:
        plt.plot(models, df[metric], marker="o", label=metric)
    plt.xlabel("Model")
    plt.ylabel(f"{metrics}")
    plt.title(f"Model Comparison - {metrics}")
    plt.xticks(rotation=45, ha="right")  # rotate labels if model names too long
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Test loops - prime numbers
    primes = loops_3_1()
    print(f"Prime numbers (first 10): {primes[:10]}...")

    # Test while loop - digit counter
    print(f"Digits in 12345: {while_3_1(12345)}")

    # Test if statement - ticket price
    print(f"Ticket price (age 25, member): ${if_3_2(25, True)}")

    # Test palindrome
    print(
        f"'A man a plan a canal Panama' is palindrome: {is_palindrome('A man a plan a canal Panama')}"
    )

    # Test BankAccount
    account = BankAccount("123456", 1000)
    account.deposit(500)
    account.withdrawal(200)
    account.display_balance()

    # Test random matrix
    row_sums, col_sums = random_matrix(3)
    print(f"Row sums: {row_sums}, Column sums: {col_sums}")

    # Test matplotlib visualization
    matplotlib_5_1(df)
