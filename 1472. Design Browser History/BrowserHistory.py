class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        while len(self.history) > self.index+1:
            self.history.pop()
        
        self.history.append(url)
        self.index = len(self.history)-1
        

    def back(self, steps: int) -> str:
        self.index = max(0, self.index-steps)
        return self.history[self.index]

    def forward(self, steps: int) -> str:
        self.index = min(len(self.history)-1, self.index+steps)
        return self.history[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)