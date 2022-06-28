import phonenumbers
from phonenumbers import timezone, carrier
 
myStringNumber = "+2349032604209"
myNumber = phonenumbers.parse(myStringNumber)
possible_number = phonenumbers.is_possible_number(myNumber)
valid_number = phonenumbers.is_valid_number(myNumber)

if valid_number: 
  print("Valid Number")  
  print(timezone.time_zones_for_number(myNumber)) 
  print(carrier.name_for_number(myNumber, "en"))  
else:
  print("Invalid Number") 
