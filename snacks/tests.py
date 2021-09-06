from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from snacks.models import Snack

class SnackModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_snack = Snack.objects.create(
            author = test_user,
            title = 'Name of Snack',
            body = "A fajita, in Tex-Mex cuisine, is any stripped grilled meat with stripped peppers and onions that is usually served on a flour or corn tortilla. The term originally referred to skirt steak, the cut of beef first used in the dish."
        )
        test_snack.save()

    def test_blog_content(self):
        snack = Snack.objects.get(id=1)

        self.assertEqual(str(snack.author), 'tester')
        self.assertEqual(snack.title, 'Name of Snack')
        self.assertEqual(snack.body, "A fajita, in Tex-Mex cuisine, is any stripped grilled meat with stripped peppers and onions that is usually served on a flour or corn tortilla. The term originally referred to skirt steak, the cut of beef first used in the dish.")

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('Snacks_list'))
        self.assertEqual(response.status_code, 403)






















    # def test_detail(self):

    #     test_user = get_user_model().objects.create_user(username='tester',password='pass')
    #     test_user.save()

    #     test_snack = Snack.objects.create(
    #         author = test_user,
    #         title = 'Title of Blog',
    #         body = 'Words about the blog'
    #     )
    #     test_snack.save()

    #     response = self.client.get(reverse('Snacks_detail', args=[1]))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, {
    #         'id':1,
    #         'title': test_snack.title,
    #         'body': test_snack.body,
    #         'author': test_user.id,
    #     })


    # def test_create(self):
    #     test_user = get_user_model().objects.create_user(username='tester',password='pass')
    #     test_user.save()

    #     url = reverse('Snacks_list')
    #     data = {
    #         "title":"Testing is Fun!!!",
    #         "body":"when the right tools are available",
    #         "author":test_user.id,
    #     }

    #     response = self.client.post(url, data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

    #     self.assertEqual(Snack.objects.count(), 1)
    #     self.assertEqual(Snack.objects.get().title, data['title'])

    # def test_update(self):
    #     test_user = get_user_model().objects.create_user(username='tester',password='pass')
    #     test_user.save()

    #     test_snack = Snack.objects.create(
    #         author = test_user,
    #         title = 'Title of Blog',
    #         body = 'Words about the blog'
    #     )

    #     test_snack.save()

    #     url = reverse('Snacks_detail',args=[test_snack.id])
    #     data = {
    #         "title":"Testing is Still Fun!!!",
    #         "author":test_snack.author.id,
    #         "body":test_snack.body,
    #     }

    #     response = self.client.put(url, data, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_200_OK, url)

    #     self.assertEqual(Snack.objects.count(), test_snack.id)
    #     self.assertEqual(Snack.objects.get().title, data['title'])


    # def test_delete(self):
    #     """Test the api can delete a snack."""

    #     test_user = get_user_model().objects.create_user(username='tester',password='pass')
    #     test_user.save()

    #     test_snack = Snack.objects.create(
    #         author = test_user,
    #         title = 'Title of Blog',
    #         body = 'Words about the blog'
    #     )

    #     test_snack.save()

    #     snack = Snack.objects.get()

    #     url = reverse('Snacks_detail', kwargs={'pk': snack.id})


    #     response = self.client.delete(url)

    #     self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)