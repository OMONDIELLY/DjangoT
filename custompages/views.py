from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def page_view(request,*args,**kwargs):
    
    print(request.user)
    return render(request,"home.html",{})
#   return HttpResponse("<H1>Hello World</H1>") 
   
def about_view(request,*args,**kwargs):
    my_def = {
         "intro":"BriTech Solutions is a multidimensional ICT company",
         "services":"We develop solutions,and applications that fall under ICT",
         "include": ('web apps','ussd apps','data analysis','static sites','Network Admins')
    }
    return render(request,"about.html", my_def) 



def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})


def social_view(request,*args,**kwargs):
    return render(request,"social.html",{})