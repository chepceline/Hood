from django.test import TestCase
from .models import Neighborhood, Gender, Profile, PostType, Post, Business

# Create your tests here.

class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.name=Neighborhood(name='kalimoni', location='juja', description='good neighborhood', manager_name='Harley', manager_number='0701234567', manager_email='harley@gmail.com', hospital_name='kalimoni', hospital_number='0701234567', hospital_email='kdhs@gmail.com', police_name='kalimoni police station', police_number='0701234567', police_email='kps@gmail.com', hood_pic='image')

    def test_instance(self):
        self.assertTrue(isinstance(self.name,Neighborhood))  

    def test_create_method(self):
        self.name.create_neighborhood()
        neighborhood=Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0) 

    def test_delete_method(self):
        self.name.create_neighborhood()
        self.name.delete()
        neighborhoods=Neighborhood.objects.all()
        self.assertTrue(len(neighborhoods) == 0) 


class ProfileTestClass(TestCase):
    def setUp(self):
        self.user=Profile(user='Faith', house='254', phase='3', phone='0701234567', gender='femele/male', profile_pic='image', neighborhood='kalimoni', )

    def test_instance(self):
        self.assertTrue(isinstance(self.user,Profile))    




