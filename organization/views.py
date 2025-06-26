from .models import *
from .serializers import *
from .permissions import *
from rest_framework import viewsets,generics
from rest_framework.permissions import AllowAny

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [IsOrganizationAdminOrReadOnly]

    def get_queryset(self):
        return Organization.objects.filter(admin=self.request.user)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)
        
class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    permission_classes = [IsAdminOfOrganization]

    def get_queryset(self):
        if hasattr(self.request.user, 'member'):
            return Member.objects.filter(organization=self.request.user.member.organization)
        return Member.objects.filter(organization__admin=self.request.user)

    def perform_create(self, serializer):
        if self.request.user:
            serializer.save()


