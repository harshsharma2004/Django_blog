from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('loginn/', views.loginn, name='loginn'),
    path('home/', views.home, name='home'),
    path('newpost/', views.new_post, name='new_post'),  # FIXED
    path('mypost/', views.my_posts, name='my_posts'),   # FIXED
    path('signout/', views.signout, name='signout'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    # Remove this unless you actually have a post_detail view
    # path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
