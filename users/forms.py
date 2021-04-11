from django.contrib.auth.forms import UserCreationForm

from .models import Users

class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Users
        fields = ("first_name", "last_name", "username", "email")
