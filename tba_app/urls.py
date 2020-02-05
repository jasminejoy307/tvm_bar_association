from django.urls import path
from tba_app import views
from django.views.generic import TemplateView

urlpatterns=[
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('memberlist',TemplateView.as_view(template_name='member.html'),name='member'),
    path('loginpage',TemplateView.as_view(template_name='login.html'),name='login'),
    path('registerpage',TemplateView.as_view(template_name='reg.html'),name='reg'),
    path('homeadmin',TemplateView.as_view(template_name='adminhome.html'),name='adminhome'),
    path('homemember',TemplateView.as_view(template_name='memberhome.html'),name='memberhome'),
    path('viewprofile',TemplateView.as_view(template_name='profileview.html'),name='profileview'),
    path('proedit',TemplateView.as_view(template_name='profileedit.html'),name='profileedit'),
    path('msg',TemplateView.as_view(template_name='contact.html'),name='contact'),

    
    
   
    path('registerdetails/',views.regview,name='adminhome1'),
    path('reg',views.register,name='register'),
    path('approval',views.approval,name='approv'),
    path('auth',views.authenticate,name='submitt'),
    path('viewmembers',views.membersview,name='member'),
    path('details',views.detailsview,name='profileview'),
    path('detailsedit',views.editprofile,name='profileedit'),
    path('connect',views.contactadmin,name='cont'),
    path('saveprofile',views.editsave,name='proedit'),
    path('contacts/',views.viewmsg,name='contact'),
    path('read',views.readmsg,name='readmessage'),
]
