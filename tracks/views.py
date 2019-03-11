from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from .serializers import TrackSerializer, QuestionSerializer, ChoiceSerializer
from .models import Track, Question, Choice
from rest_framework.decorators import action


class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(track=self.kwargs['track_pk'])

    def perform_create(self, serializer):
        track = get_object_or_404(Track, pk=self.kwargs['track_pk'])
        serializer.save(track=track)

    @action(methods=['get'], detail=True)
    def analysis(self, request, track_pk, pk):
        q = get_object_or_404(
            Question,
            track=track_pk,
            pk=pk
        )
        corrects = Choice.objects.filter(question=q, correct=True).aggregate(Sum('votes'))["votes__sum"]
        incorrects = Choice.objects.filter(question=q, correct=False).aggregate(Sum('votes'))["votes__sum"]
        return Response({"right": corrects, "wrong": incorrects})


class ChoiceViewSet(ModelViewSet):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        return Choice.objects.filter(
            question__track=self.kwargs['track_pk'],
            question=self.kwargs['question_pk']
        )

    def perform_create(self, serializer):
        question = get_object_or_404(
            Question,
            pk=self.kwargs['question_pk'],
            track=self.kwargs['track_pk']
        )
        serializer.save(question=question)

    @action(methods=['post'], detail=True)
    def votes(self, request, track_pk, question_pk, pk):
        choice = get_object_or_404(
            Choice,
            question__track=track_pk,
            question=question_pk,
            pk=pk
        )
        choice.votes += 1
        choice.save()
        return Response(ChoiceSerializer(choice).data)