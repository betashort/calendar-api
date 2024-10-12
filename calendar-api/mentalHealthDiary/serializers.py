from rest_framework import serializers
from .models import MentalHealthDirary

class MentalHealthDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MentalHealthDirary
        fields = '__all__'