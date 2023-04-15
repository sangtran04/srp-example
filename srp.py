class Invoice:
  def __init__(self, customerName, total):
    self.customerName = customerName
    self.total = total

  def get_details(self):
    return f'''Customer name: {self.customerName}, 
Total: {self.total}'''

class SalesTax:
  def __init__(self, state):
    self.state = state

  def get_sales_tax(self):
      if self.state == 'AZ':
        return 5.5
      elif self.state ==  'TX':
        return 3.2
      elif self.state ==  'CA':
        return 8.7

class Email:
  @staticmethod
  def send_email(content):
    print('Sending email...')
    print(content)
    
invoice = Invoice('Google', 100)
sales_tax = SalesTax('AZ')
print(sales_tax.get_sales_tax())
Email.send_email(invoice.get_details())
