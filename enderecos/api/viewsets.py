from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializer import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
