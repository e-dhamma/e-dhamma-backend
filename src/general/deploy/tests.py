from django.test import TestCase
from django.urls import resolve
from django.conf import settings
from .views import deploy

class DeployViewTest(TestCase):

    def test_deploy_view(self):
        found = resolve(f'/deploy/{settings.DEPLOY_KEY}/')
        self.assertEqual(found.func, deploy)