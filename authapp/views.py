from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from . forms import CostomUserCreationForm

# Create your views here.

class SignUpView(CreateView):
    form_class = CostomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


