from rest_framework import serializers
from .models import SleepDiary

class SleepDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SleepDiary
        fields = '__all__'