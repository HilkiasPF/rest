from rest_framework import serializers

from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = {
            'id',
            'curso',
            'none',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        }