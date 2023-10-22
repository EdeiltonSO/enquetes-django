from django.http import HttpResponse
from .models import Pergunta
from django.shortcuts import render
from django.http import Http404

def listar(request):
    ultimas = Pergunta.objects.order_by('-data_pub')[:3]
    context = {'perguntas_list': ultimas}
    return render(request, 'enquetes/index.html', context)

def detalhar(request, question_id):
    try:
        p = Pergunta.objects.get(pk=question_id)
    except Pergunta.DoesNotExist:
        raise Http404("Essa pergunta não existe!")
    return render(request, 'enquetes/detalhar.html', {'pergunta': p})

def resultados(request, question_id):
    response = "Você está visualizando os resultados da pergunta %s."
    return HttpResponse(response % question_id)

def votar(request, question_id):
    return HttpResponse("Você votou na pergunta %s." % question_id)
