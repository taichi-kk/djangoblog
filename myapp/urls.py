from django.urls import path, include
from . import views


app_name = 'myapp'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post_create', views.PostCreate.as_view(), name='post_create'),
    path('post_detail/<int:pk>', views.PostDetail.as_view(), name='post_detail'),
    path('post_update/<int:pk>', views.PostUpdate.as_view(), name='post_update'),
    path('post_dalete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
]
