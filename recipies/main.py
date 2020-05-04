import json
import os

import numpy as np
import pandas as pd


def get_recipes():
    json_files = [file for file in os.listdir('./recipes') if file.endswith('.json')]
    recipes = []
    for file in json_files:
        with open('./recipes/' + file, 'r') as fd:
            recipes.append(json.load(fd))
    return recipes


def create_dataframe(recipes):
    recipe_names = [recipe['name'] for recipe in recipes]
    ingredients = []
    for recipe in recipes:
        ingredients += recipe['ingredients'].keys()
    ingredients = list(set(ingredients))
    df = pd.DataFrame(columns=recipe_names, index=ingredients)
    for ingredient in ingredients:
        for recipe in recipes:
            ingred_info = recipe['ingredients'].get(ingredient)
            if ingred_info is not None:
                data = str(ingred_info['quantity']) + ' ' + ingred_info['unit']
            else:
                data = ""
            df.loc[ingredient][recipe['name']] = data
    return df


def main():
    recipes = get_recipes()
    df = create_dataframe(recipes)
    print(df)


if __name__ == "__main__":
    main()
