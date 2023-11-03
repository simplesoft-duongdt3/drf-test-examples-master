from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APITransactionTestCase
from rest_framework.test import APIRequestFactory

from lecture_api_testing.models import City, School, Student
from lecture_api_testing.factories import CityFactory, SchoolFactory, StudentFactory
from lecture_api_testing.views import CityViewSet, SchoolViewSet, StudentViewSet


# APITestCase (allows to work with db)
class TestCaseForCity(APITestCase):

    # Testing via request factory
    def test_get_city_request_factory(self):
        city = CityFactory(name="Test", population=1)
        request_factory = APIRequestFactory()
        request = request_factory.get("/api/cities/")
        city_view = CityViewSet.as_view({"get": "list"})
        response = city_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_city_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.post(
            "/api/cities/", {"name": "Test", "population": 1}, format="json"
        )
        city_view = CityViewSet.as_view({"post": "create"})
        response = city_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Testing via api client
    def test_get_city_api_client(self):
        city = CityFactory(name="Test", population=1)
        response = self.client.get("/api/cities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_city_api_client(self):
        response = self.client.post(
            "/api/cities/", data={"name": "Test", "population": 1}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Will fail
    def test_transactional_case_for_city(self):
        CityFactory(name="Test", population=1)
        city = City.objects.first()
        city.set_population_to_zero()
        self.assertEqual(city.name, "Died")

    def test_users_api_client(self):
        response = self.client.get("/api/users/100/")

        expected_json = {'data': {'id': '100', 'name': 'Doan Thanh Duong', 'qr_code_url': 'https://myqr.com/000.png'}, 'result': 1}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, expected_json)

    def test_users_with_mock_qrcode_context_manager_api_client(self):
        mocked_qr_code_url = 'mocked_url_context_manager'

        with patch('lecture_api_testing.views.get_qr_code_url') as mock_get_qr_code_url:
            mock_get_qr_code_url.return_value = mocked_qr_code_url
            response = self.client.get("/api/users/100/")

            expected_json = {'data': {'id': '100', 'name': 'Doan Thanh Duong', 'qr_code_url': mocked_qr_code_url}, 'result': 1}

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertDictEqual(response.data, expected_json)

    @patch('lecture_api_testing.views.get_qr_code_url')
    def test_users_with_mock_qrcode_decorator_api_client(self, mock_get_qr_code_url):
        mocked_qr_code_url = 'mocked_url_decorator'
        mock_get_qr_code_url.return_value = mocked_qr_code_url

        response = self.client.get("/api/users/100/")

        expected_json = {'data': {'id': '100', 'name': 'Doan Thanh Duong', 'qr_code_url': mocked_qr_code_url}, 'result': 1}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, expected_json)


    @patch('lecture_api_testing.views.User2ViewSet.get_qr_code_url2')
    def test_users2_with_mock_qrcode_decorator_api_client(self, mock_get_qr_code_url):
        mocked_qr_code_url = 'mocked_url_decorator'
        mock_get_qr_code_url.return_value = mocked_qr_code_url

        response = self.client.get("/api/users2/100/")

        expected_json = {'data': {'id': '100', 'name': 'Doan Thanh Duong', 'qr_code_url': mocked_qr_code_url}, 'result': 1}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data, expected_json)


class TestCaseForCityWithTransaction(APITransactionTestCase):
    def test_transactional_case_for_city(self):
        CityFactory(name="Test", population=1)
        city = City.objects.first()
        city.set_population_to_zero()
        self.assertEqual(city.name, "Died")
