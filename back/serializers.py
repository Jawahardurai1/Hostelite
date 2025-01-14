from rest_framework import serializers
from .models import outing,outpass,feedback
class outingserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models=outing
        fields=('name','plfno','date','time','reason')
class outpassserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models=outpass
        fields=('name','plfno','date','time','reason')
class feedbackserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models=feedback
        fields=('name','plfno','description')