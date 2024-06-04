from django.db import models
from django.utils.timezone import now
from account.models import User
from recipes.models import Recipe

# Comments model 

class comments(models.Model) :
    id = models.AutoField(primary_key=True)
    comment = models.TextField(blank=False, editable=True, max_length = 200)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, editable=False)
    created_at = models.DateTimeField(default=now, editable=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return f'{self.created_by.name} - {self.comment}'


