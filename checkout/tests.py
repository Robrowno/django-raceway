from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import basket


class TestCheckoutAppUrls(SimpleTestCase):
    """
    For testing the resolution of the urls in checkout app.
    """

    def test_basket_page_url_is_resolved(self):

        """
        For testing the resolution of the basket page url
        """

        url = reverse('my_basket')
        self.assertEquals(resolve(url).func, basket)
