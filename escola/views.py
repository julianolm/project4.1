from rest_framework import viewsets
from escola.serializers import AlunoSerializer
from escola.models import Aluno


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer