from django.contrib.auth import get_user_model
from django.test import TestCase


class LoggedInTestCase(TestCase):

    def setUp(self):
        self.password = ''

        self.test_user = get_user_model().objects.create_user(
            username='',
            email='',
            password=self.password
        )

        # テスト用ユーザーでログイン
        self.client.login(email=self.test_user.email, password=self.test_user.password)


