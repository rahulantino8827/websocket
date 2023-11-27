from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from django.urls import path

# router = DefaultRouter()

# router.register("student",StudentViewSet, basename="student")

# urlpatterns = router.urls

urlpatterns = [
    path("student/", StudentViewSet.as_view())
]
