from rest_framework_nested import routers
from django.urls import re_path, include
from .views import TrackViewSet, QuestionViewSet, ChoiceViewSet


track_router = routers.SimpleRouter()
track_router.register(r"tracks", TrackViewSet)

question_router = routers.NestedSimpleRouter(track_router, r"tracks", lookup="track")
question_router.register(r"questions", QuestionViewSet, base_name="track_questions")

choice_router = routers.NestedSimpleRouter(question_router, r"questions", lookup="question")
choice_router.register(r"choices", ChoiceViewSet, base_name="track_question_choices")

urlpatterns = [
	re_path(r"^", include(track_router.urls)),
	re_path(r"^", include(question_router.urls)),
	re_path(r"^", include(choice_router.urls)),
]