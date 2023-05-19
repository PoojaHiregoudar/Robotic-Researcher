from RPA.Browser.Selenium import Selenium


br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name
        self.browser = Selenium()

    def say_hello(self):
        print("Hello, It's me your search wizard " + self.name)
        
    def robo_steps(self):
        print("I am here today to do some magic and give you some relevant information on few scientists Let me tell you how I did this fanatastic job to make your life easy.\nSo here's what I did, Just like you, I googled the scientist landing on their wikipedia page.\nYay!!!! from there I scrapped their Name, Date of birth, Death anniversary, and used my smart brains to calculate the age of the scientist.\nNow after knowing the basic infomation one needs to know a bit about the scientist so I handled that as well, grabbing a small summary for you to read through and get a better understanding. So run along have fun searching for favourite scientists.") 
      
        
    def scientist_info(self, scientist_name):
        # Open the scientist's Wikipedia page
        self.browser.open_available_browser(f"https://en.wikipedia.org/wiki/{scientist_name}")
        
        self.browser.wait_until_page_contains_element("css:#mw-content-text")
        
        
        if (scientist_name == 'Marie Curie'):
            scientist_info = self.browser.get_text("//table[@class='infobox biography vcard']//tr[1]")
            scientist_info1 = self.browser.get_text("//body[1]/div[2]/div[1]/div[3]/main[1]/div[3]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]")
            scientist_info2 = self.browser.get_text("//table[@class='infobox biography vcard']//tr[5]")
            scientist_info3 = self.browser.get_text("xpath://*[@id='mw-content-text']//p[3]")
            byear_element = self.browser.find_element("css:.infobox .bday")
            byear = byear_element.get_attribute("textContent").split('-')[0]
            byear = int(byear)
            
            dyear_element = self.browser.find_element("//body[1]/div[2]/div[1]/div[3]/main[1]/div[3]/div[3]/div[1]/table[1]/tbody[1]/tr[5]/td[1]//span")
            dyear = dyear_element.get_attribute("textContent").split('-')[0]
            dyear = int(dyear[1:])
            age = dyear- byear
        else:
            scientist_info3 = self.browser.get_text("xpath://*[@id='mw-content-text']//p[2]")
        

        # Extract and return the scientist information
            scientist_info = self.browser.get_text("//table[@class='infobox biography vcard']//tr[1]")
            scientist_info1 = self.browser.get_text("//body[1]/div[2]/div[1]/div[3]/main[1]/div[3]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[1]")
            byear_element = self.browser.find_element("css:.infobox .bday")
            byear = byear_element.get_attribute("textContent").split('-')[0]
            byear = int(byear)


            scientist_info2 = self.browser.get_text("//table[@class='infobox biography vcard']//tr[4]")
            dyear_element = self.browser.find_element("//body[1]/div[2]/div[1]/div[3]/main[1]/div[3]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]//span")
            dyear = dyear_element.get_attribute("textContent").split('-')[0]
            dyear = int(dyear[1:])


            age = dyear- byear
        

        
        return scientist_info, scientist_info1, scientist_info2, scientist_info3, age
    
    def new_search(self):
        name = input("Enter your favourite scientist name for me to do my magic or type in bye if you want to exit : ")
        name = name.title()
        if (len(name) == 0):
            print("Please enter a valid name")
            self.new_search()
        elif (name == 'Bye'):
            self.say_goodbye()
        else:
            information1, information2, information3, information4,age = self.scientist_info(name)
            self.display_information(information1, information2, information3, information4,age)
            self.new_search()
            
            
    
    def display_information(self, information1, information2, information3, information4,age):
        print(f"Name : {information1} \nBorn: {information2} \nDied : {information3} \nAge : {age} \n{information4} \n")

    def say_goodbye(self):
        print(" " + self.name +" Signing off " )
        
    
    def cleanup(self):
        self.browser.close_all_browsers()


