from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertTrue(view.func, views.category)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'

        # need a recipe for this test
        self.make_recipe(title=needed_title)

        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        # check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_category_template_dont_load_recipes_not_published(self):
        # need a recipe for this test
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse(
                'recipes:category',
                kwargs={'category_id': recipe.id}
            )
        )

        # check if one recipe exists
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_views_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)
