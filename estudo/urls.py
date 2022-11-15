from django.urls import path
from .views import CursoAPIView, AvaliacaoAPIView, AvaliacoesAPIView, CursosAPIView

urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'), #Mostrar e criar
    path('curso/<int:pk>', CursoAPIView.as_view(), name='curso'), #selecionar para deleter ou update
    path('curso/<int:curso_pk>/avaliacoes', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('curso/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacao/<int:pk>', AvaliacaoAPIView.as_view(), name='avaliacao'),
]