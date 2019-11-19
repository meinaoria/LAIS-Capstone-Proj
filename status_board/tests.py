from django.test import TestCase, Client
from status_board.views import home, update, updateSys
from django.urls import reverse, resolve 
from status_board.models import *
from status_board.forms import *
from datetime import datetime
# Create your tests here.

class TestUrls(TestCase):

    def test_home_url_resolves(self):
        url = reverse('status-board-home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)
    
    def test_updateSys_url_resolves(self):
        url = url = reverse('updateSys')
        print(resolve(url))
        self.assertEquals(resolve(url).func, updateSys)
    
    def test_update_url_resolves(self):
        url = reverse('update', kwargs={'id': '2', 'sys': 'elev'})
        print(resolve(url))
        self.assertEquals(resolve(url).func, update)

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_updateSys(self):

        Elevators.objects.create(
            elevatorID = '1A',
            elevatorTableID = 1,
            Elevator_Status_Choice = 'GREEN',
            updated = datetime.now()
        )

        response = self.client.post(reverse('updateSys'),{
            'system': 'elev',
            'ID': '1A',
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'status_board/ModalForms.html' )

        # response = self.client.post(reverse('updateSys'),{
        #     'system': 'bridge',
        #     'ID': '2',
        # })

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'status_board/ModalForms.html' )

    def test_home(self):
        response = self.client.get(reverse('status-board-home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'status_board/home.html')
    
    #def test_update(self):

    #      Elevators.objects.create(
    #         elevatorID = '2',
    #         elevatorTableID = 1,
    #         Elevator_Status_Choice = 'YELLOW',
    #         updated = datetime.now()
    #     )

    #     # response = self.client.post(reverse('update', kwargs={'id': '2', 'sys': 'elev',}),{

    #   kboioni  response = self.client.post(reverse('updateSys'),{
    #         'system': 'bridge',
    #         'ID': '2',
    #     })
       
        
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'status_board/form_saved.html' )

class TestForms(TestCase):

    def test_elevator_form_valid_data(self):

        form = elevatorForm(data={
            'Elevator_Status_Choice':'GREEN'
        })

        self.assertTrue(form.is_valid())