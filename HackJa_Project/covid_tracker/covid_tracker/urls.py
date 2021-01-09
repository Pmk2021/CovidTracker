from django.urls import path

from . import views
from .forms import NameForm

urlpatterns = [
    path('happy_burger', views.checkin, name='happy_burger'),
    path('happy_burger_checkout', views.checkout, name='happy_burger_checkout'),
    path('submitted', views.submitted, name='submitted'),
    path('', views.homepage, name='home'),
    path('report_case', views.report_case, name='report_case')
]
