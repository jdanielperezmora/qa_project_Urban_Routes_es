import data
from selenium import webdriver
from methods import UrbanRoutesPage
from locators import UrbanRoutesLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window() # Crucial para que los elementos sean cliqueables
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_set_address(self):
        self.page.set_address(data.address_from, data.address_to)
        # Verificación con espera para asegurar que el texto se procesó
        from_val = self.page.wait.until(lambda d: d.find_element(*UrbanRoutesLocators.FROM_FIELD).get_property('value'))
        assert from_val == data.address_from

    def test_select_comfort_tariff(self):
        self.page.click_request_taxi()
        self.page.select_comfort()
        # Verificamos que el contenedor de la tarifa esté visible
        tariff_card = self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.COMFORT_TARIFF))
        assert tariff_card.is_displayed()

    def test_fill_phone_number(self):
        self.page.fill_phone(data.phone_number)
        # El botón de teléfono debe actualizar su texto al número ingresado
        phone_btn = self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.PHONE_BUTTON))
        assert phone_btn.text == data.phone_number

    def test_add_credit_card(self):
        self.page.add_card(data.card_number, data.card_code)
        # Tras cerrar el modal, verificamos que el texto del método de pago cambió
        payment_method = self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.PAYMENT_METHOD_TEXT))
        assert "Tarjeta" in payment_method.text

    def test_comment_for_driver(self):
        self.page.set_message(data.message_for_driver)
        # Verificamos el atributo value del campo de mensaje
        msg_field = self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.MESSAGE_FIELD))
        assert msg_field.get_property('value') == data.message_for_driver

    def test_order_blanket_and_tissues(self):
        self.page.toggle_blanket()
        # En este caso, validamos que el elemento sea interactuable
        blanket_btn = self.page.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.BLANKET_SWITCH))
        assert blanket_btn.is_enabled()

    def test_order_two_ice_creams(self):
        self.page.add_ice_cream(2)
        # Esperamos a que el contador de helados llegue a "2"
        counter = self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.ICE_CREAM_COUNTER))
        assert counter.text == "2"

    def test_appearance_of_taxi_modal(self):
        self.page.final_order()
        # Espera explícita al modal final de búsqueda
        modal = self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.DRIVER_MODAL))
        assert modal.is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()