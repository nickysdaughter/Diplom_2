import helpers

credentials_with_empty_field = [
    {'email': '',
     'password': helpers.generate_random_password(),
     'name': helpers.generate_random_username()
     },
    {'email': helpers.generate_random_email(),
     'password': '',
     'name': helpers.generate_random_username()
     },
    {'email': helpers.generate_random_email(),
     'password': helpers.generate_random_password(),
     'name': ''
     }
]

class UserTestData:
    email = 'marina_kuratova_19@ya.ru'
    password = 'qwerty'
    username = 'marina'

class TestUserUpdate:
    updated_user_data = {
        'email': helpers.generate_random_email(),
        'password': helpers.generate_random_password(),
        'name': helpers.generate_random_username()
    }

class IngredientData:
    burger = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
                '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

    burger_2 = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6d',
                '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6f']

    invalid_hash_ingredient = ['61c0c5a71d1f82001bd00000']