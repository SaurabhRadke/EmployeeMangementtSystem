from django.contrib import admin
from django.urls import path
from .views import ViewALL ,GETallDetails,ShowallData,Editdetails,adddetails,getDeplist,removeEmployee,SigninPage,SignUpPage,mainpage

urlpatterns = [
    path("",mainpage),
    path('page',ViewALL),
    path("signIn",SigninPage),
    path("signUp",SignUpPage),
    path('ALLDetailsAPI',GETallDetails.as_view()),
    path('ViewallEmployee',ShowallData),
    path('addAnEmploye',adddetails),
    path('editAnEmploye',Editdetails),
    path('removeAnEmployee',removeEmployee),
    path('removeAnEmployee/<int:pk>',removeEmployee)
]   
