from django.shortcuts import render
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
    return render(request,"contact.html")


def about(request):
    return render(request,"about.html")
