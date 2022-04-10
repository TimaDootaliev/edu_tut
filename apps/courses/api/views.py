from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action

from ..models import Course, Subject
from .serializers import CourseSerializer, SubjectSerializer


class SubjectListView(ListAPIView):
    """ Get List Of Subjects """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(RetrieveAPIView):
    """ Get Detail Of Subjects """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


# class CourseEnrollView(APIView):
#     """ Enroll A User In A Course """
#     authentication_classes = (BasicAuthentication, )
#     permission_classes = (IsAuthenticated, )

#     def post(self, request, pk, format=None):
#         course = get_object_or_404(Course, pk=pk)
#         print(course)
#         course.students.add(request.user)
#         return Response({'enrolled': True})


class CourseViewSet(ReadOnlyModelViewSet):
    """ ViewSet Including List, Detail, Enroll, Reviews """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(methods=['post'], 
            authentication_classes=[BasicAuthentication], 
            permission_classes=[IsAuthenticated], detail=True)
    def enroll(self, request, pk):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

