from rest_framework import serializers
from .models import BmiMeasurement

from accounts.serializers import UserSerializer


class BmiSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    result = serializers.SerializerMethodField(read_only=True)

    RESULT = {
        1: 'underweight',
        2: 'normal',
        3: 'overweight',
        4: 'obese'
    }

    class Meta:
        model = BmiMeasurement
        fields = ('user', 'height', 'weight', 'bmi', 'result')
        extra_kwargs = {
            'bmi': {'read_only': True},
        }

    def get_result(self, obj):
        return self.RESULT.get(obj.result)

    def previous_status(self, bmi, height):
        if float(bmi) >= 30:
            return f'You need to loose {self.get_delta_weight(round(float(bmi) - 30, 2), height)} kgs'
        elif float(bmi) <= 18.5:
            return f'You are underweight'
        elif float(bmi) >= 24.9:
            return f'You need to lose {self.get_delta_weight(round(float(bmi) - 24.9, 2), height)} kgs'
        return f'You need to lose {self.get_delta_weight(round(float(bmi) - 18.5, 2), height)} kgs'

    @staticmethod
    def get_delta_weight(delta_bmi, height):
        return round(delta_bmi * height ** 2, 2)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['previous_status'] = self.previous_status(instance.bmi, instance.height)
        return data
