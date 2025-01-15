from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


# Common CSS class for input fields
html_class = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'

class CreateForm(UserCreationForm):

    

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2','role','photo']  

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': html_class, 'placeholder': 'First Name'})  
        self.fields['last_name'].widget.attrs.update({'class': html_class, 'placeholder': 'Last Name'})
        self.fields['username'].widget.attrs.update({'class': html_class, 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': html_class, 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': html_class, 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': html_class, 'placeholder': 'Confirm Password'})
        self.fields['role'].initial = 'Patient'
    

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password'])
    #     if commit:
    #         user.save()
    #         CreateForm.objects.create(
    #             user=user,
    #             role=self.cleaned_data['role'],
    #             photo=self.cleaned_data.get('photo')
    #         )
    #     return user

