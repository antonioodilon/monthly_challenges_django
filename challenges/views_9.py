from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def index_list_months(request):
    list_items = ""
    months = list(month_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    response_data = "<ul>{0}</ul>".format(list_items)
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        month_response = month_dict[month]
        return render(request, "challenges/challenge.html", {
            "text": month_response
        })  # Passing now a third argument, which will now let Django get the values in month_dict,
        # using the month_response variable, and put it in the challenge.html
        # Double curly braces is special Django syntax in challenge.html with 'text' inside is
        # special Django syntax
    except:
        return HttpResponseNotFound('<h1>Please insert a valid month.</h1>')


def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Please insert a valid month.")
    forward_month = months[month - 1]
    forward_path = reverse("month_challenge", args=[forward_month])
    print(forward_month)
    return HttpResponseRedirect(forward_path)