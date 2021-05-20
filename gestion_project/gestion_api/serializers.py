from rest_framework import serializers
from .models import UserProfile
from django.utils.timezone import now


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'name', 'surname', 'password', 'date']

    """ Serializar campo, como crear un formulario """
    date = serializers.DateTimeField(default=now())
    password = serializers.CharField(max_length=128, default="")
