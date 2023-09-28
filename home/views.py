from django.shortcuts import render
from home.email import  send_contact_email


# Create your views here.
def home(request):
    return render(request,"index.html",context={"name":"my name is chandra ojha"})
def index(request):
    print("REQUEST METHOD:",request.method)
    print("PARAMS:", request.GET)
    data = request.GET.dict()
    data = {"students":[
        {
            "name":"chandra ojha",
            "address":"ktm",
            "age":20,
            "course":"BSC CSIT"
        },
         {
            "name":"chandra ojha",
            "address":"ktm",
            "age":20,
            "course":"BSC CSIT"
        },
         {
            "name":"chandra ojha",
            "address":"ktm",
            "age":20,
            "course":"BSC CSIT"
        },
    ],"college":"KCT",}

    return render(request,"index.html",context=data)

def contact(request):
    if request.method == "GET":
     return render(request,"contact.html")
    else :
        data = request.POST
        print("data",data)
        send_contact_email(
            data.get("message"),
            data.get("email"),
            data.get("name"),
        )
        return render( request,"contact.html",{"message":"Thank you for contacting us"})


def about(request):
    return render(request,"about.html")

def handle_404(request):
    return render (request,"errors/4o4_error.html")

def handle_403(request):
    return render (request,"errors/4o3_error.html")

def handle_500(request):
    return render (request,"errors/500_error.html")
