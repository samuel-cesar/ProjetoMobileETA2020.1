import unittest
from appium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCaseHackerHews(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def setUp(self):
        caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'automationName': 'UiAutomator2',
            'app': 'C:\\DESENVOLVIMENTO\\APKS\\com.leavjenn.hews_28_apps.evozi.com.apk',
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def tearDown(self):
        self.driver.quit()
        time.sleep(2)

    def test_01_validacaoUsernameVazio(self):
        self.acessarATelaDeLogin()
        self.waitUserName()

        # PREENCHER O CAMPO USERNAME COM VAZIO
        inputUsername = self.driver.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        inputUsername.clear()
        inputUsername.send_keys("")

        # PREENCHER O CAMPO PASSWORD
        inputPassword = self.driver.find_element_by_id("com.leavjenn.hews:id/et_password")
        inputPassword.clear()
        inputPassword.send_keys("123456")

        # CLICAR NO BOTÃO LOGIN
        btnLogin = self.driver.find_element_by_id("android:id/button1")
        btnLogin.click()

        # VERIFICAR VALIDAÇÃO USERNAME
        msgValidacaoUsername = self.driver.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        assert msgValidacaoUsername.text == "Catch you, anonymous!"
        print("test_01_validacaoUsernameVazio")

    def test_02_validacaoPasswordVazio(self):
        self.acessarATelaDeLogin()
        self.waitUserName()
        # PREENCHER O CAMPO USERNAME
        inputUsername = self.driver.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        inputUsername.clear()
        inputUsername.send_keys("test@test.com")

        # PREENCHER O CAMPO PASSWORD COM VAZIO
        inputPassword = self.driver.find_element_by_id("com.leavjenn.hews:id/et_password")
        inputPassword.clear()
        inputPassword.send_keys("")

        # CLICAR NO BOTÃO LOGIN
        btnLogin = self.driver.find_element_by_id("android:id/button1")
        btnLogin.click()

        # VERIFICAR VALIDAÇÃO PASSWORD
        msgValidacaoPassword = self.driver.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        assert msgValidacaoPassword.text == "You got a short…password"
        print("test_02_validacaoPasswordVazio")

    def test_03_validacaoUsernameEPasswordVazio(self):
        self.acessarATelaDeLogin()
        self.waitUserName()
        # PREENCHER O CAMPO USERNAME COM VAZIO
        inputUsername = self.driver.find_element_by_id("com.leavjenn.hews:id/et_user_name")
        inputUsername.clear()
        inputUsername.send_keys("")

        # PREENCHER O CAMPO PASSWORD COM VAZIO
        inputPassword = self.driver.find_element_by_id("com.leavjenn.hews:id/et_password")
        inputPassword.clear()
        inputPassword.send_keys("")

        # CLICAR NO BOTÃO LOGIN
        btnLogin = self.driver.find_element_by_id("android:id/button1")
        btnLogin.click()

        # VERIFICAR VALIDAÇÃO PASSWORD
        msgValidacaoUsernameEPassword = self.driver.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        assert msgValidacaoUsernameEPassword.text == "Catch you, anonymous!"
        print("test_03_validacaoUsernameEPasswordVazio")

    def acessarATelaDeLogin(self):
        wait = self.getWebDriveWait()
        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Hews']")))
        # CLICAR NA LABEL HEWS
        labelNews = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Hews']")
        assert labelNews.text == "Hews"

        # CLICAR NO NAVIGATEUP
        navigateUp = self.driver.find_element_by_accessibility_id("Navigate up")
        navigateUp.click()

        wait.until(expected_conditions.presence_of_element_located((By.ID, "com.leavjenn.hews:id/tv_account")))
        # CLICAR NO CAMPO LOGOUT
        comboLogout = self.driver.find_element_by_id("com.leavjenn.hews:id/tv_account")
        comboLogout.click()

        wait.until(
            expected_conditions.presence_of_element_located((By.ID, "com.leavjenn.hews:id/design_menu_item_text")))
        # CLICAR NA LABEL LOGIN
        labelLogin = self.driver.find_element_by_id("com.leavjenn.hews:id/design_menu_item_text")
        labelLogin.click()

        wait.until(expected_conditions.presence_of_element_located((By.ID, "android:id/alertTitle")))
        # VERIFICAR QUE A TELA DE LOGIN É EXIBIDA
        titleLogin = self.driver.find_element_by_id("android:id/alertTitle")
        yourPasswordWillNotBeSaved = self.driver.find_element_by_id("com.leavjenn.hews:id/tv_prompt")
        assert titleLogin.text == "Login"
        assert yourPasswordWillNotBeSaved.text == "* Your password will NOT be saved"

    def getWebDriveWait(self):
        wait = WebDriverWait(self.driver, 5)
        return wait

    def waitUserName(self):
        wait = self.getWebDriveWait()
        wait.until(expected_conditions.presence_of_element_located((By.ID, "com.leavjenn.hews:id/et_user_name")))
