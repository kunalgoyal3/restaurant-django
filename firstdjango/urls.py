from django.contrib import admin
from django.urls import path
from foodapp.views import *

admin.site.site_header  =  "Welcome to Admin pannel"  
admin.site.site_title  =  "Kunal goyal"
admin.site.index_title  =  "title not exist"

urlpatterns = [
    path('',receipe,name="Home"),
    path('restaurent',receipe,name="Home"),
    path('delete/<int:record_id>/', deleterecord, name="deleterecord"),
    # path('update/<int:record_id>/', updaterecord, name="updaterecord"),
    path('update/<int:record_id>/', updaterecord, name='updaterecord'),


 #   path('contact/',contact,name="contact"),
  

    path('admin/', admin.site.urls),
]
