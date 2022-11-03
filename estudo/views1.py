from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CrusoSerializer, AvaliacaoSerializer
from rest_framework import status

class CursoAPIView(APIView):
    """Teste"""
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CrusoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CrusoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AvaliacaoAPIView(APIView):
    def get(self, request):
        avaliacoes = Avaliacao.objcts.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)