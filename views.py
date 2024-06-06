from django.shortcuts import render, redirect, get_object_or_404
from .forms import TodoItemsForm
from .models import TodoItems

# Create your views here.

#view and add to-do items
def view_todo_items(request):
    # process the form data when user selects submit(post)
    if request.method == 'POST':
        #create the form instance 
        form = TodoItemsForm(request.POST)
        #ensure form meets values
        if form.is_valid():
            #save the form to db
            form.save()
            #go to viewtodos(same page but with new, saved todo)
            return redirect('view_todo_items')
    else:
        form = TodoItemsForm()
    todos = TodoItems.objects.all()

    context = {
        'n': range(len(todos)),
        'todos' : todos,
        'form' : form,
    }

    return render(request, 'view_todo_items.html', context)

def remove_todo_items(request, todo_id):
    todo = get_object_or_404(TodoItems, id=todo_id)
    todo.delete()
    return redirect('view_todo_items')

def edit_todo_items(request, todo_id):
        todo = get_object_or_404(TodoItems, id=todo_id)
        if request.method == 'POST':
            print("post worked")
            form = TodoItemsForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                print("redirection")
                return redirect('view_todo_items')
            else:
                print("wasnt valid")
        else:
            
            form = TodoItemsForm(instance=todo)

        return render(request, 'edit_todo_items.html', {'form' : form, 'todo' : todo})

