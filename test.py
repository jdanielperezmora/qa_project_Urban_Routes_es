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
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)

    def test_full_order_flow(self):
        # 1. Direcciones
        self.page.set_address(data.address_from, data.address_to)
        self.page.click_request_taxi()

        # 2. Tarifa Comfort
        self.page.select_comfort()

        # 3. Teléfono
        self.page.fill_phone(data.phone_number)

        # 4. Tarjeta
        self.page.add_card(data.card_number, data.card_code)

        # 5. Mensaje, manta y helados
        self.page.set_message(data.message_for_driver)
        self.page.toggle_blanket()
        self.page.add_ice_cream(2)

        # 6. Pedir taxi y verificar modal
        self.page.final_order()
        assert self.page.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.DRIVER_MODAL))

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()