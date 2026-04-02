from selenium.webdriver.common.by import By


class UrbanRoutesLocators:
    # Direcciones
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
    REQUEST_TAXI_BUTTON = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")

    # Tarifas
    COMFORT_TARIFF = (By.XPATH, "//div[contains(text(), 'Comfort')]")

    # Teléfono
    PHONE_BUTTON = (By.CLASS_NAME, 'np-text')
    PHONE_INPUT = (By.ID, 'phone')
    NEXT_BUTTON_PHONE = (By.XPATH, "//button[contains(text(), 'Siguiente')]")
    CONFIRMATION_CODE_INPUT = (By.ID, 'code')
    CONFIRM_PHONE_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirmar')]")

    # Tarjeta
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, 'pp-text')
    ADD_CARD_BUTTON = (By.CLASS_NAME, 'pp-plus')
    CARD_NUMBER_INPUT = (By.ID, 'number')
    CARD_CVV_INPUT = (By.XPATH, "//div[@class='card-code-input']//input[@id='code']")
    LINK_CARD_BUTTON = (By.XPATH, "//button[contains(text(), 'Agregar')]")
    CLOSE_PAYMENT_MODAL = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[1]/button")

    # Extras
    MESSAGE_FIELD = (By.ID, 'comment')
    BLANKET_SWITCH = (By.XPATH, "//*[@id='root']//div[@class='r-sw']//span[@class='slider round']")
    ICE_CREAM_PLUS = (By.XPATH, "//div[@class='r-counter']//div[@class='counter-plus']")

    # Final
    ORDER_BUTTON = (By.CLASS_NAME, 'smart-button')
    DRIVER_MODAL = (By.CLASS_NAME, 'order-header-content')