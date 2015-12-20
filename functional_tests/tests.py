from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)	
	
	def tearDown(self):
		self.browser.quit()
		
	def check_for_row_in_list_table(self,row_text):
		table=self.browser.find_element_by_id("id_list_table")
		rows=table.find_elements_by_tag_name("tr")
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):

		#User goes to app's homepage
		self.browser.get(self.live_server_url)

		#User notices that page title includes words "to-do"
		self.assertIn('To-Do',self.browser.title)
		header_text=self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',header_text)

		#User is invited to enter a to-do item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a To-Do item'
			)
		#User types "Become a programming guru" in the text box, presses ENTER, then types "Learn philosophy" and hits ENTER again
		inputbox.send_keys("Become a programmer guru")
		inputbox.send_keys(Keys.ENTER)
		
		inputbox = self.browser.find_element_by_id("id_new_item")
		inputbox.send_keys("Learn philosophy")
		inputbox.send_keys(Keys.ENTER)
	#After pressing ENTER the page updates and there are two items in to-do list

		self.check_for_row_in_list_table("1: Become a programmer guru")
		self.check_for_row_in_list_table("2: Learn philosophy")
#Page updates again and shows both items on the list

#Site generates unique URL for user and informs him about that

#User visits given URL and sees previously created list

#User closes browser

