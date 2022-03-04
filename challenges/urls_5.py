from django.urls import path, include
from challenges import views

urlpatterns = [
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name="month_challenge"),  # By adding name="month_challenge", 
    # we can then make our app more versatile. In urls.py, if we change path("challenges/" to path("challenge/"
    # (without an S), then we'll have no errors
]