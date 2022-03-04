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

# Sometimes we hear URLs being called Routes. It's the same thing.
# For each URL we have our Views. They Views are the logic that is executed for different URLs
# and Http methods. They can be a Function or a Class. With the Views we handle the incoming
# request and return a response.


# Now we want to return a list of months, and each item in that list should be a clickable link:
def index_list_months(request):
    list_items = ""
    months = list(month_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"  #<li> creates a link
        # Apprending the string list_items with each month. Remember that we are also creating a 
        # list in html with <li></li>, which obviously is different from a Python list
        # <a href='{month_path}'> is the path that Django will use
    response_data = "<ul>{0}</ul>".format(list_items)
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        month_response = month_dict[month]
        response_data = "<h1>{0}</h1>".format(month_response)
        return HttpResponse(response_data)
        # return HttpResponse(month_response)  # Now instead of returning plain text, we will return
        # html
    except:
        return HttpResponseNotFound('<h1>Please insert a valid month.</h1>')


def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Please insert a valid month.")
    forward_month = months[month - 1]
    forward_path = reverse("month_challenge", args=[forward_month])  # reverse() allows us to build
    # URLs dynamically, without hard-coding them. We identify them by name ("month_challenge") in this
    # case. And then we can use it however we want, for redirecting or for generating a link, such as
    # a code in month_path = reverse("month_challenge", args=[month]) in the index_list_months function
    print(forward_month)
    return HttpResponseRedirect(forward_path)