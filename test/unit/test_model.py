from api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingr, inst, rate, is_star fields are defined correctly
    """
    recipe = Recipe('Chocolate Chip Cookies', 'flour, baking soda, salt, butter, sugar, brown sugar, eggs, vanilla extract, chocolate chips', 'Preheat the oven to 350 degrees F (175 degrees C). In a medium bowl, whisk together the flour, baking soda, and salt. In a separate large bowl, cream together the butter, sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Gradually add the dry ingredients to the wet ingredients and mix until just combined. Stir in the chocolate chips. Drop the dough by rounded spoonfuls onto ungreased baking sheets. Bake for 8-10 minutes, or until the edges are lightly golden. Allow the cookies to cool on the baking sheet for a few minutes before transferring to a wire rack to cool completely.')
    assert recipe.name == 'Chocolate Chip Cookies'
    assert recipe.ingr == 'flour, baking soda, salt, butter, sugar, brown sugar, eggs, vanilla extract, chocolate chips'
    assert recipe.inst == 'Preheat the oven to 350 degrees F (175 degrees C). In a medium bowl, whisk together the flour, baking soda, and salt. In a separate large bowl, cream together the butter, sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Gradually add the dry ingredients to the wet ingredients and mix until just combined. Stir in the chocolate chips. Drop the dough by rounded spoonfuls onto ungreased baking sheets. Bake for 8-10 minutes, or until the edges are lightly golden. Allow the cookies to cool on the baking sheet for a few minutes before transferring to a wire rack to cool completely.'