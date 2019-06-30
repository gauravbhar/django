from . import views
from django.urls import path



urlpatterns=[
    #path('',views.index, name='index'),
    #path('heading<int:Reported_id>',views.heading, name='heading'),
    path('Article/<str:year>/',views.year_achieve,name='year_acheive')
    ]
