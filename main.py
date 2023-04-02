def main_run():
    with open('recipes.txt', 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            recipe_name = line.strip()
            ingredients_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            file.readline()
            cook_book[recipe_name] = ingredients


if __name__ == '__main__':
    main_run()