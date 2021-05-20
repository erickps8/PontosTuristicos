from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacao
from .serializer import AvaliacaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
