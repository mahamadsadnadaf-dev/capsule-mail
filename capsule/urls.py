from rest_framework.routers import DefaultRouter
from .views import LetterViewSet, RegistrationPoint
from django.urls import path

router = DefaultRouter()
router.register(r'letters',LetterViewSet, basename='letter')
urlpatterns = router.urls + [
    path('register/', RegistrationPoint.as_view(), name='register')
]