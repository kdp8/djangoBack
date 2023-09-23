from rest_framework.generics import ListAPIView
from .models import Actor
from .serializers import ActorSerializer

class ActorListAPIView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

