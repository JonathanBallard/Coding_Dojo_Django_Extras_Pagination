


''' 
================================================================================ 
================================================================================ 
                            APP-LEVEL URLS.PY: page_app 
================================================================================ 
================================================================================ 
''' 



from django.urls import path 
from django.conf.urls import url 
from . import views 

urlpatterns = [ 
    path('', views.root), 
    path('<int:page>/', views.index), 
    path('lead/<int:page>/', views.pagination), 
    path('lead/new/', views.newLead), 

] 
