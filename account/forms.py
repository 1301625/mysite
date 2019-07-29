from django import forms
from account.models import Account

from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm


class AccountCreateForm(forms.ModelForm):
    email = forms.EmailField(label="Email", max_length=255,
                             help_text="A valid email address",
                             error_messages={
                                 'invalid': "This form is not a email address"})

    username = forms.RegexField(label='Username', max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters, digits and "
                                          "./+/-/_ only.",
                                error_messages={
                                    'invalid': "This value may contain only letters, number and "
                                               "@/./+/- characters"
                                })

    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'username')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Account._default_manager.get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError("A user with that username already exists")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AccountChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    email = forms.EmailField(label="Email", max_length=255,
                             help_text="A valid email address",
                             error_messages={
                                 'invalid': "This form is not a email address"})

    username = forms.RegexField(label='Username', max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required. 30 characters or fewer. Letters, digits and "
                                          "./+/-/_ only.",
                                error_messages={
                                    'invalid': "This value may contain only letters, number and "
                                               "@/./+/- characters"
                                })

    password = ReadOnlyPasswordHashField(label='password',
                                         help_text="Raw passwords are not stored, so there is no way to see "
                                                   "this user's password, but you can change the password "
                                                   "using <a href=\"password/\">this form</a>.")

    class Meta:
        model = Account
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):


    email = forms.EmailField(label="Email",required=True, max_length=255, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ('Email address'),
            'required': True,
            'autofocus': True,
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'required': True,
        }
    )
    )

    class Meta:
        fields = ['email', 'password']