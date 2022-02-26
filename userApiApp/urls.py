from django.urls import path
from . import views


urlpatterns = (

    path('', views.UserDataAPIView.as_view(), name='users_data'),
    path('<int:id>/', views.UserDetailAPIView.as_view(), name='user_detail'),

)