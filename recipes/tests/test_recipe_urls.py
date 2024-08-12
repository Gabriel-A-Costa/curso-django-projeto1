from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeURLsTest(TestCase):

    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_recipe_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

    # recipes:search exist? if Yes, check if url is /recipes/search/
    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')

    # in recipes:search the func is iqual views.search?
    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    # check is template exist in response
    def test_recipe_search_loads_correct_templat(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    # test if search is valid or not
    def test_recipe_search_raises_404_if_no_search_term(self):
        # expected the value q=... in url
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
