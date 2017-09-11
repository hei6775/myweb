# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#导入网络方面的模块
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template.loader import get_template
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

#导入认证模块
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
#导入其它模块
from datetime import datetime
from django.contrib import messages
from django.core.mail import EmailMessage
#导入模型
from mysite import models
from mysite import forms
# Create your views here.

#主页显示
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    messages.get_messages(request)
    
    template = get_template('index.html')
    posts = models.Bozhu.objects.all()
    now = datetime.now()
    html = template.render(context=locals(),request=request)
    return HttpResponse(html)
    
    
#单篇博客处理
def detail(request,id):
    if request.user.is_authenticated:
        username = request.user.username
    template = get_template('detail.html')
    try:
        detail = models.Bozhu.objects.get(id=id)
    except:
        return Http404
    now = datetime.now()
    html = template.render(context=locals(),request=request)
    return HttpResponse(html)
    
    
    
#登录函数        
def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['user_name']
            userpass = request.POST['user_pass']
            user = authenticate(username=username,password=userpass)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    print 'success'
                    messages.add_message(request,messages.SUCCESS,'成功登录了')
                    return redirect('/')
                else:
                    messages.add_message(request,messages.WARNING,'帐号或密码错误')
            else:
                messages.add_message(request,messages.WARNING,'帐号或密码错误')
        else:
            messages.add_message(request,messages.WARNING,'输入字符不合法')
    else:
        login_form = forms.LoginForm()
    template = get_template('login.html')
    
    html = template.render(context=locals(),request=request)
    
    return HttpResponse(html)
    

#注销函数
@login_required
def logout(request):
    auth.logout(request)
    messages.add_message(request,messages.INFO,'成功退出')
    return redirect('/')
    
    
#写博客模块
@login_required
def write(request):
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        write_form = forms.WriteForm(request.POST)
        if write_form.is_valid():
            messages.add_message(request,messages.INFO,'您的这篇博客已经保存...')
            write_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.WARNING,'请检查各个字段，暂时不支持暂存为草稿箱功能')
    else:
        write_form = forms.WriteForm()
        #messages.add_message(request,messages.WARNING,'请检查各个字段，暂时不支持暂存为草稿箱功能')
    template = get_template('post.html')
    html = template.render(context=locals(),request=request)
    return HttpResponse(html)

#联系管理员模块
def post_email(request):
    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            messages.add_message(request,messages.INFO,'感谢您的来信，我们会尽快处理')
            contact_name = contact_form.cleaned_data['contact_name']
            contact_place = contact_form.cleaned_data['contact_place']
            contact_email = contact_form.cleaned_data['contact_email']
            contact_message = contact_form.cleaned_data['contact_message']
            email_body = u'''
            网友昵称：{}
            居住城市：{}
            反映意见，如下：{}
            '''.format(contact_name,contact_place,contact_message)
            email = EmailMessage(
                                '来自网友的一封邮件',
                                email_body,
                                contact_email,
                                ['913799761@qq.com']
                                )
            email.send()
        else:
            messages.add_message(request,messages.WARNING,'请检查您输入的信息是否正确')
    else:
        contact_form = forms.ContactForm()
    template = get_template('email.html')
    html = template.render(context=locals(),request=request)
    
    return HttpResponse(html)