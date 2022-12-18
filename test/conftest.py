import pytest
from api.models import Recipe
from api import db, app
@pytest.fixture
def  testing_client(scope='module'):
    """
    GIVEN a Flask application
    WHEN a new Recipe is created via the API
    THEN check the response contains the new Recipe's id
    """
    db.create_all()
    recipe = Recipe('Pumpkin Pie', 'pumpkin, sugar, salt, butter, pie crust', 'Preheat oven to 425 degrees F (220 degrees C). Mix pumpkin, sugar, salt, and butter together in a bowl. Pour into pie crust. Bake in preheated oven until a knife inserted near the center comes out clean, about 1 hour.')
    db.session.add(recipe)
    db.session.commit()
    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()