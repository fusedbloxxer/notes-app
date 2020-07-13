from registration import views as registration
from django.urls import path, include

app_name = 'registration'

urlpatterns = [
    path('signup/', registration.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
