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


def monthly_challenge(request, month):
    try:
        month_response = month_dict[month]
    except:
        return HttpResponseNotFound('Please insert a valid month.')  # At the moment we are not sending
        # HTML to our web page, just pure plain text. So this code has been copied and pasted to another
        # file, and in there we will make these changes
    return HttpResponse(month_response)


def monthly_challenge_by_number(request, month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("Please insert a valid month.")
    forward_month = months[month - 1]
    forward_path = reverse("month_challenge", args=[forward_month])
    # The reverse function allows us to create paths by referring to the names of the paths, of the URLs.
    # reverse() figures out how to build a full path of the url in urlpatterns inside the challenges/urls.py
    # code
    # Now Python Django will construct a string path that looks like this: # challenge/january
    print(forward_month)
    return HttpResponseRedirect(forward_path)
