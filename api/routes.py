
from api import db, app
from api.models import Recipe
from flask import request






@app.route('/recipe', methods=['POST'])
def create_recipe():
  data = request.json
  recipe = Recipe(name=data['name'], ingr=data['ingr'], inst=data['inst'], rate=data['rate'], star=data['star'])
  db.session.add(recipe)
  db.session.commit()
  return { 'id': recipe.id }




@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipe = Recipe.query.all()
    return {'recipe': [format_recipe(i) for i in recipe]}



@app.route('/recipe/<int:id>', methods=['PUT'])
def update_recipe(id):
  recipe = Recipe.query.get(id)
  data = request.json
  recipe.name = data['name']
  recipe.ingr = data['ingr']
  recipe.inst = data['inst']
  recipe.rate = data['rate']
  recipe.star = data['star']
  db.session.commit()
  return { 'success': True }

@app.route('/recipe/<int:id>', methods=['DELETE'])
def delete_recipe(id):
  recipe = Recipe.query.get(id)
  db.session.delete(recipe)
  db.session.commit()
  return { 'success': True }




def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingr': recipe.ingr,
        'inst': recipe.inst,
        'rate': recipe.rate,
        'star':recipe.star,
        
    }
