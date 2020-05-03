import os, json

def get_recipes():
    json_files = [file for file in os.listdir('./recipes') if file.endswith('.json')]
    recipes = []
    for file in json_files:
        with open('./recipes/' + file, 'r') as fd:
            recipes.append(json.load(fd))
    return recipes


def main():
    recipes = get_recipes()
    for recipe in recipes:
        print(recipe['name'])

if __name__ == "__main__":
    main()