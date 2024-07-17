from rest_framework import serializers
from .models import course
class Courseserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = course
        fields = ('id','url', 'course_name','course_id')