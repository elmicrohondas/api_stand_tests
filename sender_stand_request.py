import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")


def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = post_new_user(user_body)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, "\
                                         "la longitud debe ser de 2 a 15 caracteres."