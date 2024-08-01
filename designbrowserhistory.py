class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str):

        self.history = self.history[:self.current_index + 1]
        self.history.append(url)
        self.current_index += 1

    def back(self, steps: int):
       
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int):
      
        self.current_index = min(len(self.history) - 1, self.current_index + steps)
        return self.history[self.current_index]

  
browser_history = BrowserHistory("leetcode.com")

browser_history.visit("google.com")    
browser_history.visit("facebook.com")   
browser_history.visit("youtube.com")   

print(browser_history.back(1))          
print(browser_history.back(1))         

print(browser_history.forward(1))       


browser_history.visit("linkedin.com")


print(browser_history.forward(2))     


print(browser_history.back(2))          
print(browser_history.back(7))          
    
