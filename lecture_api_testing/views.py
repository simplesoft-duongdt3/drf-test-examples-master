from rest_framework import views, viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import City, School, Student
from .serializers import CitySerializer, SchoolSerializer, StudentSerializer
from lecture_api_testing.util import get_qr_code_url_other_file

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def get_qr_code_url(user_id: int):
    return 'https://myqr.com/000.png'


class UserViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        qr_code_url = get_qr_code_url(user_id=pk)
        return Response({
            'result': 1,
            "data": {
                'id': pk,
                "name": "Doan Thanh Duong",
                "qr_code_url": qr_code_url,
            }
        })


class User2ViewSet(viewsets.ViewSet):
    def get_qr_code_url2(self, user_id: int):
        return 'https://myqr.com/000.png'

    def retrieve(self, request, pk=None):
        qr_code_url = self.get_qr_code_url2(user_id=pk)
        return Response({
            'result': 1,
            "data": {
                'id': pk,
                "name": "Doan Thanh Duong",
                "qr_code_url": qr_code_url,
            }
        })

class User3ViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        qr_code_url = get_qr_code_url_other_file(user_id=pk)
        return Response({
            'result': 1,
            "data": {
                'id': pk,
                "name": "Doan Thanh Duong",
                "qr_code_url": qr_code_url,
            }
        })