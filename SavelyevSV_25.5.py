import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import valid_email, valid_password

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('c:/test/chromedriver.exe')
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.set_window_size(1920, 1080)
    yield
    pytest.driver.quit()


def list_of_pets_data(strt, elements):
    field_nbr = 4
    element_data = elements[strt::field_nbr]
    pets_data = []
    for i in element_data:
        pets_data.append(i.text)
        assert i.text != "", 'В карточке питомца есть пустое поле'
    return pets_data

def test_page_my_pets():
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'button[type="submit"]'))).click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, u"Мои питомцы"))).click()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '.navbar-brand.header2').text == "PetFriends"
    my_pets = pytest.driver.find_element(By.CSS_SELECTOR, 'div[class=".col-sm-4 left"]')
    number_my_pets = int(my_pets.text.split ('\n')[1].split(':')[1])
    elements = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td')

    pet_names = list_of_pets_data(0, elements)
    pet_breeds = list_of_pets_data(1, elements)
    pet_age = list_of_pets_data(2, elements)

    assert number_my_pets == len(pet_names), 'Несоответствие числа карточек и питомцев'

    pet_images = pytest.driver.find_elements(By.CSS_SELECTOR, 'th img')
    pets_with_image = 0
    for i in range(number_my_pets):
        if pet_images[i].get_attribute('src') != "":
            pets_with_image += 1
    assert pets_with_image >= number_my_pets/2, 'Чиcло питомцев без фото меньше половины!'

    data_my_pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    list_data_my_pets = []
    for i in range(len(data_my_pets)):
        list_data = data_my_pets[i].text.split("\n")
        list_data_my_pets.append(list_data[0])
    set_data_my_pets = set(list_data_my_pets)
    assert len(list_data_my_pets) == len(set_data_my_pets)

    assert len(pet_names) == len(set(pet_names)), 'Имена питомцев повторяются!'


    print(pet_names, '\n', pet_breeds, '\n', pet_age)


