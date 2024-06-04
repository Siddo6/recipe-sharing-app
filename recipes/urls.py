from django.urls import path
from . import views

urlpatterns = [
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('success_page/', views.success_page, name='success_page'),
    path('all_recipe_list/', views.all_recipe_list, name='all_recipe_list'),
    path('user_recipe_list/', views.user_recipe_list, name='user_recipe_list'),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path ('search_results/', views.search_results, name='search_results')
]