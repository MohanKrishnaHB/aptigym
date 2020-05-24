from rest_framework.routers import DefaultRouter
from .api import QuestionViewSet, OptionsViewSet, Category1ViewSet, Category2ViewSet

router = DefaultRouter()

router.register('question', QuestionViewSet, 'question')
router.register('option', OptionsViewSet, 'options')
router.register('category1', Category1ViewSet, 'category1')
router.register('category2', Category2ViewSet, 'category2')


urlpatterns = router.urls
