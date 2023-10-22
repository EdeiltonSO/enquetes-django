from django.http import HttpResponse

def index(request):
    return HttpResponse("Aqui aparecerá a lista de enquetes")
