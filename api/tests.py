from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from gwt.models import SurveyData
from api.auth import jwt_create_token

class SurveyTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser('super', 'super@gmail.com', 'password')
        cls.user = User.objects.create_user('user', 'user@gmail.com', 'password')
        cls.empty_survey = SurveyData.objects.create(user=cls.superuser,project='EmptyProject',location=Point(4.5, 52.0),survey='{}')
        cls.survey1 = SurveyData.objects.create(user=cls.superuser,project='TestProject',location=Point(4.5, 52.0),survey='{"question":"answer"}')
        cls.token = jwt_create_token(cls.user)
        
    def get_list(self,token=None):
        headers = {'Authorization': 'JWT '+token} if token else None
        return self.client.get('/api/v1/survey/',headers=headers)
    
    def get_survey(self, id):
        return self.client.get('/api/v1/survey/{}/'.format(id))

    def get_token(self, username, password):
        return self.client.post('/api/v1/login/',data={'username': username, 'password': password})
                     
    def post_survey(self, survey):
        return self.client.post('/api/v1/survey/',data=survey)

    def test_not_authorized(self):
        response = self.get_list()
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)    
    
    def test_get_list(self):
        response = self.get_token('user','password')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        token = response.data.get('token')
        response = self.get_list(token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)