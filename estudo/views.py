"""Nova views usando generics"""

from rest_framework import generics

from .models import Curso, Avaliacao
from .serializers import CrusoSerializer, AvaliacaoSerializer

class CursoAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CrusoSerializer

class AvaliacaoAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
