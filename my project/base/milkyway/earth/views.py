from django.shortcuts import render
from .forms import UserForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
# Create your views here.
class Index(TemplateView):
    template_name = 'earth/index.html'

def contact(request):
    


    registered = False

    

        
    user_form = UserForm(data=request.POST)
        

        
    if user_form.is_valid() :     
        user = user_form.save()   
        user.set_password(user.password)    
        user.save()               
        registered = True

    else:
            
        print(user_form.errors)

    
        

    
    return render(request,'earth/contact.html',
                          {'user_form':user_form,'registered':registered})