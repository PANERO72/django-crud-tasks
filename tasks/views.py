from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.utils import timezone

from .models import Task
# from .forms import CreateTaskForm
from .forms import TaskForm

from django.http import HttpResponse

#import sweetify

# Additional methods with the type already defined
# sweetify.info(request, 'Message sent', button='Ok', timer=3000)
# sweetify.warning(request, 'This is a warning... I guess')

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': UserCreationForm
        })
    else:

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                user_login(request, user)
                messages.success(request, '¡Usuario creado con éxito!')
                return redirect('login')
                # return render(request, 'login.html', {
                #     'form': UserCreationForm,
                # })

            except IntegrityError:
                messages.error(request, '¡El usuario ya existe!')
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                })
        else:
            messages.error(request, '¡La contraseña no coindice!')
            return render(request, 'register.html', {
                'form': UserCreationForm,
            })

    # return render(request, 'login.html', {
    #    'form': UserCreationForm,
    # })

# URL para abrir la página del formulario de inicio de sesión
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            messages.error(request, '¡Usuario o contraseña son incorrectos!')
            return render(request, 'login.html', {
                'form': AuthenticationForm, 
            })
        else:
            user_login(request, user)
            return redirect('home')

# URL solo para abrir la página de tareas
@login_required
def tasks(request):
    tasks = Task.objects.filter(user = request.user)

    return render(request, 'tasks.html', {'tasks': tasks})

# URL solo para abrir la página de detalles de un tarea
@login_required
def task_details(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user = request.user)
        form = TaskForm(instance=task) 

        return render(request, 'task_details.html', {'task': task, 'form': form})
    else:
        try:
            date_completed = request.POST.get('date_completed') 

            if date_completed:
                print(date_completed, 'Seleccioado')
                task = get_object_or_404(Task, pk=task_id, user = request.user)
                task.datecompleted = timezone.now()
                task.save()
            else:
                print(date_completed, 'No selecionado')
            
            task = get_object_or_404(Task, pk=task_id, user = request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            messages.error(request, "¡Error al actualizar la tarea!")
            return render(request, 'task_details.html', {'task': task, 'form': form})

# URL para abrir la página del formulario de crear nueva tarea y recopilar datos del formulario
@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    
    else:
        try:
            form = TaskForm(request.POST)

            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()

            return redirect('tasks')

        except ValueError:

            messages.error(request, "Hubo un error, por favor proporcione datos válidos.")
            return render(request, 'create_task.html', {
                'form': TaskForm
            })

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'GET':
        # messages.warning(request, "¿Desea eliminar esta taera?")
        task.delete()
        return redirect('tasks')

# URL para cerrar sesión en le sitio
def logout(request):
    user_logout(request)
    return redirect('login')