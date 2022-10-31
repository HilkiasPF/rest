from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CrusoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):

    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CrusoSerializer(cursos, many=True)
        return Response(serializer.data)

class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objcts.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)