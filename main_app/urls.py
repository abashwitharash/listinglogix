from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('lists/', views.lists_index, name='lists-index'),
    path('lists/<int:list_id>/', views.list_detail, name='list-detail'),
    path('lists/create/', views.ListCreate.as_view(), name='list-create'),
    path('lists/<int:pk>/update/', views.ListUpdate.as_view(), name='lists-update'),
    path('lists/<int:pk>/delete/', views.ListDelete.as_view(), name='lists-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('all/', views.all_listings, name='all-listings'),
    path('profile/create/', views.create_profile, name='create-profile'),
    path('profile/me/', views.my_profile, name='my-profile'),
    path('profile/edit/', views.EditProfile.as_view(), name='edit-profile'),
    path('profile/delete/', views.DeleteProfile.as_view(), name='delete-profile'),
    path('agents/', views.all_agents, name='all-agents'),
    path('agents/<int:user_id>/', views.agent_profile, name='agent-profile'),


]   
