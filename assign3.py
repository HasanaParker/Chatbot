"""
Hasana Parker
CS51A Assignment 3
February 7th, 2022
"""
import random

from assign3_quotes import *
from random import *


# ____________________________________________________________________
# Movie Quotes Analysis Section


# 1
def is_question(quote):
    """
    This function takes a string as a input and returns to you whether the inputted string is a question or not.
    :param quote: A specific quote that is inputted into the function and determined whether to be a question or not.
    :return: True or False
    """

    return quote[-1] == "?"


# 2
def get_first_quotes(list_of_tuples):
    """
    This function can take any list of tuples and put all the first values of the tuples in a list.
    :param: list_of_tuples insert any list of tuples.
    :return: the first value of each tuple in a list.
    """
    my_list_of_first_quotes = []
    for first_quote, second_quote in list_of_tuples:
        my_list_of_first_quotes. append(first_quote)  # have to append the values of the first_quote to my empty list
    return my_list_of_first_quotes


# 3
def get_first_questions(list_of_tuples):
    """
    This function scans through the list of tuples and add to a list the first value that is a question.
    :param: list_of_tuples inserts any list of tuples.
    :return: the value of each first question in a tuple.
    """
    list_of_first_quote_questions = []
    for first_quote, second_quote in list_of_tuples:
        if is_question(first_quote):  # if the boolean returns true, than the first quote will be appended to a list.
            list_of_first_quote_questions.append(first_quote)
    return list_of_first_quote_questions


# 4
def count_question_quotes(list_of_tuples):
    """
    This function works to count the total number of questions. Each first tuple
    :param list_of_tuples: any list of tuples
    :return: the total number of questions in the list of tuples, the number of first quotes that are tuples.
    """
    question_count = get_first_questions(list_of_tuples)
    return len(question_count)  # only need the length of the question_count list


# 5
def get_average_question_length(list_of_tuples):
    """
    This function works to get the length of each character of a question and divide this length by the total number
    of first quote questions to solve for the average.
    :param list_of_tuples: any list of tuples can be set as a parameter for the code.
    :return: the return value will be a float that is the average length of each first quote question.
    """
    summation = 0 # setting summation to 0, in order to have a starting value for the summation to occur.

    for quest_quote in get_first_questions(list_of_tuples):
        summation += len(quest_quote)   # To sum the list of each letter in the list.
    return summation / len(get_first_questions(list_of_tuples)) # taking the average here.


# make a for loop to go through each and add them together.
# collect all first quotes that are questions.
# sum all the characters in all the quotes that are questions. Add all the characters
# divide the total sum of characters by the number of quotes that are questions?

# ____________________________________________________________________
# Chatbot Section


# 6
def get_responses(list_of_tuples, question):
    """
    This function is working to first check if the first quote is a question and then to append all the second quotes
    with the same first quote question to an empty list.
    :param list_of_tuples: Any list of tuples.
    :param question: This parameter is a question from the list of tuples we are using.
    :return: will return a list of all the second responses, corresponding to a certain question that is a first quote.
    """
    responses = []
    for first_quote, second_quote in list_of_tuples:
        if first_quote == question:  # if the question asked by the user is the same as a first quote quest in the data
            responses.append(second_quote)

    return responses


# 7
# test list number = [1, 2, 3, 4, 5]


def get_random_from_list(my_list):
    """
    This code is working to return a random index from any list.
    :param my_list: can be any list
    :return: Will be returned the value of a random index in the list.
    """
    return my_list[randint(0, len(my_list)-1)] # choosing a random index, from the length of the list.

# -1 at the end because the index starts at 0


# 8
def respond(list_of_tuples, question):
    """
    This function is working to get a random response from the list of tuples, and to return I don't know if there are
    noe responses in the data for the question asked.

    :param list_of_tuples: Any list of tuples
    :param question: any question an be inputed from the data list.
    :return: is a print statement returning, "I don't know".
    """
    responses = get_responses(list_of_tuples, question)
    if responses == []: # if there is no response present for the question asked by the user, return I don't know
        return print("I don't know")
    else:
        return get_random_from_list(responses)

# Not getting anything, do I have to return a value. Yes!


# 9
def chatbot():
    """
    This function is the final chatbot working to respond to questions coresponding to the data set that a user may
    input.
    :return: no return statement for this function
    """
    print(" Welcome! Ask me anything. When you're done, just type 'bye'")
    user_input = input()
    while user_input != "bye": # using a while loop, so that the loop continues until the user inputs bye.
        if not is_question(user_input): # if the question asked is not a question.
            print("I only respond to question")
        else:
            print(respond(get_quotes(), user_input))  # calling the respond function here.
        user_input = input() # checking at the end of the loop to make sure the user didn't input bye.
