from django.shortcuts import render , redirect
from ToDoApp.models import *
# Create your views here.
def home(request):
    if request.method == "POST":
        datetime = request.POST.get('datetime')
        name = request.POST.get('name')
        todolist = request.POST.get('todolist')

        todo.objects.create(
            datetime = datetime,
            name = name,
            todolist = todolist
        )
        return redirect('/')
    return render(request,'index.html')

def get_todolist(request):
    queryset = todo.objects.all()
    # print(queryset)
    return render(request,'getdata.html', {'todolists' : queryset})

def updatetodo(request,id):
    queryset = todo.objects.get(id = id)

    if request.method == 'POST':
        datetime = request.POST.get('datetime')
        name = request.POST.get('name')
        todolist = request.POST.get('todolist')

        queryset.datetime = datetime
        queryset.name = name
        queryset.todolist = todolist
        queryset.save()
        return redirect('/')
    
    return render(request,'updatetodo.html', {'todolists' : queryset})

def deletetodo(request,id):
    queryset = todo.objects.get(id = id)
    queryset.delete()
    return redirect('/')
