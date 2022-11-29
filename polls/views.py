from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola! estamos haciendo mi primer app de django.")



def prueba(request):
    return HttpResponse("Hola! estás en el método prueba.")
