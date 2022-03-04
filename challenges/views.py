from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

month_dict = {
    'january': 'Eat more meat, eggs and vegetables!',
    'february': 'Lift weights at least 4 times a week for 40 minutes!',
    'march': 'Learn Python Django for at least one hour every day!',
    'april': 'Eat less processed food!',
    'may': 'Learn MongoDB for at least two hours everyday!',
    'june': 'Lift weights at least 4 times a week for 1 hour!',
    'july': 'Tell your spouse everyday that you love her/him while looking into her/his eyes!',
    'august': 'Make a special dinner for your spouse and children 2 times a week!',
    'september': None,
    'october': 'Teach your children how to program for 30 minutes 4 times a week!',
    'november': 'Eat only healthy food with your family for the entire month!',
    'december': None,
}


def index_list_months(request):
    # list_items = ""
    months = list(month_dict.keys())

    return render(request, "challenges/index_template.html", {
        "months": months,
        })


def monthly_challenge(request, month):
    try:
        month_challenge_response = month_dict[month]
        return render(request, "challenges/challenge_template.html", {
            "text_challenge": month_challenge_response,
            "text_month": month,
        })
    except:
        raise Http404()  # We NEED to name our 404 templates file as 404.html
        # response_data = render_to_string("404.html")
        # return response_data
        

def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())
    if month > len(months):
        response_data = render_to_string("404.html")
        return response_data
    forward_month = months[month - 1]
    forward_path = reverse("month_challenge", args=[forward_month])
    print(forward_month)
    return HttpResponseRedirect(forward_path)