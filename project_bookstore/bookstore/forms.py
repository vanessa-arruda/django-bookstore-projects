from django import forms
from bookstore.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password':forms.PasswordInput(),
        }
        fields = '__all__'