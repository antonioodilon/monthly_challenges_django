from django.urls import path, include
from challenges import views

urlpatterns = [
    path('', views.index_list_months),  # This will direct to the main screen, /challenges/
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name="month_challenge"),  # By adding name="month_challenge", 
    # we can then make our app more versatile. In urls.py, if we change path("challenges/" to path("challenge/"
    # (without an S), then we'll have no errors
]

"""
from django.urls import path, include
from challenges import views

urlpatterns = [
    path('', views.index_list_months, name="index_months"),  # We referenced it in shared_header_template, with
    # url "index_months" (the name of this path)
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name="month_challenge"),  # By adding name="month_challenge", 
    # we can then make our app more versatile. In urls.py, if we change path("challenges/" to path("challenge/"
    # (without an S), then we'll have no errors
"""