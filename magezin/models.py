from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


# Create your models here.


class ipadd(models.Model):
    ip_add = models.GenericIPAddressField()


class magezin(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    body = models.TextField(verbose_name='متن')
    auth = models.ForeignKey(User ,on_delete=models.CASCADE, null=True)
    status_choice = (
        ('draft','پیشنویس'),
        ('send','ارسال'),
       
    )
    status = models.CharField(choices=status_choice, default='draft',max_length=200,verbose_name='وضعیت')
    conformation_choice=(
        ('reject','رد شده'),
        ('confirm','تایید شده'),
        
    )
    conformation=models.CharField(choices=conformation_choice,max_length=200,null=True,blank=True,default=None)
   
   
   

    def __str__(self):
        return self.title


class coment(models.Model):
    post = models.ForeignKey(magezin , on_delete=models.CASCADE , related_name='cm')   
    text = models.CharField(max_length=400)     
    writer = models.ForeignKey(User , on_delete=models.CASCADE)
