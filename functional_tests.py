from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)	
	
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		#User goes to app's homepage
		self.browser.get('http://localhost:8000')

		#User notices that page title includes words "to-do"
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish the test!')

#User is invited to enter a to-do item

#User types "Become a programming guru" in the text box


#After pressing ENTER the page updates and there is "1: Become a programming guru" as an item in todo list

#There is still a text box inviting to add new item, so user types "Learn about philosophy"


#Page updates again and shows both items on the list

#Site generates unique URL for user and informs him about that

#User visits given URL and sees previously created list

#User closes browser

if __name__=='__main__':
	unittest.main(warnings='ignore')