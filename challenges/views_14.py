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
    'september': None,  # Changing this key's value to None so we can see what happens in challenge.html
    # with the if statement
    'october': 'Teach your children how to program for 30 minutes 4 times a week!',
    'november': 'Eat only meat and eggs with your family for the entire month!',
    'december': None,
}


def index_list_months(request):
    # list_items = ""
    months = list(month_dict.keys())

    return render(request, "challenges/index_template.html", {
        # Passing the list of month names that we generated through the template
        "months": months,  # This is a dictionary. The name "months" and the months variable have
        # to be the same
        })
        # Take a look for month in months is in our index_template.html
        # code

        # We are working with DTL here in the index_template.html. Much of what we see there is
        # DLT syntax. DLT = Django template language
        # https://docs.djangoproject.com/en/4.0/ref/templates/language/

        # Very important! In pure Python we use indentation to determine where an if statement or
        # for loop starts and ends.
        # Take a look at index_template.html. In body -> ul we are using {%%} to determine where they
        # start and where they end.

        # Be sure to take a look at urls.py to check out our urls. It's what {% url month_challenge month=month %}
        # is doing in index_template.html . month=month means that the first month variable is <str:month>
        # in urls.py , and the second month variable is month in {% for month in months%} in index_template.html

        # {% url 'month_challenge' month=month %} that is inside the for loop in index_template.html doesn't
        # need a closing tag {% endfor %}

"""
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month_challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    response_data = "<ul>{0}</ul>".format(list_items)
    return HttpResponse(response_data)
"""


def monthly_challenge(request, month):
    try:
        month_challenge_response = month_dict[month]
        return render(request, "challenges/challenge_template.html", {
            "text_challenge": month_challenge_response,
            "text_month": month,
        })
    except:
        return HttpResponseNotFound('<h1>Please insert a valid month.</h1>')


def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Please insert a valid month.</h1>")
    forward_month = months[month - 1]
    forward_path = reverse("month_challenge", args=[forward_month])
    print(forward_month)
    return HttpResponseRedirect(forward_path)