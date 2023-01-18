from django.urls import path
from . views import SignUpView, ChangeView , SettingsView

urlpatterns = [
    path("signup/",SignUpView.as_view(), name='signup'),
    path("change/",ChangeView.as_view(), name='change_pD'),
    path('settings/',SettingsView, name='settings')

]