# mini project in python resume builder --

print("🙂-Welcome to resume builder-🙂")

name = input("Enter your name :-")

resume = {
    "persnol_detail" : {},
    "Education" : {},
    "skill" : [],
    "Experence" : {},
}

while True:
    print("""
    1 - Personal Details
    2 - Education
    3 - Skills
    4 - Experience
    5 - Display Resume
    6 - Exit
    """)
    
    user_choise = int(input("What should be you do :-"))
    
    
#  1 - Personal Details
    if user_choise == 1:
        resume["persnol_detail"]["name"] = input("Enter your name :-")
        resume["persnol_detail"]["E-mail"] = input("Enter your E-mail :-")
        resume['persnol_detail']['phone-number'] = int(input("Enter number here :-"))
        resume['persnol_detail']['Address'] = input("Enter your address :-")

        print("your persnol info are addedd :-")
       
    
# 2 - Education

    elif user_choise == 2:
        resume["Education"]["collage"] = input("Enter your collage name :-")
        resume["Education"]["Degree"] = input("which degree you passed :-")
        resume['Education']["passing year"] = int(input("enter your passing year :-"))
        print(" Education details saved")
        
        
# skill--

    elif user_choise == 3:
        skill = input("Enter your skill here :-")
        resume["skill"].append(skill)
        print("skill are added :-")
        
    # Experence
    
    elif user_choise == 4:
        resume["Experence"]["company"] = input("Enter your company name :-")
        resume["Experence"]["role"] = input("Role of work :-")
        resume["Experence"]["years"] = input("Years of experience:-")
        print(" Experience added")
        
        
    #   display resume --
    
    elif user_choise == 5:
        print(f"\n-----Hello {name} your resume")
        
        print("\n Personal Details -")
        for k, v in resume["persnol_detail"].items():
            print(f"{k.capitalize()} : {v}")

        print("\n your Education - ")
        for k, v in resume["Education"].items():
            print(f"{k.capitalize()} : {v}")
            
            
        print("\n Skills -")
        for s in resume["skill"]:
            print("_" , s)
            
            
        print("\n your Experence :-")
        for k, v in resume["Experence"].items():
            print(f"{k.capitalize()} : {v}")
            
        
    elif user_choise == 6:
         print("👋 Thank you for using Resume Builder")
         break
     
    else:
         print("invalid user choise :-")
       
        