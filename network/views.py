from rest_framework import viewsets, permissions, filters
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer


class IsActiveStaff(permissions.BasePermission):
    """
    Разрешает доступ только активным сотрудникам
    (is_active=True и is_staff=True)
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_active
            and request.user.is_staff
        )


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveStaff]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveStaff]
