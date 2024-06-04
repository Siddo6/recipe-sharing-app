from django.urls import path
from . import views

urlpatterns = [
    path('<int:recipe_id>/create_comments/', views.create_comments, name='create_comments'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]