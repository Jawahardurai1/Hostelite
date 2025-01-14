from rest_framework import viewsets
from .serializers import outingserializer,outpassserializer,feedbackserializer
from .models import outing,outpass,feedback
class outingview(viewsets.ModelViewSet):
    queryset=outing.objects.all()
    serializer_class=outingserializer
class outpassview(viewsets.ModelViewSet):
    query=outpass.objects.all()
    serializer_class=outpassserializer
class feedbackview(viewsets.ModelViewSet):
    queryset=feedback.objects.all()
    serializer_class=feedbackserializer
