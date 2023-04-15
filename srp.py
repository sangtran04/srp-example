# Thông tin hóa đơn
class Invoice:
  # Hàm khởi tạo đói tượng hóa đơn
  def __init__(self, customerName, total):
    self.customerName = customerName
    self.total = total
  
  # Lấy thông tin chi tiết của một hóa đơn
  def get_details(self):
    return f'''Customer name: {self.customerName}, 
Total: {self.total}'''

# Thông tin thuế
class SalesTax:
  # Hàm khởi tạo đói tượng thuế
  def __init__(self, state):
    self.state = state

  # Tính toán phần trăm thuế theo bang
  # AZ: Arizona
  # TX: Texas
  # CA: California
  def get_sales_tax(self):
      if self.state == 'AZ':
        return 5.5
      elif self.state ==  'TX':
        return 3.2
      elif self.state ==  'CA':
        return 8.7

# Email
class Email:
  #Gửi email
  @staticmethod
  def send_email(content):
    print('Sending email...')
    print(content)
    
invoice = Invoice('Google', 100)
sales_tax = SalesTax('AZ')
print(sales_tax.get_sales_tax()) # In ra phần trăm thuế
Email.send_email(invoice.get_details()) # Gửi email
