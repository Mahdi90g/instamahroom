from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import magezin , coment


class signup(UserCreationForm):
    first_name = forms.CharField(label="",max_length=60,widget=forms.TextInput(attrs={'class':'first-name','placeholder':'نام خود ذا وارد کنید'}))
    last_name = forms.CharField(label="",max_length=60,widget=forms.TextInput(attrs={'class':'first-name','placeholder':'نام خانوادگی خود ذا وارد کنید'}))
    username = forms.CharField(label="",max_length=20,widget=forms.TextInput(attrs={'class':'first-name','placeholder':'نام کاربری خود ذا وارد کنید' , 'required':'True'}))
    password1 = forms.CharField(label="",max_length=50,widget=forms.PasswordInput(attrs={'class':'first-name','placeholder':'رمز خود را وارد کنید','type':'password','name':'password'}))
    email = forms.EmailField(label="",max_length=50,widget=forms.EmailInput(attrs={'class':'first-name','placeholder':'ایمیل خود را وارد کنید' , 'required':'True'}))
    password2 = forms.CharField(label="",max_length=50,widget=forms.PasswordInput(attrs={'class':'first-name','placeholder':'مجدد رمز خود را وارد کنید','type':'password','name':'password'})) 
    
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')
   

class editform(forms.ModelForm):
    title = forms.CharField(label="عنوان",max_length=60,widget=forms.TextInput(attrs={'class':'title', 'disabled':'True'}))
    body = forms.TimeField()
    status = forms.CharField()
    conformation = forms.CharField()

    class Meta:
        model= magezin
        fields = ('title','body','status','conformation')



class comentform(forms.ModelForm):
     class Meta:
        model = coment
        fields = ('post','text','writer',)
