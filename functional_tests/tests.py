from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(StaticLiveServerTestCase):

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
		edith_list_url=self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Become a programmer guru')
		
		inputbox = self.browser.find_element_by_id("id_new_item")
		inputbox.send_keys("Learn philosophy")
		inputbox.send_keys(Keys.ENTER)
	#After pressing ENTER the page updates and there are two items in to-do list

		self.check_for_row_in_list_table("1: Become a programmer guru")
		self.check_for_row_in_list_table("2: Learn philosophy")

#User 2 now comes to the computer

##We start new browser session to assure that User 2 doesn't see any information from User 1 via cookies etc.

		self.browser.quit()
		self.browser=webdriver.Firefox()

#User 2 visits homepage and there is no sign of User 1 content

		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Become a programmer guru',page_text)
		self.assertNotIn('philosophy', page_text)

#User 2 starts new list by entering an item

		inputbox=self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

#User 2 gets his own unique URL

		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url,edith_list_url)

#There is no trace of User 1 list

		page_text=self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('programmer guru',page_text)
		self.assertIn('Buy milk', page_text)

	def test_layout_and_styling(self):
		#User goes to the home page
		self.browser.get(self.live_server_url)
		self.browser.set_window_size(1024,768)

		#Input box is centered
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta=5)
		
		#New list is centered too
		inputbox.send_keys('testing\n')
		inputbox=self.browser.find_element_by_id('id_new_item')	
		self.assertAlmostEqual(inputbox.location['x']+inputbox.size['width']/2,512,delta=5)
