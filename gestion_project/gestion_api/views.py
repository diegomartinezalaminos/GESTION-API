from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework import viewsets


# Create your views here.
class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
