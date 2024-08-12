from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Name'
        )
        return super().setUp()

    def test_recipe_category_model_string_representation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_recipe_category_model_max_length_is_65_chars(self):
        self.category.name = 'A' * 70
        with self.assertRaises(ValidationError):
            self.category.full_clean()