from django.urls import path
from .views import RegisterView

urlpatterns = [
    path('new_user/', RegisterView.as_view())#.as_view())
]