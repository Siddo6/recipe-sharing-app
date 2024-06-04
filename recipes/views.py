from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RecipeForm
from .models import Recipe
from django.shortcuts import render, get_object_or_404
from comments.models import comments
from django.db.models import Q

# Create your views here.
@login_required
def create_recipe (request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid ():
            form.instance.created_by = request.user
            form.save()
            return redirect ('success_page')
    else:
        form = RecipeForm()

    return render(
        request,
        'recipes/create_recipe.html',
        {
            "form": form
        }
    )

@login_required
def success_page (request):
    user_recipes = Recipe.objects.filter(created_by=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid ():
            form.instance.created_by = request.user
            form.save()
            
    return render(
        request,
        'recipes/success_page.html', {'user_recipes': user_recipes})

    
    
def all_recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/all_recipe_list.html', {'recipes': recipes})


@login_required
def user_recipe_list(request):
    user_recipes = Recipe.objects.filter(created_by=request.user)
    a = 0
    for recipe in user_recipes:
        a += 1

    return render(request, 'recipes/user_recipe_list.html', {'user_recipes': user_recipes, 'recipe_count': a})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.visit_count += 1
    recipe.save()
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'ingredients':recipe.ingredients.split(',')})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})

@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('user_recipe_list')  # Redirect to the recipe list or any other page
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})


def search_results (request):
    query = request.GET.get ('q')
    if query:
        results = Recipe.objects.filter(Q(title__icontains=query) | Q(ingredients__icontains=query))
    else:
        results=Recipe.objects.none()
    return render (request, 'recipes/search_results.html',{'results':results, 'query':query})