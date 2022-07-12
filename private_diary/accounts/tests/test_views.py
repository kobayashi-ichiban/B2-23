from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from private_diary.diary.models import Diary


class LoggedInTestCase(TestCase):

    def setUp(self):
        # テストユーザー1
        self.password = 'admin_diary'

        self.test_user = get_user_model().objects.create_user(
            # テストユーザー1
            username='admin',
            email='admin@sample.com',
            password=self.password
        )

        # テスト用ユーザーでログイン
        self.client.login(email=self.test_user.email, password=self.test_user.password)


class TestCreateDiaryView(LoggedInTestCase):
    """DiaryCreateViewのテスト"""
    def test_create_diary_success(self):
        """パラメータ"""
        params = {
            'title': 'CreateView',
            'content': 'CreateDocBody',
            'pref': '1',
            'photo1': '',
            'photo2': '',
            'photo3': '',
        }

        response = self.client.post(reverse_lazy('diary:diary_create'), params)
        self.assertRedirects(response, reverse_lazy('diary:diary_list'))
        self.assertEqual(Diary.objects.filter(title='CreateView').count(), 1)

    def test_create_diary_failure(self):
        response = self.client.post(reverse_lazy('diary:diary_create'))
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')


class TestUpdateDiaryView(LoggedInTestCase):
    """DiaryUpdateViewのテスト"""
    def test_update_diary_success(self):
        diary = Diary.objects.create(user=self.test_user, titlle='編集前')

        params = {
            'title': 'テスト編集'
        }
        response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk': diary.pk}), params)
        self.assertRedirects(response, reverse_lazy('diary:diary_detail', kwargs={'pk': diary.pk}))

        # 日記を編集したかを確認
        self.assertEqual(Diary.objects.get(pk=diary.pk).title, 'テスト編集')

    def test_update_diary_failure(self):
        response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, 404)
