from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'email/$',views.email, name='email'),

    url(r'login/$', views.login, name = 'login'),
    url(r'nexus_login_view/$', views.nexus_login_view, name = 'nexus_login_view'),
    url(r'nexus_signup_view/$', views.nexus_signup_view, name = 'nexus_signup_view'),
    url(r'sign_up/$', views.sign_up, name = 'sign_up'),
    url(r'home/$', views.home, name = 'home'),
    url(r'confirm/$', views.confirm, name = 'confirm'),
    

]
