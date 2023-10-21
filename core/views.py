from django.shortcuts import render, redirect
from .forms import NewForm, MessageForm
from .models import Product
from django.http import HttpResponseRedirect

def index(request):
    all_products = Product.objects.all
    return render(request, 'core/index.html',
                  {'products': all_products,}
                  )
 

def newitem(request):
    submitted = False
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/newitem?submitted=True')
    else:
        form = NewForm
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'core/newitem.html',
                  {'form': form,
                   'submitted': submitted,
                   }
                  )
    
def message(request):
    form = MessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
        return redirect('index')
    else:
        return render(request,'core/message.html',{'form':form})
    
def cart(request):
    return render(request, 'core/cart.html')