
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('core.urls')),
    path('', include ('account.urls')),
    path('', include ('recipes.urls')),
    path('', include ('comments.urls')),
]
