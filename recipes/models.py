from django.db import models
from django.utils.timezone import now
from account.models import User
from django.contrib.postgres.search import SearchVectorField

# Create your models here.

class Recipe (models.Model):
    
    CATEGORIES = (
        ('appetizer','Appetizer'),
        ('soup', 'Soup'),
        ('salad', 'Salad'),
        ('main', 'Main dishes'),
        ('pasta', 'Pasta/Noodles'),
        ('rice', 'Rice/Grains'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('seafood', 'Seafood'),
        ('meat', 'Meat'),
        ('pizza', 'Pizza'),
        ('sandwich', 'Sandwich/Wraps'),
        ('side', 'Side dishes'),
        ('breakfast/brunch', 'Breakfast/Bruch'),
        ('dessert', 'Desserts'),
        ('grill', 'Grilling/Barbecue'),
        ('healthy', 'Healthy/Low calories'),
        ('international', 'International Cuisine')
    )

    DIFFICULTY_LEVEL = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard')
    )
        
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    category = models.CharField(
        max_length = 255,
        choices = CATEGORIES,
        default = None,
        blank = True,
        null = True
    )
    difficulty = models.CharField(
            max_length = 255,
            choices = DIFFICULTY_LEVEL,
            default = None,
            blank = True,
            null = True
        )
    cooking_time = models.PositiveIntegerField ()
    created_by = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    search_vector = SearchVectorField(null=True, editable = False)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

