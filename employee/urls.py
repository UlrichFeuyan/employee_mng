from django.urls import path
from employee.views import list_employee


app_name="employee"
urlpatterns = [
    path('', list_employee),
]
