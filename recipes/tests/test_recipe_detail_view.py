from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):
    def test_recipe_detail_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertTrue(view.func, views.recipe)

    def test_recipe_detail_views_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipe(self):
        needed_title = 'This is a detail page - It load one recipe'

        # need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')

        # check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_load_recipes_not_published(self):
        # need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:recipe',
                kwargs={'id': recipe.id}
            )
        )

        # check if one recipe exists
        self.assertEqual(response.status_code, 404)
