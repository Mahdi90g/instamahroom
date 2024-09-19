from django.shortcuts import render , redirect , get_object_or_404
from .models import magezin , coment
from django.views.generic.edit import CreateView,UpdateView, DeleteView , FormMixin
from django.urls import reverse_lazy , reverse
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .forms import signup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView
from.mixins import editmixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import views as auth_views
from .forms import comentform
# Create your views here.



def home(request):
    posts = magezin.objects.all()
    if request.method == "POST":
        form = comentform(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')
            post = magezin.objects.get(id=post_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.writer = request.user 
            comment.save()
            return redirect('home')
    else:
        form = comentform()

    return render(request, './home.html',{'posts':posts , 'form':form})           







class homee(FormMixin,ListView):
    template_name = './home.html'
    queryset= magezin.objects.all()
    form_class = comentform

    def get_success_url(self):
        return reverse('/',kwargs={"pk":self.object.id})

    def post(self,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form() 
        if form.is_valid():
            return self.form_valid(form)
        else:
            pass    
    def form_valid(self, form):
        form.save()
        return super(homee,self).form_valid(form)

        
    


class new(LoginRequiredMixin,CreateView):
    model=magezin
    template_name='./new.html'
    fields=['title','body','status',]
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        form.instance.auth = self.request.user
        return super().form_valid(form)




class edit(LoginRequiredMixin,UpdateView):
    model=magezin
    template_name='./edit.html'
    success_url=reverse_lazy('mypost')
    fields=['title','body','status',]
    def form_valid(self,form):
        form.instance.conformation = ''
      
        return super().form_valid(form)

class editadmin(LoginRequiredMixin,UpdateView):
    model=magezin
    template_name='./editadmin.html'
    success_url=reverse_lazy('control')
    fields=['title','body','status','conformation']
      


   
class delt(DeleteView):
    model=magezin
    template_name='./delt.html'
    success_url=reverse_lazy('home')

    
def login_user(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username , password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,('نام کاربری یا کلمه ی عبور نادرست است'))
            return redirect('login')
            

    else:      

        return render(request,'./login.html')
   
def logout_user(request):
    logout(request)
    return redirect('home')



def signup_u(request):
    form = signup()
    if request.method == 'POST' :
        form = signup(request.POST)
        if form.is_valid :
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(request , username = username , password = password1)
            return redirect('login')
        else:
            messages.success(request, ('اطلاعات را به درستی وارد کنید')) 
            return redirect('signup') 
            
             
    else:
        return render(request , './signup.html' , {'form':form})         
    


class profile(UpdateView):
    model=User
    fields = ['first_name','last_name','username']    
    success_url = reverse_lazy('home')
    template_name = './profile.html'



class myposti(LoginRequiredMixin,ListView):
    template_name = 'control/mypost.html'
    def get_queryset(self):
        return  magezin.objects.filter(auth=self.request.user)
    
class control(LoginRequiredMixin,ListView):
    template_name = 'control/control.html'
    
    queryset= magezin.objects.all()

   
       
   
class allpost(LoginRequiredMixin,ListView):
    template_name = 'control/allpost.html'
    queryset= magezin.objects.all()


class changepass(PasswordChangeView):
    template_name = './password_change_form.html'
    success_url=reverse_lazy('done')

  
class done(PasswordChangeDoneView) :
    template_name='./password_change_done.html'  
    
        
class passreset(auth_views.PasswordResetView):
    template_name = 'pass/reset.html'


class passdone(auth_views.PasswordResetDoneView):
    template_name='pass/done.html'

class passconf(auth_views.PasswordResetConfirmView)   :
    template_name = 'pass/conf.html' 

class passend(auth_views.PasswordResetCompleteView):
        template_name = 'pass/end.html' 