from rest_framework.serializers import ModelSerializer

from .models import AboutWork,MySkill

class AboutWorkSerializer(ModelSerializer):
    class Meta:
        model = AboutWork
        fields = '__all__'


class MySkillSerializer(ModelSerializer):
    class Meta:
        model = MySkill
        fields = '__all__'