from django.shortcuts import render, redirect

from . import forms

# Create your views here.
from django.views import View

from . import forms
from .forms import DomainForm
from .models import Domain


class DomainCreateView(View):
    def get(self, request, *args, **kwargs):

        form = DomainForm()
        domains = Domain.objects.all()
        return render(request, 'domain_form.html', {'form': form, 'domains': domains})

    def post(self, request, *args, **kwargs):

        form = DomainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_domain')
        domains = Domain.objects.all()
        return render(request, 'domain_form.html', {'form': form, 'domains': domains})
