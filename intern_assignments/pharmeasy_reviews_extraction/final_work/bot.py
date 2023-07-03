import time
import os
import json

from selenium import webdriver
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

class SeleniumBot:
    
    def __init__(self, executable_path="C:/VS_Code_folder/Intern_projects/pharmeasy_reviews_extraction/chromedriver.exe"):
        

        capabilities = webdriver.DesiredCapabilities.CHROME

        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("start-maximized")

        #chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(executable_path), chrome_options=chrome_options, desired_capabilities=capabilities)
                
        stealth(self.driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
        
        time.sleep(2)
        self.driver.get("https://bot.sannysoft.com/")
        time.sleep(5)
        self.driver.get("https://pharmeasy.in/health-care/products/chau-foods-phool-makhana-fox-nuts-lotus-seeds--3772108")

        
    def send_ajax(self, url, method="GET", headers={}, data={}):
        for _ in range(3):

            try : 
                response = self.driver.execute_script("""
            function run(method, url, headers, data) {
                // Creating Our XMLHttpRequest object 
                var xhr = new XMLHttpRequest();

                // Making our connection  
                xhr.open(method, url, false);  // Set the method to POST or GET and the third argument to false to make the request synchronous

                for (var header in headers) {
                    xhr.setRequestHeader(header, headers[header]);  
                }

                // Sending our request with data
                if (method === 'POST') {
                    xhr.setRequestHeader('Content-Type', 'application/json');
                    xhr.send(JSON.stringify(data));  // Convert the data to a JSON string before sending it
                } else {
                    xhr.send();
                }

                // function execute after request is successful 
                if (xhr.readyState == 4) {  // Check for status 201 (created)
                    console.log(xhr.responseText);
                    return xhr.responseText;  // Return the response text
                }
            }
            return run(arguments[0], arguments[1], arguments[2], arguments[3]); 
            """, method, url, headers, data)
                return response
            except JavascriptException:
                self.driver.refresh()
                time.sleep(2)
                return '{"status":"invalid_url"}'
            
            except Exception as e:
                print(type(e),e)
                self.driver.refresh()
                time.sleep(2)
        
    def storing_files(self, file_data, product_id):

        file_path = product_id +'.json' 

        if os.path.exists(file_path):
            with open(file_path, 'a') as file:
                file.write(json.dumps(file_data, indent=4, sort_keys=True))

        else:
            formatted_json = json.dumps(file_data, indent=4, sort_keys=True)
            with open(file_path, 'w') as file:
                file.write(formatted_json)

    def get_data(self, my_link, store_data=False):
        extrated_data, page_number = [], 0
        
        self.driver.get(my_link)
        product_id = str(my_link.split("-")[-1])
        print(product_id, "==>", my_link)
        time.sleep(1)
        data_present = True
        while data_present:
            page_number += 1
            if not (page_number % 5):
                print(page_number, "page are completed for", product_id)
            responce = self.send_ajax(f"https://pharmeasy.in/api/browse/product/reviews/{str(product_id)}?page={page_number}&showAll=1")
            responce = json.loads(responce)

            if "error" in responce:
                print(responce)
                data_present = False
            elif "data" in responce and responce['data']:
                if "response" in responce['data'] and responce['data']['response']:
                    extrated_data.extend(responce['data']['response'])
                else:
                    data_present = False

        if extrated_data:
            if store_data:
                self.storing_files({'data': extrated_data}, str(product_id))

            return {'data': extrated_data}



