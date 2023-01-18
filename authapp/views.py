from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView
from . forms import CostomUserCreationForm , CostomUserChangeForm

from . models import CostomUser

# Create your views here.

class SignUpView(CreateView):
    form_class = CostomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

class ChangeView(UpdateView):
    form_class = CostomUserChangeForm
    template_name = "registration/change_personal_data.html"
    success_url = reverse_lazy('settings')

    def get_object(self, queryset=None):
        return self.request.user


def SettingsView(request):
    id = request.user.id
    user = CostomUser.objects.get(id=id)
    context = {
        'user': user
    }

    return render(request, 'settings.html', context)