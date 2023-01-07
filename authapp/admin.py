from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . models import CostomUser
from . forms import CostomUserChangeForm, CostomUserCreationForm

# Register your models here.

class CostomUserAdmin(UserAdmin):
    add_form = CostomUserCreationForm
    form = CostomUserChangeForm
    model = CostomUser
    list_display = ["email","username","first_name","last_name","age","is_staff","is_superuser"]
    fieldsets = UserAdmin.fieldsets + (
        (None,{"fields": ("age",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{"fields": ("age",)})
    )

admin.site.register(CostomUser, CostomUserAdmin)