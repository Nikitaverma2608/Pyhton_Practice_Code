class contact: 
   def __init__(self,name,phone_number):
       self.name=name
       self.phone_number=phone_number

   def get_data(self):
  
       contact_details = open("Contact Details.txt","r")
       print(contact_details.read())
       contact_details.close()

   def put_data(self):
       global contact_details

       contact_details = open("Contact Details.txt","w")
       contact_details.write(name)
       contact_details.write("\n")
       contact_details.write(phone_number)
       contact_details.close()

name = input("Enter name: ")
phone_number= input("Enter phone: ")
c1=contact(name,phone_number)
p1=c1.put_data()
g1=c1.get_data()
