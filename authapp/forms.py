from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CostomUser

class CostomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CostomUser
        fields = ["username", "email", "first_name", "last_name", "age"]

class CostomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CostomUser
        fields = ["email", "first_name", "last_name", "age"]