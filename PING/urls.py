from django.urls import path
from . import views
from .views import DomainCreateView

urlpatterns = [
    path('add-domain/', DomainCreateView.as_view(), name='add_domain')

]