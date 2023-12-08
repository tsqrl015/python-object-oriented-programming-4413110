# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"
#12-8-23 - add code for buy rating with use of hasattr() in get_description()

class Stock:
    
    def __init__(self, ticker_var, price_var, company_var):
        self.ticker_var = ticker_var
        self.price_var = price_var
        self.company_var = company_var

    def set_rating(self,rating_var):
        self.rating = rating_var
    
    
    def get_description(self) -> str:
        if hasattr(self, "rating"):
            output_str = self.ticker_var + " : " + self.company_var + " -- $" + str(self.price_var) + " (Stock Rating: " + self.rating + ")"
            return output_str
        else:
            output_str = self.ticker_var + " : " + self.company_var + " -- $" + str(self.price_var)
            return output_str
            
        
# ~~~~~~~~~ TEST CODE ~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
msft.set_rating("Buy")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())
