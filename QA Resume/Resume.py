import variables
obj=variables.Skills()
Wel_msg='''\
    Hi! Welcome to my Profile
    I am Mitul Kataria
    "Quality Analyst"
    '''
print(Wel_msg)
qahire=input("Want to hire a QA?\n'Yes' or 'No'").lower()

if(qahire=="yes"):
    print("I have experience in Manual and Automation testing")
    obj.Experience()
    knowskills=input("Want to know about the skills\n'Yes' or 'No'").lower()
    if(knowskills=="yes"):
        details=input('''\
        For Automation testing skills enter "A"
        For Manual testing skills enter "M"
        For both enter "B" ''').lower()
        if(details=="a"):
            obj.Automation()
            obj.Tools()
        elif(details=="m"):
            obj.Manual()
            obj.Tools()
        else:
            obj.Automation()
            obj.Manual()
            obj.Tools()
        Org = input("Enter 'yes' to know Previous Organizations").lower()
        if (Org == "yes"):
            obj.Organizations()
        else:
            obj.Contact()
        Qual = input("Enter 'yes' to know Educational Qualification").lower()
        if (Qual == 'yes'):
            obj.Qualification()
        else:
            obj.Contact()
        hobby = input("Want to know my hobbies?")
        if (hobby=="yes"):
            obj.hobbies()
    else:
        print("Thank you")

    full_res=input("Want to view full Resume?")
    if(full_res=="yes"):
        print(Wel_msg)
        obj.all()
    else:
        print("Thank you for your time.")
else:
    print("Thank you for your time.")



