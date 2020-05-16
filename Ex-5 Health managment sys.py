# # Health Managment system
#
# Manage 3 clients data - Amit, Ankit, mohit
# make 6 files - 3 for diet and 3 for exercises record
# how program will works:
# asks for client name - 3 options to choose
# asks for log data or retrieve data - two options
# ask about diet or exercise
#
# How data will store:   [display time] exercise name or diet name   and display client name at above


'''=============FIRST ATTEMPT==========='''
# print(":: Health Managment System ::\n\n")
# # FOR LOGGING THE DATA
# def log_data():
#     client_name = int(input("Press 1 for Amit\nPress 2 for Ankit\nPress 3 for Mohit\n"))
#     if client_name == 1:
#         d_or_e = int(input("What you want to log - \nPress 1 for diet\nPress 2 for exercise\n"))
#         if d_or_e == 1:
#             with open("amit_diet.txt","a") as f:
#                 diet_log = input("Enter what you eat today - \n")
#                 f.write(diet_log)
#         else:
#             with open("amit_exercise.txt", "a") as f:
#                 exe_log = input("Enter which exercise you do todya - \n")
#                 f.write(exe_log)

#     elif client_name == 2:
#         d_or_e = int(input("What you want to log - \nPress 1 for diet\nPress 2 for exercise\n"))
#         if d_or_e == 1:
#             with open("ankit_diet.txt", "a") as f:
#                 diet_log = input("Enter what you eat today - \n")
#                 f.write(diet_log)
#         else:
#             with open("ankit_exercise.txt", "a") as f:
#                 exe_log = input("Enter which exercise you do today - \n")
#                 f.write(exe_log)

#     elif client_name == 3:
#         d_or_e = int(input("What you want to log - \nPress 1 for diet\nPress 2 for exercise\n"))
#         if d_or_e == 1:
#             with open("mohit_diet.txt", "a") as f:
#                 diet_log = input("Enter what you eat today - \n")
#                 f.write(diet_log)
#         else:
#             with open("mohit_exercise.txt", "a") as f:
#                 exe_log = input("Enter which exercise you do today - \n")
#                 f.write(exe_log)

# # FOR RETRIEVING THE DATA

# def retrieve_data():
#     client_name = int(input("Press 1 for Amit\nPress 2 for Ankit\nPress 3 for Mohit\n"))
#     if client_name == 1:
#         d_or_e = int(input("What you want to retrieve - \nPress 1 for diet\nPress 2 for exercise\n"))
#         if d_or_e == 1:
#             with open("amit_diet.txt") as f:
#                 print(f.read())
#         else:
#             with open("amit_exercise.txt") as f:
#                 print(f.read())

#     elif client_name == 2:
#         d_or_e = int(input("What you want to retrieve - \nPress 1 for diet\nPress 2 for exercise\n"))
#         if d_or_e == 1:
#             with open("ankit_diet.txt") as f:
#                 print(f.read())
#         else:
#             with open("ankit_exercise.txt") as f:
#                 print(f.read())

#     elif client_name == 3:
#         d_or_e = int(input("What you want to retrieve - \nPress 1 for diet\nPress 2 for exercise\n"))
#         if d_or_e == 1:
#             with open("mohit_diet.txt") as f:
#                 print(f.read())
#         else:
#             with open("mohit_exercise.txt") as f:
#                 print(f.read())


# log_or_retrieve = int(input("Press 1 for log data\nPress 2 for retrieve data\n"))
# if log_or_retrieve == 1:
#     log_data()
# elif log_or_retrieve == 2:
#     retrieve_data()






'''===================SECOND ATTEMPT====================='''



    # Amit's Solution = Ex-5 Health Managment system

def gettime():
    import datetime
    return datetime.datetime.now()
def log_data():
    name = input("Enter your name: ")
    d_or_e = int(input("Press 1 for Diet\nPress 2 for Exercise"))
    if d_or_e == 1:
        with open(name + "_diet.txt", "a") as f:
            diet = input("Enter what you eat today: ")
            f.write(str([str(gettime())]) + "\t" + diet + "\n")
    elif d_or_e == 2:
        with open(name + "_exercise.txt", "a") as f:
            exercise = input("Enter which exercise you perform today: ")
            f.write(str([str(gettime())]) + "\t" + exercise + "\n")

def retrieve_data():
    name = input("Enter your name: ")
    d_or_e = int(input("Press 1 for Diet\nPress 2 for Exercise"))
    if d_or_e == 1:
        with open(name + "_diet.txt") as f:
            print(f"{name.title()}  ,you eat:\n" + f.read())
    elif d_or_e == 2:
        with open(name + "_exercise.txt") as f:
            print(f"\n{name.title()} ,you perform following exercises:\n" + f.read())

        
print("\t\t\t::Health Managment System:: \n\n")
inp = int(input("What you want to do-\nPress 1 for log data\nPress 2 for retrieve data"))
if inp == 1:
    log_data()
elif inp == 2:
    retrieve_data()

