import numbers_to_words
from numbers_to_words import Digits_to_words


class Umeme_bill():
  def __init__(self, previous_meter_reading, current_meter_reading, flat_unit_rate, flat_units, remaining_unit_rate, vat, service_fee):
    self.previous_meter_reading = previous_meter_reading
    self.current_meter_reading = current_meter_reading
    self.flat_unit_rate = flat_unit_rate
    self.flat_units = flat_units
    self.remaining_unit_rate = remaining_unit_rate
    self.vat = vat
    self.service_fee = service_fee
  
  def umeme_pay(self):
      number_of_units = self.current_meter_reading - self.previous_meter_reading
      remaining_units = number_of_units - self.flat_units 
      flat_unit_amount = self.flat_unit_rate * self.flat_units
      remaining_unit_amount = self.remaining_unit_rate * remaining_units
      if number_of_units <= self.flat_units:
        flat_unit_amount = number_of_units * self.flat_unit_rate
        total_amount = flat_unit_amount
      else:
        total_amount = flat_unit_amount + remaining_unit_amount
      vat_amount = self.vat * total_amount / 100
      amount_to_pay = round((total_amount + vat_amount + self.service_fee),2)
    
      return amount_to_pay

flat_units = input("Enter the number of flat units: ")
flat_unit_rate = input("Enter the cost per flat unit of electricity: ")
remaining_unit_rate = input("Enter the remaining unit rate: ")
vat = input("Enter the vat rate,(percentage without the % sign): ")
service_fee = input("Enter the monthly service rate: ")

try:
  flat_units = float(flat_units)
  flat_unit_rate = float(flat_unit_rate)
  remaining_unit_rate = float(remaining_unit_rate)
  vat = float(vat)
  service_fee = float(service_fee)
  number_of_customers = int(input("Enter the number of customers: "))
except:
  print("Enter only numeric values")

customer_names = []
customer_bills = []

i = 1
while i<= number_of_customers:
  customer_name = input(f"Enter name of customer {i}: ")
  customer_names.append(customer_name)
  
  current_meter_reading = input(f"Enter {customer_name}'s current meter reading: ")
  previous_meter_reading = input(f"Enter {customer_name}'s previous meter reading: ")
    
  try:
    reading1 = float(current_meter_reading)
    reading2 = float(previous_meter_reading) 
    
  except:
    print("Please enter numeric values only!")

  amt = Umeme_bill(reading2, reading1, flat_unit_rate, flat_units, remaining_unit_rate, vat, service_fee)
  amount = amt.umeme_pay()
  customer_bills.append(amount)
  i+=1

for x,y in zip(customer_names, customer_bills):
  bill = Digits_to_words(str(y))
  bill_in_words = bill.numbers_to_words()
  bill_list = bill_in_words.split("in words is: ")
  
  print(f"{x}'s electricity bill is UGX: {bill_list[0]} ({bill_list[1]})")

