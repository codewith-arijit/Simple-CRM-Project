from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path , include       
from .views import CustomerCreate, CustomerUpdate
from .views import customer_template


urlpatterns = [
    path('', CustomerCreate.as_view()),
    path('<int:pk>/', CustomerUpdate.as_view()),
    
    url(r'^template/$', customer_template, name='customer_template'),
]

"""
    path('', CustomerList.as_view()),
    path('<int:pk>/', CustomerDetail.as_view(), name='retrieve-customer'),
    path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
    
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer'),
    path('item/create/', ItemCreateView.as_view(), name='create-customer'),
"""

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)