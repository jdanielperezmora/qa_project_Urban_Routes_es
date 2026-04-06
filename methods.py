from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import UrbanRoutesLocators
from retrive_phone_code import retrieve_phone_code


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Aumentado a 15s para mayor margen

    def set_address(self, from_addr, to_addr):
        # Espera explícita para ambos campos
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.FROM_FIELD)).send_keys(from_addr)
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.TO_FIELD)).send_keys(to_addr)

    def click_request_taxi(self):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.REQUEST_TAXI_BUTTON)).click()

    def select_comfort(self):
        # La tarifa Comfort puede tardar en ser clickable tras el paso anterior
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.COMFORT_TARIFF)).click()

    def fill_phone(self, phone):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PHONE_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.PHONE_INPUT)).send_keys(phone)
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.NEXT_BUTTON_PHONE)).click()

        code = retrieve_phone_code(self.driver)
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.CONFIRMATION_CODE_INPUT)).send_keys(code)
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.CONFIRM_PHONE_BUTTON)).click()

    def add_card(self, number, code):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.PAYMENT_METHOD_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ADD_CARD_BUTTON)).click()

        # Llenado de tarjeta
        card_field = self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.CARD_NUMBER_INPUT))
        card_field.send_keys(number)

        cvv_field = self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.CARD_CVV_INPUT))
        cvv_field.send_keys(code)
        cvv_field.send_keys(Keys.TAB)

        # Esperar a que el botón de enlace se active tras el TAB
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.LINK_CARD_BUTTON)).click()
        # Cerrar modal
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.CLOSE_PAYMENT_MODAL)).click()

    def set_message(self, message):
        self.wait.until(EC.visibility_of_element_located(UrbanRoutesLocators.MESSAGE_FIELD)).send_keys(message)

    def toggle_blanket(self):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.BLANKET_SWITCH)).click()

    def add_ice_cream(self, quantity):
        plus_btn = self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ICE_CREAM_PLUS))
        for _ in range(quantity):
            plus_btn.click()

    def final_order(self):
        self.wait.until(EC.element_to_be_clickable(UrbanRoutesLocators.ORDER_BUTTON)).click()