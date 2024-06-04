from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm  # Create a CommentForm to handle comment input
from recipes.models import Recipe
from django.contrib.auth.decorators import login_required
from .models import comments


@login_required
def create_comments(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.created_by = request.user
            comment.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = CommentForm()

    return render(request, 'comments/create_comments.html', {'form': form, 'recipe': recipe})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(comments, pk=comment_id)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('recipe_detail', recipe_id=comment.recipe.pk)
    
    return render(request, 'comments/delete_comment.html', {'comment': comment})
