from django.http import HttpResponse

def listar(request):
    return HttpResponse("Aqui aparecerá a lista de enquetes")

def detalhar(request, question_id):
    return HttpResponse("Você está votando na pergunta %s." % question_id)

def resultados(request, question_id):
    response = "Você está visualizando os resultados da pergunta %s."
    return HttpResponse(response % question_id)

def votar(request, question_id):
    return HttpResponse("Você votou na pergunta %s." % question_id)
