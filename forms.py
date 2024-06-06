from django import forms
from .models import TodoItems

#Choices = (
 #   ("0", "Yes"),
  #  ("1", "No"),
#)

class TodoItemsForm(forms.ModelForm):
    class Meta:
        model = TodoItems
        fields = ['title', 'description','datedue', 'priority']
        widgets = {
            'datedue' : forms.DateInput(attrs={'placeholder' : 'MM/DD/YYYY'}),
            'description' : forms.Textarea(attrs={'rows':5, 'cols':27}),
        }
