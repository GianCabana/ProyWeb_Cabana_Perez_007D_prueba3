from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Categoria, Photocard, Boleta, detalle_boleta, Perfil
from .forms import PhotocardForm, RegistroUserForm, UserProfileForm
from .compras import Carrito



def index(request):
    return render (request, 'index.html')

def sobreNosotros(request):
    return render (request, 'sobreNosotros.html')

def stock(request):
    return render (request, 'stock.html')

def contacto(request):
    return render (request, 'contacto.html')

def articulos(request):
    return render (request, 'articulos.html')

@login_required
def productos(request):
    photocard = Photocard.objects.all()              #similar a select * from Vehiculo
    return render(request, 'productos.html', {'photocard':photocard})

def modificar(request, id):
    photocard = Photocard.objects.get(idPhotocard=id)
    datos={
        'forModificar': PhotocardForm(instance=photocard),     #crea un obj de tipo formulario
        'photocard':  photocard
    }
    if request.method=='POST':
        formulario= PhotocardForm(request.POST, request.FILES, instance=photocard)
        if formulario.is_valid():
            formulario.save()               #actualiza la información del obj.
            return redirect('productos')
    return render(request, 'modificar.html', datos)

def crear(request):
    if request.method == 'POST':
        photocardForm = PhotocardForm(request.POST, request.FILES)
        if photocardForm.is_valid():
            photocardForm.save()
            return redirect('productos')
    else:
        photocardForm = PhotocardForm()
    return render(request, 'crear.html', {'photocardForm': photocardForm})

def detalle(request, id):
    photocard = get_object_or_404(Photocard, idPhotocard=id)   #realiza busquedas especificas por atributo pk
    return render (request, 'detallePhotocard.html', {'photocard': photocard})

def modificar(request, id):
    photocard = Photocard.objects.get(idPhotocard=id)
    datos={
        'forModificar': PhotocardForm(instance=photocard),     #crea un obj de tipo formulario
        'photocard': photocard
    }
    if request.method=='POST':
        formulario= PhotocardForm(request.POST, request.FILES, instance=photocard)
        if formulario.is_valid():
            formulario.save()               #actualiza la información del obj.
            return redirect('productos')
    return render(request, 'modificar.html', datos)

def eliminar(request, id):
    photocard = get_object_or_404(Photocard, idPhotocard=id)
    if request.method=='POST':
        if 'elimina' in request.POST:       #botón cuyo name es elimina en html para confirmar
            photocard.delete()               #elimina el objeto despues de confirmar
            return redirect ('productos')
        else:
            return redirect ('detalle', idPhotocard=id)
    return render (request, 'eliminar.html', {'photocard': photocard})
    
def cerrar(request):
    logout(request)
    return redirect('index')

def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=='POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                                password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('index')
        data["form"]=formulario
    return render(request, 'registration/registrar.html',data)
        


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    photocard = Photocard.objects.get(idPhotocard=id)
    carrito_compra.agregar(photocard=photocard)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    photocard = Photocard.objects.get(idPhotocard=id)
    carrito_compra.eliminar(photocard=photocard)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    photocard = Photocard.objects.get(idPhotocard=id)
    carrito_compra.restar(photocard=photocard)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    

def tienda(request):
    photocards = Photocard.objects.all()
    datos={
        'photocards':photocards
    }
    return render(request, 'tienda.html', datos)

def generarBoleta(request):
    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total += int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total=precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
        producto = Photocard.objects.get(idPhotocard=value['photocard_id'])
        cant = value['cantidad']
        if producto.stock >= cant:
            producto.stock -= cant
            producto.save()
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta=boleta, id_producto=producto, cantidad=cant, subtotal=subtotal)
            detalle.save()
            productos.append(detalle)
        else:
            # manejar el caso cuando el stock no es suficiente
            pass
    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html', datos)

@login_required
def perfil(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Redirigir a alguna página de éxito o renderizar nuevamente el perfil
            return redirect('perfil')  # Ajusta 'profile' a la URL de tu perfil
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'perfil.html', {'form': form})