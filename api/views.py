from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializers


# Create your views here.
@extend_schema_view(
    list=extend_schema(description="Permite extraer lista de Usuarios"),
    retrieve=extend_schema(description='Permite obtener un usuario'),
    create=extend_schema(description='permite crear un usuario'),
    update=extend_schema(description='permite actualizar un usuario'),
    destroy=extend_schema(description='permite eliminar un usuario'),

)
class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
