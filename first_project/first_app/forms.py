from django import forms
from .models import EmpDetails




class EmpDetailsForm(forms.ModelForm):
    class Meta:
        model = EmpDetails
        fields = ['emp_name', 'emp_city', 'emp_company']






#
# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=100,label="Your name")
#     email=forms.EmailField(label="Your Email")
#     message=forms.CharField(widget=forms.Textarea, label="Your message")
#
# class ContactForm(forms.Form):
#     OPTIONS=[("option1","sachin"),
#              ("option2","virat"),
#              ("option3","mahi")]
#     name=forms.CharField(max_length=100,
#                         widget=forms.TextInput(attrs={'placeholder':'Enter your name','class': 'form-control'}),
#                          label="Your name")
#     email=forms.EmailField(label="Your Email",
#                            widget=forms.TextInput(attrs={'placeholder':'Enter your Email','class': 'form-control'}))
#     message=forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40, 'placeholder': 'Enter your feedback'}),
#                             label="Your message")
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-field'}),
#         label="Password")
#
#     subscribe = forms.BooleanField(
#             widget=forms.CheckboxInput(),
#             label="Subscribe to newsletter",
#             required=False
#         )
#     choice =forms.ChoiceField(choices= OPTIONS,
#                               widget=forms.Select(attrs={'class': 'form-select'}),
#                               label="Select one options")

class RegistrationForm(forms.Form):
    username= forms.CharField(max_length=150)
    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username.lower() == 'admin':
            raise forms.ValidationError("Name 'admin' is not allowed.")
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(" Password is not matched ")


