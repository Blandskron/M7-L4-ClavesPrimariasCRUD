# README.md

## Proyecto Django Educativo

Este proyecto está diseñado para enseñar los conceptos básicos de Django, incluyendo manejo de claves primarias, relaciones entre modelos y un CRUD completo. Sigue estos pasos para desarrollar el proyecto:

### 1. Instalación de Django

1. Asegúrate de tener Python instalado en tu sistema.
2. Crea y activa un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate   # Linux/macOS
    env\Scripts\activate    # Windows
    ```
3. Instala Django:
    ```bash
    pip install django
    ```

### 2. Crear el Proyecto

1. Crea un proyecto llamado `mysite`:
    ```bash
    django-admin startproject mysite
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd mysite
    ```

### 3. Crear las Aplicaciones

1. Crea dos aplicaciones:
    ```bash
    python manage.py startapp app1
    python manage.py startapp app2
    ```
2. Registra las aplicaciones en el archivo `settings.py` dentro de `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
        ...
        'app1',
        'app2',
    ]
    ```

### 4. Definir los Modelos

1. En `app1/models.py`, define el modelo `ParentModel`:
    ```python
    from django.db import models

    class ParentModel(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=100)

        def __str__(self):
            return self.name
    ```

2. En `app2/models.py`, define el modelo `ChildModel` relacionado con `ParentModel`:
    ```python
    from django.db import models
    from app1.models import ParentModel

    class ChildModel(models.Model):
        id = models.AutoField(primary_key=True)
        parent = models.ForeignKey(ParentModel, on_delete=models.CASCADE)
        description = models.TextField()

        def __str__(self):
            return self.description
    ```

### 5. Migrar la Base de Datos

1. Crea y aplica las migraciones:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### 6. Crear un CRUD Completo

1. En `app2/forms.py`, crea un formulario:
    ```python
    from django import forms
    from .models import ChildModel

    class ChildModelForm(forms.ModelForm):
        class Meta:
            model = ChildModel
            fields = ['parent', 'description']
    ```

2. En `app2/views.py`, implementa las vistas para el CRUD:
    ```python
    from django.shortcuts import render, get_object_or_404, redirect
    from .models import ChildModel
    from .forms import ChildModelForm

    def child_list(request):
        children = ChildModel.objects.all()
        return render(request, 'app2/child_list.html', {'children': children})

    def child_detail(request, pk):
        child = get_object_or_404(ChildModel, pk=pk)
        return render(request, 'app2/child_detail.html', {'child': child})

    def child_create(request):
        if request.method == "POST":
            form = ChildModelForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('child_list')
        else:
            form = ChildModelForm()
        return render(request, 'app2/child_form.html', {'form': form})

    def child_update(request, pk):
        child = get_object_or_404(ChildModel, pk=pk)
        if request.method == "POST":
            form = ChildModelForm(request.POST, instance=child)
            if form.is_valid():
                form.save()
                return redirect('child_list')
        else:
            form = ChildModelForm(instance=child)
        return render(request, 'app2/child_form.html', {'form': form})

    def child_delete(request, pk):
        child = get_object_or_404(ChildModel, pk=pk)
        if request.method == "POST":
            child.delete()
            return redirect('child_list')
        return render(request, 'app2/child_confirm_delete.html', {'child': child})
    ```

### 7. Configurar las URLs

1. En `mysite/urls.py`, configura las rutas:
    ```python
    from django.contrib import admin
    from django.urls import path
    from app2 import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.child_list, name='child_list'),
        path('child/<int:pk>/', views.child_detail, name='child_detail'),
        path('child/create/', views.child_create, name='child_create'),
        path('child/<int:pk>/update/', views.child_update, name='child_update'),
        path('child/<int:pk>/delete/', views.child_delete, name='child_delete'),
    ]
    ```

### 8. Crear Plantillas HTML

1. Crea las plantillas en `app2/templates/app2/`:
    - `child_list.html`
    - `child_detail.html`
    - `child_form.html`
    - `child_confirm_delete.html`

   Cada archivo ya está implementado en el proyecto.

### 9. Correr el Proyecto

1. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
2. Abre el navegador y accede a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

### 10. Ingresar Datos desde el Shell

1. Accede al shell de Django:
    ```bash
    python manage.py shell
    ```
2. Crea objetos en las tablas:
    ```python
    from app1.models import ParentModel
    from app2.models import ChildModel

    parent = ParentModel.objects.create(name="Parent Example")
    child = ChildModel.objects.create(parent=parent, description="Child Description Example")
    ```
3. Verifica los datos:
    ```python
    print(ParentModel.objects.all())
    print(ChildModel.objects.all())
    ```
