from rest_framework.routers import DefaultRouter
from .api import *

router = DefaultRouter()
router.register('test', TestViewSet, 'Test')
router.register('test-partition', TestPartitionViewSet, 'TestPartition')
router.register('test-question', TestQuestionsViewSet, 'TestQuestion')
router.register('student-test', StudentTestViewSet, 'StudentTest')
router.register('student-question', StudentQuestionViewSet, 'StudentQuestion')
router.register('student-question-option',
                StudentQuestionOptionViewSet, 'StudentQuestionOption')


urlpatterns = router.urls
