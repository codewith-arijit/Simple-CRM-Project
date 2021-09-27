from django.urls import path , include
from .views import CustomerCreate, CustomerUpdate


urlpatterns = [
    path('', CustomerCreate.as_view()),
    path('<int:pk>/', CustomerUpdate.as_view()),
    
]

"""
    path('', CustomerList.as_view()),
    path('<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer'),
    path('item/create/', ItemCreateView.as_view(), name='create-customer'),
"""