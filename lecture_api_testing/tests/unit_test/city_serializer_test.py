from rest_framework.test import APISimpleTestCase
from lecture_api_testing.serializers import CitySerializer


# https://www.vinta.com.br/blog/how-i-test-my-drf-serializers

# APISimpleTestCase (doesn't work with db)
class CitySerializerTest(APISimpleTestCase):

    def setUp(self):
        print('Setup here')

    def test_serializer_valid(self):
        data = {'name': 'Test Serializer', 'population': 109090}
        serializer = CitySerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid(self):
        data = {'code': 'Test Serializer'}
        serializer = CitySerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_read(self):
        name = 'Test Serializer'
        population = 109090
        data = {'name': name, 'population': population}
        serializer = CitySerializer(data=data)
        serializer.is_valid()

        self.assertEqual(name, serializer.validated_data['name'])
        self.assertEqual(population, serializer.validated_data['population'])
    #
    # def test_serializer_write(self):
    #     data = {'name': 'Test Serializer'}
    #     serializer = CitySerializer(data=data)
    #     self.assertTrue(serializer.is_valid())
