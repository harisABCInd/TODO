from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskStatusUpdateView, TaskViewSet
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', TaskViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('status/<int:pk>/', TaskStatusUpdateView.as_view(), name='task_status_update')
]