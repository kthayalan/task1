from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from mixer.backend.django import mixer
from django.urls import reverse
from Authentication.models import User
from AddressComponent.models import State, Locality, Postcode, LocalPostalCode, Street, Address


class UserAddressTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user_address', kwargs={'id': 2})
        # self.state1 = mixer.blend(State)
        # self.locality = mixer.blend(Locality)
        # self.postcode = mixer.blend(Postcode)
        # self.localPostalCode = mixer.blend(LocalPostalCode)
        # self.street = mixer.blend(Street)
        # self.address = mixer.blend(Address)
        # self.user1 = mixer.blend(User, username='thayaTest')

        self.state1 = State.objects.create(code=101010, name='Eastern', country='Srilanka')
        self.locality1 = Locality.objects.create(code=695558, name='Milagiriya', state=self.state1)
        self.postcode1 = Postcode.objects.create(code=30378, state=self.state1)
        self.localPostalCode1 = LocalPostalCode.objects.create(name='mila', locality=self.locality1, postcode=50989)
        self.street1 = Street.objects.create(name='main street', local_postal_code=self.localPostalCode1)
        self.address1 = Address.objects.create(no=50, address_1='3/1, milagiriya avenue', street=self.street1)
        self.user1 = User.objects.create(id=1, username='thaya', address=self.address1)

        self.state2 = State.objects.create(code=202020, name='california', country='USA')
        self.locality2 = Locality.objects.create(code=785669, name='heriys', state=self.state2)
        self.postcode2 = Postcode.objects.create(code=89895, state=self.state2)
        self.localPostalCode2 = LocalPostalCode.objects.create(name='yorks', locality=self.locality2, postcode=228879)
        self.street2 = Street.objects.create(name='malicarfi street', local_postal_code=self.localPostalCode2)
        self.address2 = Address.objects.create(no=210, address_1='51, kavinth apartment road', street=self.street2)
        self.user2 = User.objects.create(id=2, email='nishan@test.com', username='nisha', address=self.address2)

    def test_user_address_get(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['User address info']['username'] == 'nisha'
        assert response.data['User address info']['address']['street']['name'] == 'malicarfi street'
        # print('data: ', response.data)
        # print('json: ', response.json()['User address info'], response.json()['country'])

    def test_user_address_patch(self):
        data = {
            "address": {
                "no": 76,
                "address_1": "thayalan new road",
                "street": {
                    "name": "thaya new street"
                }
            }
        }
        response = self.client.patch(self.url, data=data, content_type="application/json")
        #print(response.data['Address updated']['address']['street']['name'] == 'thaya new street')
        #print('Response data', response.data)
        print('json: ', response.json())

