from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import profile, update_profile


class TestCarsAppUrls(SimpleTestCase):
    """
    For testing the resolution of the urls in profiles app.
    """

    def test_profile_page_url_is_resolved(self):
        """
        For testing the resolution of the profile page url
        """

        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_edit_profile_url_is_resolved(self):
        """
        For testing the resolution of the edit profile url
        """

        url = reverse('updateProfile')
        self.assertEquals(resolve(url).func, update_profile)
