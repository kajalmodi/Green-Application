from django.urls import path
from . import views
urlpatterns = [
    #giving path to every page to its releted view
    path('',views.login,name='login'),
    path('camera',views.camera,name='camera'),
    path('airdust',views.airdust,name='airdust'),
    path('temperature',views.temperature,name='temperature'),
    path('row1',views.row1,name='row1'),
    path('row2',views.row2,name='row2'),
    path('history',views.history,name='history'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('controlmotor',views.controlmotor,name='controlmotor'),
    path('logout',views.logout,name='logout'),
    path('temp',views.temp,name='temp')
    
]