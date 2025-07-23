# Bored API: https://bored-api.appbrewery.com
import  requests

def  get_random_activity():
    """
    Get a completely random activity suggestion
    API: https://bored-api.appbrewery.com/random
    """
    # Step 1: define our url and our endpoint (route)
    url ='https://bored-api.appbrewery.com/random'
    
    # Step2: Make the requests
    response =requests.get(url)
    
    # Step3: Check what we got back
    # print("Status Code: ", response.status_code)
    # print("Raw Response: ", response.text)
    
    # Step4: Parse JSON data (make it something useful in python)
    if response.status_code == 200:
        data=response.json() #convert to python dictionary
        # print(f"parsed data : {data}")
        print("\n----------===== Random Activity =====----------")
        print("=====-----=====-----=======-----=====-----=====")
        print(f"Activity: {data['activity']}")
        print(f"Type: {data['type']}")
        print(f"Participants:: {data['participants']}")


def  get_activity_by_type():
    """
    Let user choose an activity type and get a suggestion
    API: https://bored-api.appbrewery.com/filter?type={type}
    Types: education, recreational, social, diy, charity, cooking, relaxation, music, busywork
    """
    in_type=''
    while(in_type!='education' and in_type!='recreational' and in_type!='social'and in_type!='diy' and in_type!='charity' and in_type!='cooking' and in_type!='relaxation'and in_type!='music' and in_type!='busywork'):
        in_type=input("Select type: education, recreational, social, diy, charity, cooking, relaxation, music, busywork \nChoice: ")
    # Step 1: define our url and our endpoint (route)
    url = f'https://bored-api.appbrewery.com/filter?type={in_type}'
    
    # Step2: Make the requests
    response =requests.get(url)
    
    # Step3: Check what we got back
    # print("Status Code: ", response.status_code)
    # print("Raw Response: ", response.text)
    
    # Step4: Parse JSON data (make it something useful in python)
    if response.status_code == 200:
        data=response.json() #convert to python dictionary
        # print(f"parsed data : {data}")
        print(f"\n----------===== {in_type} activities =====----------")
        print("=====-----=====-----=======-----=====-----=====")
        for one_data in data:
            print(f"Activity: {one_data['activity']}")


def  get_activity_by_participants():
    """
    Get activity suggestions based on number of participants
    API: https://bored-api.appbrewery.com/filter?participants={number}
    """
    number=''
    while(not number.isdecimal()):
        number=input("How many participants?: ")
    # Step 1: define our url and our endpoint (route)
    url = f'https://bored-api.appbrewery.com/filter?participants={number}'
    
    # Step2: Make the requests
    response =requests.get(url)
    
    # Step3: Check what we got back
    # print("Status Code: ", response.status_code)
    # print("Raw Response: ", response.text)
    
    # Step4: Parse JSON data (make it something useful in python)
    if response.status_code == 200:
        data=response.json() #convert to python dictionary
        # print(f"parsed data : {data}")
        print(f"\n-----===== activities for {number} people =====-----")
        print("=====-----=====-----=======-----=====-----=====")
        for one_data in data:
            print(f"Activity: {one_data['activity']}")


def  show_menu():
    """Display the main menu"""
    print("\nBored Activity Finder")
    print("="  *  21)
    print("1. Get a random activity")
    print("2. Get activity by type")
    print("3. Get activity by participants")
    print("4.  Exit")

def  main():
    """Main function with menu loop"""
    print("Welcome to the Bored Activity Finder!")
    while  True:
        show_menu()
        try:
            choice  =  input("\nChoose an option (1-6): ")
            if  choice  ==  '1':
                get_random_activity()
            elif  choice  ==  '2':
                get_activity_by_type()
            elif  choice  ==  '3':
                get_activity_by_participants()
            elif  choice  ==  '4':
                print("Thanks for using Bored Activity Finder!")
                break
            else:
                print("Invalid choice! Please choose 1-4.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if  __name__  ==  "__main__":
    main()