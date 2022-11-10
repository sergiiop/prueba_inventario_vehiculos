from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from core.form import FormPropietarios, FormVehiculo,FormTicket
import datetime

from core.models import Propietarios, Vehiculos, Ticket

# Create your views here.
@login_required(login_url='signin')
def index(request):
    user = request.user
    vehiculos = Vehiculos.objects.all()
    propietarios = Propietarios.objects.all()
    tickets = Ticket.objects.filter(estado='Activo')
    limit = True
    if len(tickets) >= 7:
        limit=False

    print(len(tickets))
    print(limit)
    if request.method=='POST':
        pass
    return render(request, 'index.html', {
        'user': user,
        'propietarios': propietarios,
        'vehiculos': vehiculos,
        'tickets': tickets,
        'limit': limit
        })

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         # tipo_documento = request.POST['tipo_documento']
#         # documento=request.POST['documento']
#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email taken')
#                 return redirect('signup')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username taken')
#                 return redirect('signup')
#             # elif Propietarios.objects.filter(documento=documento).exists():
#             #     messages.info(request, 'Document taken')
#             #     return redirect('signup')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password)
#                 user.save()

#                 #create a Profile object for the new user
#                 # user_model = User.objects.get(username=username)
#                 # new_profile = Propietarios.objects.create(user=user_model, id_user=user_model.id, tipo_documento=tipo_documento, documento=documento)
#                 # new_profile.save()

#                 #log user in and redirect
#                 user_login = authenticate(username=username, password=password)

#                 login(request, user_login)
#                 return redirect('/')
#         else:
#             messages.info(request, 'Password not matching!')
#             return redirect('signup')
#     else:
#         return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('/signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='signin')
def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def create_propietario(request):
    if request.method == 'POST':
        documento = request.POST['documento']
        if Propietarios.objects.filter(documento=documento).exists():
            messages.info(request, 'Document taken')
            return redirect('create_propietario')
        else:
            form = FormPropietarios(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/propietarios/')
                except:
                    messages.info(request, 'Datos invalidos')
                    return redirect('create_propietario')
            else:
                print(form.errors)
    else:
        form = FormPropietarios()
    return render(request, 'create_propietario.html', {
        'form': FormPropietarios
        })

@login_required(login_url='signin')
def view_propietarios(request):
    user = request.user
    propietarios = Propietarios.objects.all()
    if len(propietarios) == 0:
        return render(request, 'propietarios.html', {
            'user': user,
            'message': 'Aun no tienes Propietarios registrados, registra alguno'
            })

    return render(request, 'propietarios.html', {
        'user': user,
        'propietarios': propietarios
        })

@login_required(login_url='signin')
def update_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietarios, pk=propietario_id)
    if request.method == 'POST':
        try:
            form = FormPropietarios(request.POST, instance=propietario)
            form.save()
            return redirect('view_propietarios')
        except:
            messages.info(request, 'Datos invalidos')
            return redirect('update_propietario')
    else:
        propietario = get_object_or_404(Propietarios, pk=propietario_id)
        form = FormPropietarios(instance=propietario)
        return render(request, 'update_propietario.html', {
            'form': form,
            'propietario': propietario
        })

@login_required(login_url='signin')
def delete_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietarios, pk=propietario_id)
    if request.method == 'POST':
        propietario.delete()
        return redirect('index')

def vehiculo_propietario(request, propietario_id):
    user = request.user
    propietario= Propietarios.objects.get(pk=propietario_id)
    vehiculos = Vehiculos.objects.filter(propietario=propietario_id)
    if len(vehiculos) == 0:
        return render(request, 'vehiculos_propietarios.html', {
            'user': user,
            'propietario': propietario,
            'message': 'Aun no tienes Propietarios registrados, registra alguno'
            })

    return render(request, 'vehiculos_propietarios.html', {
        'user': user,
        'propietario': propietario,
        'vehiculos': vehiculos
        })

def view_vehiculo(request):
    user = request.user
    vehiculos = Vehiculos.objects.all()
    if len(vehiculos) == 0:
        return render(request, 'vehiculos.html', {
            'user': user,
            'message': 'Aun no tienes vehiculos registrados, registra alguno'
            })

    return render(request, 'vehiculos.html', {
        'user': user,
        'vehiculos': vehiculos
        })

@login_required(login_url='signin')
def create_vehiculo(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        if Vehiculos.objects.filter(placa=placa).exists():
            messages.info(request, 'Placa ya existente')
            return redirect('vehiculo/create')
        else:
            form = FormVehiculo(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('view_vehiculos')
                except:
                    messages.info(request)
                    return redirect('vehiculo/create')
    else:
        return render(request, 'create_vehiculo.html', {
            'form': FormVehiculo
        })

@login_required(login_url='signin')
def update_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculos, pk=vehiculo_id)
    if request.method == 'POST':
        try:
            form = FormVehiculo(request.POST, instance=vehiculo)
            form.save()
            return redirect('view_vehiculos')
        except:
            messages.info(request, 'Datos invalidos')
            return redirect('update_vehiculo')
    else:
        vehiculo = get_object_or_404(Vehiculos, pk=vehiculo_id)
        form = FormVehiculo(instance=vehiculo)
        return render(request, 'update_vehiculo.html', {
            'form': form,
            'vehiculo': vehiculo
        })

@login_required(login_url='signin')
def delete_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculos, pk=vehiculo_id, propietario=request.user)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('index')

def create_ticket(request):
    if request.method == 'POST':
        form = FormTicket(request.POST)
        propietario_field = request.POST['propietario']
        ticket= Ticket.objects.filter(propietario_id=propietario_field).filter(estado='Activo')
        if ticket:
            messages.info(request, 'Vehiculo ya registrado')
            return redirect('ticket/create')
        else:
            if form.is_valid():
                try:
                    form.save()
                    return redirect('index')
                except:
                    messages.info(request)
                    return redirect('ticket/create')
            messages.info(request)
            return redirect('ticket/create')
    else:
        return render(request, 'create_ticket.html', {
            'form': FormTicket
        })

def registrar_salida(request, ticket_id):
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        now = datetime.datetime.now()
        print('here')
        try:
            ticket.hora_salida = now
            ticket.valor = 2000
            ticket.estado = 'Terminado'
            ticket.save()
            print('success')
            return redirect('index')
        except:
            print('Error')
            return redirect('index')
    else:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        return render(request, 'registrar_ticket.html', {
            'ticket': ticket
        })