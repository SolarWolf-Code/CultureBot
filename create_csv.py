import requests

def get_nested_value(dictionary, *keys):
    """
    Retrieve a value from a nested dictionary using a variable number of keys.

    Args:
        dictionary (dict): The dictionary to search in.
        *keys: Variable number of keys to access the nested values.

    Returns:
        The retrieved value if the keys exist, or None if any key is not found.
    """
    try:
        for key in keys:
            dictionary = dictionary[key]
        if type(dictionary) == list:
            dictionary = dictionary[0]
        dictionary = str(dictionary).replace(",", "")
        return dictionary
    except (KeyError, TypeError):
        return None

def create_country_csv():
    # create a csv file with the following columns:
    # name, capital, subregion, population, flag
    req = requests.get('https://restcountries.com/v3.1/all')

    countries = req.json()
    print(len(countries))
    # h1 | name (common)
    # h3 | capital [0]
    # h3 | subregion
    # h3 | population
    # embed | flag (flags["png"])

    with open('countries.csv', 'w') as file:
        file.write('name, capital, subregion, population, flag\n')
        for country in countries:
            name = get_nested_value(country, 'name', 'common')
            capital = get_nested_value(country, 'capital')
            subregion = get_nested_value(country, 'subregion')
            population = get_nested_value(country, 'population')
            flag = get_nested_value(country, 'flags', 'png')
            file.write(f'{name}, {capital}, {subregion}, {population}, {flag}\n')

if __name__ == '__main__':
    create_country_csv()