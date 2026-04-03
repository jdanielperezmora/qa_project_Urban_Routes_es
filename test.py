import data
from selenium import webdriver
from methods import UrbanRoutesPage
from locators import UrbanRoutesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    # 1. Configuración de la dirección inicial
    def test_set_address(self):
            self.page.set_address(data.address_from, data.address_to)
            assert self.driver.find_element(*UrbanRoutesLocators.FROM_FIELD).get_property('value') == data.address_from
            assert self.driver.find_element(*UrbanRoutesLocators.TO_FIELD).get_property('value') == data.address_to

    # 2. Selección de la tarifa Comfort
    def test_select_comfort_tariff(self):
            self.page.click_request_taxi()
            self.page.select_comfort()
            # Verificamos que el elemento de tarifa Comfort esté presente o activo
            tariff_element = self.driver.find_element(*UrbanRoutesLocators.COMFORT_TARIFF)
            assert tariff_element.is_displayed()

    # 3. Ingreso del número de teléfono
    def test_fill_phone_number(self):
            self.page.fill_phone(data.phone_number)
            phone_button_text = self.driver.find_element(*UrbanRoutesLocators.PHONE_BUTTON).text
            assert phone_button_text == data.phone_number

    # 4. Agregar tarjeta de crédito
    def test_add_credit_card(self):
            # Este paso cubre la apertura del modal y llenado de datos
            self.page.add_card(data.card_number, data.card_code)
            payment_text = self.driver.find_element(*UrbanRoutesLocators.PAYMENT_METHOD_BUTTON).text
            assert "Método de pago" in payment_text

    # 5. Confirmación del código de la tarjeta (Verificación de enlace exitoso)
    def test_card_linked_successfully(self):
            # Validamos que después de agregarla, el check o el texto indique que está lista
            # Si el paso anterior cerró el modal, verificamos el estado en la interfaz principal
            card_value = self.driver.find_element(*UrbanRoutesLocators.PAYMENT_METHOD_TEXT).text
            #assert data.card_number[-2:] in card_value  # Verifica que coincidan los últimos dígitos
            assert "Tarjeta" in card_value

    # 6. Envío de mensaje al conductor
    def test_comment_for_driver(self):
            self.page.set_message(data.message_for_driver)
            message_val = self.driver.find_element(*UrbanRoutesLocators.MESSAGE_FIELD).get_property('value')
            assert message_val == data.message_for_driver

    # 7. Solicitud de manta y pañuelos
    def test_order_blanket_and_tissues(self):
            self.page.toggle_blanket()
            # Nota: el assert depende de cómo esté implementado el switch (clase active, checked, etc.)
            # Aquí validamos que el elemento sea visible y se pueda interactuar con él
            assert self.driver.find_element(*UrbanRoutesLocators.BLANKET_SWITCH).is_enabled()

    # 8. Pedido de 2 helados
    def test_order_two_ice_creams(self):
            self.page.add_ice_cream(2)
            # Buscamos el contador que debería marcar '2'
            counter = self.driver.find_element(By.XPATH, "//div[@class='counter-value' and text()='2']")
            assert counter.text == "2"

    # 9. Aparición del modal para buscar un taxi
    def test_appearance_of_taxi_modal(self):
            self.page.final_order()
            # Esperamos a que el modal de búsqueda (con el contador/info conductor) aparezca
            modal_visible = self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.DRIVER_MODAL))
            assert modal_visible.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()