from django.urls import path, include
from challenges import views

urlpatterns = [
    # The order matters. We first want to check for an int; otherwise, check for a string
    path('<int:month>', views.monthly_challenge_by_number),  # If month is a number, we'll handle as an int
    path('<str:month>', views.monthly_challenge),  # If the month is a string, we'll handle the string
]