from rest_framework.routers import DefaultRouter
from student.api import StudentViewSet

router = DefaultRouter()
router.register('student', StudentViewSet, 'student')

urlpatterns = router.urls
