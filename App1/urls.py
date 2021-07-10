from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.maha_form,name='maha_insert'), #GET AND POST REQ. FOR INSERT OPERATION
    path('<int:id>/', views.maha_form,name='maha_update'), #GET AND POST REQ. FOR UPDATE OPERATION
    path('delete/<int:id>', views.maha_delete,name='maha_delete'), #DELETE
    path('list/', views.maha_list,name='maha_list'), #GET REQ. TO RETRIEVE AND DISPLAY ALL RECORDS
]