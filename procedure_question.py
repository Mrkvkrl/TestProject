# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

class ProcedureQuestion(unittest.TestCase):
    print("Hello")

    def setUp(self):
        print("setUp")
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def procedure_question(self):
        print("procedure_question")
        wd = self.wd
        # wd.get("https://test.fabrikant.ru/trades/atom/ProposalRequest/?action=view&id=10092")
        wd.get("http://localhost/addressbook/")
        # wd.find_element(By.CSS_SELECTOR,"path").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # wd.find_element(By.NAME,"login[password]").click()
        # wd.find_element(By.NAME,"login[password]").clear()
        # wd.find_element(By.NAME,"login[password]").send_keys("cmy8hggb")
        # wd.find_element(By.NAME,"login[username]").click()
        # wd.find_element(By.NAME,"login[username]").clear()
        # wd.find_element(By.NAME,"login[username]").send_keys("bidder1")
        # wd.find_element(By.NAME,"login[username]").send_keys(Keys.ENTER)
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # wd.find_element(By.XPATH,u"//input[@value='Задать вопрос организатору']").click()
        # Select(wd.find_element(By.ID,"question_subReq")).select_by_visible_text(u"УСЛОВИЯ ДОГОВОРА")
        # wd.find_element_by_xpath("//option[@value='TERMS_CTR']").click()
        # wd.find_element_by_id("question_summaryReq").click()
        # Select(wd.find_element_by_id("question_summaryReq")).select_by_visible_text(u"УТОЧНЕНИЕ УСЛОВИЙ ДОГОВОРА")
        # wd.find_element_by_xpath("//option[@value='CLARIF_TERMS_CTR']").click()
        # wd.find_element_by_id("question_questionText").click()
        # wd.find_element_by_id("question_questionText").clear()
        # wd.find_element_by_id("question_questionText").send_keys(u"что за дела?")
        # wd.find_element_by_id("question_save").click()
        # wd.find_element_by_link_text(u"Подписать и опубликовать").click()
        # wd.find_element_by_id("buttonSign").click()
        # wd.find_element_by_id("select_sert_name").click()
        # Select(wd.find_element_by_id("select_sert_name")).select_by_visible_text(u"bidder1 (до 22.06.2023)")
        # wd.find_element_by_xpath("//option[@value='9FAA487B94D87AC84892FDB84948379ADEEB3850']").click()
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Закрыть окно'])[1]/following::span[1]").click()
        # wd.find_element_by_link_text(u"Вернуться к процедуре").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()
        # self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
