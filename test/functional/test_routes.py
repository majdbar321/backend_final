from api import app
import pytest

def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN a POST request is made to the '/recipe' URL with the recipe data
    THEN check the response contains the id of the created recipe
    """
    response = testing_client.post('/recipe', json={
        'name': 'Chocolate Chip Cookies',
        'ingr': 'flour, baking soda, salt, butter, sugar, brown sugar, eggs, vanilla extract, chocolate chips',
        'inst': 'Preheat the oven to 350 degrees F (175 degrees C). In a medium bowl, whisk together the flour, baking soda, and salt. In a separate large bowl, cream together the butter, sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Gradually add the dry ingredients to the wet ingredients and mix until just combined. Stir in the chocolate chips. Drop the dough by rounded spoonfuls onto ungreased baking sheets. Bake for 8-10 minutes, or until the edges are lightly golden. Allow the cookies to cool on the baking sheet for a few minutes before transferring to a wire rack to cool completely.'
    })
    assert response.status_code == 200

def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN a GET request is made to the '/recipe/' URL with an id of an existing recipe
    THEN check the response contains the details of the recipe
    """
    response = testing_client.get('/recipe')
    assert response.status_code == 200
   
def test_get_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN a GET request is made to the '/recipe/<id>' URL with an id of an existing recipe
    THEN check the response contains the details of the recipe
    """
    response = testing_client.get('/recipe/1')
    assert response.status_code == 200
    assert response.json == {
        'id' : 1,
        'name': 'Chocolate Chip Cookies',
        'ingr': 'flour, baking soda, salt, butter, sugar, brown sugar, eggs, vanilla extract, chocolate chips',
        'inst': 'Preheat the oven to 350 degrees F (175 degrees C). In a medium bowl, whisk together the flour, baking soda, and salt. In a separate large bowl, cream together the butter, sugar, and brown sugar until smooth. Beat in the eggs one at a time, then stir in the vanilla. Gradually add the dry ingredients to the wet ingredients and mix until just combined. Stir in the chocolate chips. Drop the dough by rounded spoonfuls onto ungreased baking sheets. Bake for 8-10 minutes, or until the edges are lightly golden. Allow the cookies to cool on the baking sheet for a few minutes before transferring to a wire rack to cool completely.'
    }

