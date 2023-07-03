

class something():
    
    def __init__(self) -> None:
        pass

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
            except Exception as e:
                print(type(e),e)
                #self.driver.refresh()
                #time.sleep(2)

    def send_ajax_with_status(self, url, method="GET", headers={}, data={}, send_status=False):
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
                    return {"status": xhr.status, "response": xhr.responseText};
                }

                return {"status": xhr.status, "response": "null"};
            }
            return run(arguments[0], arguments[1], arguments[2], arguments[3]); 
            """, method, url, headers, data)
                
                if send_status:
                    return response
                else:
                    return response['response']

            except Exception as e:
                print(type(e),e)
                #self.driver.refresh()
                #time.sleep(2)









