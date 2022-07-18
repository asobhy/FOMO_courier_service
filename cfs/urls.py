"""cfs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from account import views as account_views
from OrderApp import views as order_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("signup", account_views.signup, name="signup"),
    path("login", account_views.login, name="login"),
    path("logout", account_views.logout, name="logout"),
    path('neworder', order_views.NewOrder, name='neworder'),
    path('send_to_order', order_views.SendToOrder, name='send_to_order'),
    path('myorders', order_views.MyOrders, name='myorders'),
    path('userprofile', account_views.UserProfile, name='userprofile'),
    path('cancelorder/<int:oid>', order_views.CancelOrder, name='cancelorder'),
    path('availableorder', order_views.AvailableOrders, name='availableorder'),
    path('acceptedorder', order_views.AcceptedOrders, name='acceptedorder'),
    path('acceptorder/<int:oid>', order_views.Accept, name='acceptorder'),
    path('orderpicked/<int:oid>', order_views.Picked, name='orderpicked'),
    path('orderdelivered/<int:oid>', order_views.Delivered, name='orderdelivered'),
    path('changeuserdetails', account_views.ChangeUserDetails,
         name='changeuserdetails'),
    path('changepassword', account_views.ChangePassword, name='changepassword'),
    path('orderdetail/<int:oid>', order_views.OrderDetail, name='orderdetail'),
    path('feedbackform/<int:oid>', order_views.FeedbackTake, name='feedbackform'),
    path('feedback', order_views.Feedback, name='feedback'),
    path('ajaxbill', order_views.BillGeneration, name='ajaxbill'),
    path('uservalidate',account_views.ValidateUser,name='uservalidate'),
    path('forgotpassword', account_views.ForgotPassword, name='forgotpassword'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
