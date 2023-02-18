from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import car_hire


class TestCarsAppUrls(SimpleTestCase):
    """
    For testing the resolution of the urls in cars app.
    """

    def test_carhire_page_url_is_resolved(self):

        """
        For testing the resolution of the car hire page url
        """

        url = reverse('carhire')
        self.assertEquals(resolve(url).func, car_hire)
