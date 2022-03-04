from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string

# This render_to_string function converts something to a string. We will need it in order
# to convert the html contents of challenge.html (in challenges\templates\challenges folder)
# to a string so that it can be processed by our monthly_challenge function

# If we go to out settings.py file in django_project_monthly_challenges, there we can tell Django
# it should consider other paths as templates. Because at the moment our challenge.html is not being
# considered by Django, and this is why in monthly_challenge we are getting the HttpResponseNotFound
# ('<h1>Please insert a valid month.</h1>') response.

# The settings.py file tells us how to build directories that will be considered by Django. Check out
# the BASE_DIR constant/variable.
# Go to the TEMPLATES constant/variable of the type list in the file add: BASE_DIR / "challenges" / "templates"
# so that Django recognizes this path as one of the paths that should be considered.
# DON'T DELETE ANYTHING!
# Since Django is looking for templates, we NEED to build a folder with this name in our app.

# To make Django fully aware of our app, we need to go to settings.py, and put it inside INSTALLED_APPS.
# Notice that in apps.py the name of our app is set to 'challenges'

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
        return render(request, "challenges/challenge.html")  # This does the same as render_to_string
        # The difference is that it NEEDS the request variable, so that it can then extract data from
        # there
        
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
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