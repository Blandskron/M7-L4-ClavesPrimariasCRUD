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