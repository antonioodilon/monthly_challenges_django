from django.urls import path, include
from challenges import views

urlpatterns = [
    path('january', views.january),  # If a request hits /january, execute the views.view_index method
    path('february', views.february),
    path('march', views.march),
    path('<month>', views.monthly_challenge)  # Instead of typing each month, we can add a placeholder, to make everything more dynamic.
    # Django has a built-in placeholder, which is <>
]
# The method path() accepts two arguments: one is a string with the url we want. For example, in our website
# it would be challenges/january. The second argument is the function in views.py