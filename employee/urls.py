from django.urls import path
from employee.views import add_employee, list_employee


app_name="employee"
urlpatterns = [
    path("", list_employee, name="list_employee"),
    path("add/", add_employee, name="add_employee"),
]
