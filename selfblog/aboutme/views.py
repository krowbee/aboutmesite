from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import AboutWork,MySkill
from .serializers import AboutWorkSerializer,MySkillSerializer
# Create your views here.

class AboutWorkView(ModelViewSet):
    queryset = AboutWork.objects.all()
    serializer_class=AboutWorkSerializer

class MySkillView(ModelViewSet):
    queryset = MySkill.objects.all()
    serializer_class=MySkillSerializer