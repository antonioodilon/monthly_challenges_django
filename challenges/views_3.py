from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
month_dict = {
    'january': 'Eat more meat, eggs and vegetables!',
    'february': 'Lift weights at least 4 times a week for 40 minutes!',
    'march': 'Learn Python Django for at least one hour every day!',
    'april': 'Eat less processed food!',
    'may': 'Learn MongoDB for at least two hours everyday!',
    'june': 'Lift weights at least 4 times a week for 1 hour!',
    'july': 'Tell your spouse everyday that you love her/him while looking into her/his eyes!',
    'august': 'Make a special dinner for your spouse and children 2 times a week!',
    'september': 'Talk to and play with your children everyday for at least 40 minutes!',
    'october': 'Teach your children how to program for 30 minutes 4 times a week!',
    'november': 'Eat only meat and eggs with your family for the entire month!',
    'december': 'Exercise with your children 4 times a week for 30 minutes!',
}


def monthly_challenge(request, month_input):  # We put month as the second argument because that is what we
    # named as the first argument for path() in urls.py
    # for month in month_dict.keys():  # Junk code!
    #     if month_input in month:
    #         month_response = month_text
    for month, month_text in month_dict.items():
         if month_input == month:
             month_response = month_text
         else:
             return HttpResponseNotFound('Please insert a valid month.')
    return HttpResponse(month_response)
    

# This is the solution Max came up with for the moment, but it needs to be improved, and it probably 
# will.
def monthly_challenge_2(request, month):
    if month == 'january':
        month_response = 'Eat more meat, eggs and vegetables.'
    elif month == 'february':
        month_response = 'Lift weights at least 4 times a week for 40 minutes.'
    elif month == 'march':
        month_response = 'Learn Python Django for one hour every day.'
    else:
        return HttpResponseNotFound('This month is not supported')
    return HttpResponse(month_response)


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)