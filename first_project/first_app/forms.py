from django import  forms
from django.contrib.auth.models import User
from django.core import validators
from first_app.models import Userprofileinfo

class formname(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter Email again')
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError('gotabot')
    #     return botcatcher

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vmail=all_clean_data['verify_email']
        if email != vmail:
            raise forms.ValidationError("mail should match")







class Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','password','email')
class Userprofileinfoform(forms.ModelForm):
    class  Meta():
         model=Userprofileinfo
         fields=('portfolio','profile_pic')
