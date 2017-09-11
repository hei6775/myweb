#-*- coding:utf-8 -*-
from django import forms
from mysite import models
from django.utils import timezone
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    
    user_name = forms.CharField(label='您的帐号',max_length=10)
    user_pass = forms.CharField(label='您的密码',widget=forms.PasswordInput())
    captcha = CaptchaField(label='验证码')
    
class WriteForm(forms.ModelForm):
    class Meta:
        model = models.Bozhu
        fields = ['name','title','body','pub_date']
    
    def __init__(self,*args,**kwargs):
        super(WriteForm,self).__init__(*args,**kwargs)
        self.fields['name'].label = '作者'
        self.fields['title'].label = '文章标题'
        self.fields['body'].label = '文章正文'
        self.fields['pub_date'].label = '时间'
        self.fields['pub_date'].initial = timezone.now
        self.fields['name'].initial = 'hei6775'
        
#联系管理员的表单
class ContactForm(forms.Form):
    CITYS = (
            ('北京','北京'),('天津','天津'),('上海','上海'),('台湾','台湾'),('港澳','港澳'),
            ('安徽','安徽'),('重庆','重庆'),('福建','福建'),('广东','广东'),
            ('广西','广西'),('贵州','贵州'),('甘肃','甘肃'),('湖南','湖南'),('湖北','湖北'),('海南','海南'),('河南','河南'),('河北','河北'),('黑龙江','黑龙江'),
            ('江苏','江苏'),('江西','江西'),('吉林','吉林'),
            ('辽宁','辽宁'),('内蒙古','内蒙古'),('宁夏','宁夏'),('青海','青海'),
            ('山东','山东'),('山西','山西'),('陕西','陕西'),('四川','四川'),
            ('浙江','浙江'),('新疆','新疆'),('西藏','西藏'),('云南','云南'),
            
            )
    contact_name = forms.CharField(label='您的姓名',max_length=50,initial='匿名者')
    contact_place = forms.ChoiceField(label='您的所在省份',choices=CITYS)
    contact_email = forms.EmailField(label='您的电子邮箱')
    contact_message = forms.CharField(label='您的意见',widget=forms.Textarea)
    