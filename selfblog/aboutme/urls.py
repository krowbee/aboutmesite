

from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import AboutWorkView,MySkillView

router = SimpleRouter()
router.register("api/aboutwork",AboutWorkView)
router.register("api/myskill",MySkillView)

urlpatterns = [
    
] +router.urls
