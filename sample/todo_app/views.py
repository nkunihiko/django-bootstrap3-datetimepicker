from django.shortcuts import render
from sample.todo_app.forms import ToDoForm


def edit(request):
    if request.method == 'GET':
        form = ToDoForm()
    else:
        form = ToDoForm(request.POST)
    return render(request,
                  "todo_app/template.html",
                  dict(form=form))
