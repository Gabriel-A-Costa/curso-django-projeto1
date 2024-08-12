from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):

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

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=<teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;teste&gt;&quot',
            response.content.decode('utf-8')
        )
