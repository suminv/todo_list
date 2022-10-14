from django.urls import path
from django.contrib.auth.views import LogoutView

from base import views
from base.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='detail_task'),
    path('create-task', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),




]
