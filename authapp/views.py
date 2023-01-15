from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from . forms import CostomUserCreationForm

from . models import CostomUser

# Create your views here.

class SignUpView(CreateView):
    form_class = CostomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


def SettingsView(request):
    id = request.user.id
    user = CostomUser.objects.get(id=id)
    context = {
        'user': user
    }

    return render(request, 'settings.html', context)