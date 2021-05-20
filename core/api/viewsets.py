from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.http import HttpResponse
from core.models import PontoTuristico
from .serializer import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']
        ponto = PontoTuristico.objects.get(id=id)
        ponto.atracoes.set(atracoes)
        ponto.save()
        return HttpResponse('ok')
