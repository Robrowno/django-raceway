from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    track_day_list,
    track_day_detail,
    track_day_request,
    experiences,
    experiences_detail,
    tuition,
    tuition_detail)


class TestTrackdayAppUrls(SimpleTestCase):
    """
    For testing the resolution of the urls in trackdays app.
    """

    def test_trackday_list_page_url_is_resolved(self):
        """
        For testing the resolution of the trackday list page url
        """

        url = reverse('trackdays')
        self.assertEquals(resolve(url).func, track_day_list)

    def test_trackday_detail_url_is_resolved(self):
        """
        For testing the resolution of the trackday booking url
        """
        id_x = int()

        url = reverse('booking', args=[id_x])
        self.assertEquals(resolve(url).func, track_day_detail)

    def test_trackday_request_url_is_resolved(self):
        """
        For testing the resolution of the trackday request url
        """

        url = reverse('request')
        self.assertEquals(resolve(url).func, track_day_request)

    def test_experiences_page_url_is_resolved(self):
        """
        For testing the resolution of the experiences list page url
        """

        url = reverse('experiences')
        self.assertEquals(resolve(url).func, experiences)

    def test_tuition_page_url_is_resolved(self):
        """
        For testing the resolution of the tuition courses page url
        """

        url = reverse('tuition')
        self.assertEquals(resolve(url).func, tuition)

    def test_experiences_detail_url_is_resolved(self):
        """
        For testing the resolution of the experiences detail url
        """
        id_x = int()

        url = reverse('exp_detail', args=[id_x])
        self.assertEquals(resolve(url).func, experiences_detail)

    def test_tuition_detail_url_is_resolved(self):
        """
        For testing the resolution of the tuition detail url
        """
        id_x = int()

        url = reverse('tuition_detail', args=[id_x])
        self.assertEquals(resolve(url).func, tuition_detail)
