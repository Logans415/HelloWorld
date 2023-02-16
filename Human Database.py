print ("\t\t\tHello and welcome to")
print ("\t\t\t  Human Database!")
print()
print ("\tWant to spy on people and add them to a database?")
print ("\tWell look out Facebook and watch out China, here we are!\n\n")

#Prompt the user for the file name.
#Prompt the user for their name.
#Prompt the user for their street address.
#Prompt the user for their phone number.
#Write the user name, street address and phone number to a comma-separated line in the file that your user typed in step 1.
#Once the data has been written to the file your program should read the file and display the contents .

def create_profile():
  #this function is practically the main one. 
  # first we gather all the required data, then we write it to two seperate files, one for the individual and one the main database.
  print ("Let's get to spying! What is the name of your target?")
  name = input("SPYING TARGET NAME:")
  with open ("database", "a") as profile:
    print(f"Ok, {name} will be written into the database, and a file will be made.")
    print ("\nNow, we need a few more details to help you finish up your target profile.")
    with open (name, "w") as target_info:
      
      street_address = input ("What is your targets address?\nADDRESS: ")
      if len(street_address) == 0:
        street_address = ("N/A")
      else:
        pass
      city = input ("CITY:")
      if len(city) == 0:
        city = ("N/A")
      else:
        pass
      state = input ("STATE:")
      if len(state) == 0:
        state = ("N/A")
      else:
        pass
      country = input ("(optional)COUNTRY:")
      if len(country) == 0:
        country = ("N/A")
      else:
        pass
      phone_number = input ("PHONE NUMBER: ")
      if len(phone_number) == 0:
        phone_number = ("N/A")
      else:
        pass
      details = input ("OTHER DETAILS: ")
      if len(details) == 0:
        details = ("NONE")
      else:
        pass
# this is the whole string, the main data collection
      info_string = (f"\nTarget: {name}\nAddress: {street_address}, {city} {state}.\nCOUNTRY: {country}\nPHONE NUMBER: {phone_number}\nDETAILS: {details}\n")

      profile.write (info_string)
      target_info.write (info_string)
      
      print ("Great! Your target data is in the database.")
      add_another()

# similar to the 'keep' functions you have seen me use in the past.
def add_another():
  keep = input("\nWould you like to add another target to the database?\n\tPlease Type yes/no: ")
  if keep != "no":
    print("\nAlright you nosey criminal, lets do this!")
    create_profile()
  else:
    print ("Below is a list of cataloged targets, followed by the expansive set of data.\n")
    with open("database", "r") as file:
      for line in file:
        line = line.strip()  # remove the newline character
        # process the current line
        print(line)

  print("\n\t\t\t\tThanks for using my program!\n\t\t\t\tProgram Built by Logan Smith")
  exit()

create_profile()