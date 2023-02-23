from django.contrib import admin
from django.urls import path
from .views import ViewALL ,GETallDetails,ShowallData,adddetails,getDeplist,removeEmployee,Filterdetails

urlpatterns = [
    # path("",mainpage),
    path('',ViewALL),
    # path("signIn",SigninPage),
    # path("signUp",SignUpPage),
    path('ALLDetailsAPI',GETallDetails.as_view()),
    path('ViewallEmployee',ShowallData),
    path('addAnEmploye',adddetails),
    path('editAnEmploye',Filterdetails),
    path('removeAnEmployee',removeEmployee),
    path('removeAnEmployee/<int:pk>',removeEmployee)
]   
