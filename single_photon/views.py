# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import Template
from django.template import loader
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from models import Signup,Login,Verify

# Create your views here.

def index(request):
    template = loader.get_template('landing_page.html')
    context = {}
    return HttpResponse(template.render(context,request))

def home(request):
    template = loader.get_template('landing_page.html')
    context = {}
    return HttpResponse(template.render(context,request))

def nexus_login_view(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context,request))

def nexus_signup_view(request):
    template = loader.get_template('sign_up.html')
    context = {}
    return HttpResponse(template.render(context,request))

def email(request):
    template = loader.get_template('email_confirm.html')
    context = {}
    return HttpResponse(template.render(context,request))

def login(request):

 	username=request.POST.get('txt_email')
 	password=request.POST.get('txt_password')
 	context={"Error":''}
 	
 	try:
 		obj_login = Login.objects.get(login_username = username) #(obj_login is an object which retrives result set ie; our table -this command is equivalent to select * from login1 where login_username)
 		mail=Verify.objects.get(login=obj_login.id)		
 		# print obj_login.login_username
 		# print obj_login.login_password
 		if(obj_login.login_username==username and obj_login.login_password==password):
 			if(mail.login.id==obj_login.id):
	 			template=loader.get_template('success1.html')
	 			context={}
 		else:
 			template=loader.get_template('login.html')
 			context={"Email":"PLEASE VERIFY YOUR EMAIL !!!"}
 	except:
 			template=loader.get_template('login.html')
 			context={"Email":"PLEASE VERIFY YOUR EMAIL !!!"}
 	return HttpResponse(template.render(context,request))



def sign_up(request):
	
	name=request.POST.get('txt_name')
 	email = request.POST.get('txt_email')
 	password=request.POST.get('txt_password') 	
 	confirm_pwd =request.POST.get('txt_confirm_pwd') 

 	me = "test.digna@gmail.com"
	you = email
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Confirmation Email"
	msg['From'] = me
	msg['To'] = you
	text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
	html = """\
	<html>
	  <head>
	  </head>
	  <body>
	  	<p><font color="Blue"><h1>Hello !!!<h1></font><br>
        <h2><font color="Blue">This is the verification message....</font</h2><br>
        <h2><font color="Black">Click to verify :</font></h2>   
	    <button type="submit"><a href="http://127.0.0.1:8000/single_photon/email/">VERIFY</a></button></p>
	  </body>
	</html>
	"""
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')
	msg.attach(part1)
	msg.attach(part2)
	s = smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login(me,'dingu@123')
	s.sendmail(me, you, msg.as_string())
	s.quit()
 	try:
 		check_email_exist = Login.objects.filter(login_username=email).exists()
 		if check_email_exist == False:

		 	a=Login(login_username=email,login_password=password)
			a.save()
			fk_id=a.id
			
			 #----c is the object created here------
			c=  Login.objects.get(id = fk_id)
			request.session['loginid']=fk_id

		 	b = Signup(name=name,login=c)
			b.save()
			
			template=loader.get_template('login.html')
			context={"Email":"PLEASE VERIFY YOUR EMAIL !!!"}	
			
		else:
			template=loader.get_template('sign_up.html')
			context={"email_err":"Email already Exists"}
	except Exception, e:
	 			template=loader.get_template('sign_up.html')
	 			context={"error":"Invalid Login Credentials"}
	 			print("########## This is the error ############")
	 			print e		
	
 	return HttpResponse(template.render(context,request))

def confirm(request):
	check = request.POST.getlist('confirm_text')

	l_id = request.session.get('loginid')
	print l_id
	log= Login.objects.get(id=l_id)
	try:
	   mail= Verify(login=log,checkbox=check)
	   mail.save()
	   template =loader.get_template('login.html')
	   context ={}

	except Exception, e:    
	  template = loader.get_template('login.html')
	  print("************************")
	  print e
	  context ={}
 	return HttpResponse(template.render(context,request))


