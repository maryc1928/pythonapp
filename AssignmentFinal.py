import csv

def print_menu():
    print("Microsoft Customer Portal")
    print("1. Add New record")
    print("2. View Existing records")
    print("3. Delete Record")
    print("4. Exit")


def new_customer():
    quit_func =(input("Press Q to Return to Main menu or any key to continue: ")).strip()
    if quit_func == "Q":
        return
    my_list = []
    while True:
        try:
            ID = int(input("ID:"))
            break
        except ValueError:
            print("Please enter a whole number")
    my_list.append(ID)
    Engagement_name = input("Engagement Name:")
    my_list.append(Engagement_name)
    while True:
        try:
            Engagement_stage = int(input("Engagement Stage 1-5 :"))
            if Engagement_stage in range(0,6):
                break
        except:
                print("Invalid Input")
    my_list.append(Engagement_stage)
    Milestone_name = input("Milestone Name:")
    my_list.append(Milestone_name)
    while True:
        try:
            Next3MonthsPipeline=float(input("Next 3 Months Pipeline:"))
            break
        except ValueError:
            print("Please enter numerical values")
    my_list.append(Next3MonthsPipeline)
    while True:
        try:
            Pipeline = float(input("Pipeline:"))
            break
        except ValueError:
            print("Please enter numerical values")
    my_list.append(Pipeline)
    while True:
        Engagement_owner = (input("Engagement Owner Alias:"))
        if Engagement_owner.isalpha():
            break
        print("Letters only please")
    my_list.append(Engagement_owner)
    while True:
        try:
            Days_in_current_stage = int(input("Days in current stage:"))
            break
        except ValueError:
                print("Please enter in whole numbers")
    my_list.append(Days_in_current_stage)


    with open('customerdataV3.csv', 'a+',newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(my_list)
    print("Thank you, your details have been saved")




def delete_record():

    quit_func=input("Enter Q to return to main menu or any key to continue: ")
    if quit_func == "Q":
        return

    with open('customerdataV3.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in read_obj:
            print(row)

    with open("customerdataV3.csv", 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        idnum = input("Enter the ID Number in whole numbers of the record you wish to remove from file: ")
        try:
            number= int(idnum)
        except ValueError:
            print("Invalid Entry ")
        else:
            for line in lines:
                if not idnum in line.split(',')[0]:
                    f.write(line)
            f.truncate()
            print("Thank you, your record has been deleted")

def show_record():
    quit_func = input("Enter Q to return to main menu or any key to continue: ")
    if quit_func == "Q":
        return
    with open('customerdataV3.csv', 'r') as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in read_obj:
            print(row)


def exit_menu():
    print('Thank you for using the Microsoft Customer Portal')
    exit()

while True:
    print("Microsoft Customer Portal")
    print("1. New Customer")
    print("2. Remove a record")
    print("3. Show all records")
    print("4. Exit")
    choice=(input('Enter your choice:')).strip()

    if choice == '1':
        new_customer()
    elif choice == '2':
        delete_record()
    elif choice == '3':
        show_record()
    elif choice == '4':
        exit_menu()
    else:
        print("Please enter a valid choice ")