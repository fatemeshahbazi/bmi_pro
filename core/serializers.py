from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import BmiMeasurement

from accounts.serializers import UserRegisterSerializer


class BmiSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer(read_only=True)
    previous_status = serializers.SerializerMethodField()
    bmi = serializers.FloatField(read_only=True)

    class Meta:
        model = BmiMeasurement
        fields = ('user', 'height', 'weight', 'bmi', 'previous_status', 'result')
        extra_kwargs = {
            'bmi': {'read_only': True},
            'result': {'read_only': True}
        }

    def validate_weight(self, value):
        if value > 0:
            weight = float(value)
            return weight
        raise ValidationError('weight is not valid')

    def validate_height(self, value):
        if value > 0:
            height = float(value)
            return height
        raise ValidationError('height is not valid')

    def get_previous_status(self, obj):

        print(obj)
        print('hhhhhhhhhhhhhhh')
        if float(obj.bmi) >= 30:
            return self.get_delta_weight(round(float(obj.bmi) - 30, 2), obj.height)
        elif float(obj.bmi) <= 18.5:
            return f'You are underweight'
        elif float(obj.bmi) >= 24.9:
            return self.get_delta_weight(round(float(obj.bmi) - 24.9, 2), obj.height)
        return self.get_delta_weight(round(float(obj.bmi) - 18.5, 2), obj.height)

    @staticmethod
    def get_delta_weight(delta_bmi, height):
        return round(delta_bmi * height ** 2, 2)
