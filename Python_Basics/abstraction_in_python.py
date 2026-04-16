from abc import ABC,abstractmethod
class Calci(ABC):
    def __init__(self,value):
        self.val = value
    @abstractmethod
    def calculate_tax(self):
        pass
    @abstractmethod
    def calculate_total(self):
        pass

    def tax_cancel(self):
        pass

class Tax_Calculator(Calci):
    def calculate_tax(self):
        tax=0.10
        amt=tax*self.val
        return amt
    def calculate_total(self):
        total=self.calculate_tax()+self.val
        return total
    def tax_cancel(self):
        return self.val

amount=100
c=Tax_Calculator(amount)
print(f"Bill : {amount}")
print(f"Tax for the Amount : {c.calculate_tax()}")
print(f"Total bill after Tax Applied : {c.calculate_total()}")
print(f"Bill After Tax Cancelled : {c.tax_cancel()}")
