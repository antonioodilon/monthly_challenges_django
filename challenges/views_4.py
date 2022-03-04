from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Importing HttpResponseRedirect

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


# Max's solution:
def monthly_challenge(request, month):
    try:
        month_response = month_dict[month]
    except:
        return HttpResponseNotFound('Please insert a valid month.')
    return HttpResponse(month_response)


# My solution 2:
def monthly_challenge_2(request, month):
    month_response = month_dict[month]
    if month_response in month_dict[month]:
        return HttpResponse(month_response)
    else:
        return HttpResponseNotFound('Please insert a valid month.')


# My solution:
def monthly_challenge_3(request, month_input):
    for month, month_text in month_dict.items():
         if month_input == month:
             month_response = month_text
         else:
             return HttpResponseNotFound('Please insert a valid month.')
    return HttpResponse(month_response)


def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())  # A list with all the keys of month_dict
    if month > len(months):  # If month is greater than the length of the list months (12), then
        # return a negative response.
        return HttpResponseNotFound("Please insert a valid month.")
    forward_month = months[month - 1]  # Deduct 1 from month because iterables in Python start at
    # index 0.
    print(forward_month)  # forward_month is the index of the given month in months
    return HttpResponseRedirect("/challenges/" + forward_month) # /challenges/ refers probably to
    # urls.py in the challenges app
    # For some reason Django recognizes the values related to the keys in the dictionary without
    #  us needing to iterate through the items and values here.



