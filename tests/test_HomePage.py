
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getName().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["Gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param

#This is test home page test
#new one
