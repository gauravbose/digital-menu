from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm 

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

#class UserCreateForm(UserCreationForm):
 #   email = forms.EmailField(required=True)
    #password1 = forms.CharField(label=_("Password"),
     #   widget=forms.PasswordInput)
    #password2 = forms.CharField(label=_("Password confirmation"),
     #   widget=forms.PasswordInput,
      #  help_text=_("Enter the same password as above, for verification."))

  #  class Meta:
   #     model = User
    #    fields = ("username", "email", "password1", "password2")

#    def save(self, commit=True):
#        user = super(UserCreateForm, self).save(commit=False)
#        user.email = self.cleaned_data["email"]
       # user.set_password(self.cleaned_data["password1"])
#        if commit:
#            user.save()
#        return user


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
