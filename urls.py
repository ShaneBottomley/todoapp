from django.urls import path
from .views import view_todo_items, remove_todo_items, edit_todo_items

urlpatterns = [
    path('todos/', view_todo_items, name='view_todo_items'),
    path('remove/<int:todo_id>/', remove_todo_items, name='remove_todo_items'),
    path('edit/<int:todo_id>/', edit_todo_items, name='edit_todo_items')
    
]