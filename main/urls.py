from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('brand/<str:name>/', views.brand , name='brand'),
    path('review/<int:id>/',views.review,name='review')
]