from django.urls import path, include
from challenges import views

urlpatterns = [
    path('', views.index_list_months, name="index_months"),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name="month_challenge"),
]