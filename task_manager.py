"""
import date today's date using datetime with correct formatting of dd/abbr mon/yyyy
create constant variables for colour formatting
"""
import datetime

today = datetime.datetime.today()
today_date = today.strftime("%d %b %Y")

BLUE = '\033[94m'
GREEN = '\033[92m'
WHITE = '\033[0m'
RED = '\033[91m'
BOLD = '\033[1m'

"""
create function to find matching values in two different dictionaries 
store them in a list
"""


def match_values(dict_one, dict_two):
    match_values_list = []
    for key in dict_one:
        if key in dict_two:
            match_values_list.append(dict_one[key])
    return match_values_list


"""
create function that takes two dictionaries and calculates percentage of completed tasks
for each key in the our dict of completed tasks we divide it by the corresponding key of total task count dict
use if else statement to handle 0 value keys and return 0 as our answer 
"""


def dict_percentages(completed_dict, count_dict):
    percentage_completed = {key: (completed_dict[key] / count_dict[key]) * 100 if completed_dict[key] != 0 else
                            0 for key in completed_dict if key in count_dict}
    return percentage_completed


"""
create function to count number of lines in a file
"""


def line_count(file):
    with open(file, 'r') as open_file:
        lines = open_file.readlines()
        num_lines = len(lines)
    return num_lines


"""
create function to count number of times the username from one file occurs in another file
set default value for key as 0
of line starts with username then add one to the value of the corresponding key
store in new dict
username is always the first word in on a line of a file
"""


def check_usernames(file1, file2):
    with open(file1, 'r') as users:
        user_lines = users.readlines()
    with open(file2, 'r') as tasks:
        task_lines = tasks.readlines()
    counts = {}
    for line_users in user_lines:
        username_ = line_users.strip().split()[0]
        counts[username_] = 0
        for line_tasks in task_lines:
            if line_tasks.startswith(username_):
                counts[username_] += 1
    return counts


"""
create function to mark a task complete should take file username and user choice of task 
create count equal to zero
for each line in our file if it starts with the username of user add one to the count
when count equals user task choice number
change the No at end of line to Yes.
write the lines back to file
print message to let user know task is completed
"""


def mark_complete(file, username_, user_choice):
    with open(file, 'r') as open_file:
        lines = open_file.readlines()
    count = 0
    for i, line in enumerate(lines):
        if line.startswith(username_):
            count += 1
            if count == user_choice:
                words = line.strip().split(" ")
                words[-1] = "Yes"
                new_line = " ".join(words)
                lines[i] = new_line + '\n'
                break
    with open(file, 'r+') as open_file:
        open_file.writelines(lines)
        print(f"\n{GREEN}TASK MARKED COMPLETE")


"""
create function to edit task, takes file, user task choice, edit choice
create count equal to zero
for each line in our file if it starts with the username of user add one to the count
when count equals user task choice number edit the users chosen piece of data
request user input for updated data
print message to let user that their selected data was edited
write result back to file
"""


def edit_task(file, user_choice, edit_choice, username_):
    with open(file, 'r+') as open_file:
        lines = open_file.readlines()
    count = 0
    for i, line in enumerate(lines):
        if line.startswith(username_):
            count += 1
            if count == user_choice:
                words = lines[i].strip().split(" ")
                if edit_choice == 'username':
                    new_username = input("Enter a the updated username for this task: ")
                    words[0] = new_username + ","
                    new_line = " ".join(words)
                    lines[i] = new_line + '\n'
                    print(f"\n{GREEN}{edit_choice.capitalize()} successfully updated!")
                elif edit_choice == 'due date':
                    new_date = input("Enter the updated due date for this task (e.g. 21 Jan 2023): ").title() + ","
                    words[-4:-1] = new_date.split()
                    new_line = " ".join(words)
                    print(f"\n{GREEN}{edit_choice.capitalize()} successfully updated!")
                    lines[i] = new_line + '\n'
    with open(file, 'r+') as open_file:
        open_file.writelines(lines)


"""
create function to check whether or not a task is completed
create count equal to zero
for each line in our file if it starts with the username of user add one to the count
when count equals user task choice number check if last word of line is 'No'
if No request user input
if input is username or due date run edit task function
else print message to tell user than input was invalid and re request choice
if Yes inform user that the task is already completed
"""


def is_complete(file, user_choice, username_):
    with open(file, 'r+') as open_file:
        lines = open_file.readlines()
    count = 0
    for i, line in enumerate(lines):
        if line.startswith(username_):
            count += 1
            words = lines[i].strip().split(" ")
            if count == user_choice:
                if words[-1] == 'No':
                    data_choice = input("Would you like to edit the username assigned to or the due date? \n").lower()
                    if data_choice == 'username' or 'due date':
                        edit_task('tasks.txt', user_choice, data_choice, username_)
                        break
                    else:
                        print(f"\n{RED}Invalid input please try again\n")
                        continue
            elif words[-1] == 'Yes':
                print(f"\n{RED}Task already completed, please select another task")
                break


"""
create function to find whether a task is overdue which takes a file as an argument
open file as readable
count equals zero
for each line in the file create a list of the words in the line
join the last 4th,3rd and second last items in the list to a new string
remove the comma form the end of the string
convert the string to an object using strptime
if the date today is less than todays date and it is uncomplete count as overdue
"""


def is_overdue(file):
    with open(file, "r") as open_file:
        count = 0
        for line in open_file:
            words = line.split()
            date_string = ' '.join(words[-4:-1])
            date_string = date_string[:-1]
            date_object = datetime.datetime.strptime(date_string, "%d %b %Y")
            if date_object < today and words[-1] == 'No':
                count += 1
        return count


"""
create function to find tasks belonging to each user that are overdue and uncompleted
open both user and task files
create variables for each using readlines
create empty dictionary
store each username in dict with default value of 0
find due date of task of each line and if less than todays date then task is overdue
if line starts with username from dict and ends in no and is overdue, add one to the value of that dict key
return dict
"""


def uncompleted_overdue(file1, file2):
    with open(file1, 'r') as users:
        user_lines = users.readlines()
    with open(file2, 'r') as tasks:
        task_lines = tasks.readlines()
    counts = {}
    for line_users in user_lines:
        username_ = line_users.strip().split()[0]
        counts[username_] = 0
    for line_tasks in task_lines:
        username_ = line_tasks.strip().split()[0]
        words = line_tasks.split()
        date_string = ' '.join(words[-4:-1])
        date_string = date_string[:-1]
        date_object = datetime.datetime.strptime(date_string, "%d %b %Y")
        if line_tasks.startswith(username_) and line_tasks.strip().endswith('No') and date_object < today:
            counts[username_] += 1
    return counts


"""
create functions to count number of yes' and number of no's
for both functions:
open files create empty dict
store usernames from user file in empty dict with default value 0 
for yes count function if username is at start of line and line ends in yes add one to value
for no count function if username is at start of line and line ends in no add one to value
"""


def completed_count_yes(file1, file2):
    with open(file1, 'r') as users:
        user_lines = users.readlines()
    with open(file2, 'r') as tasks:
        task_lines = tasks.readlines()
    counts = {}
    for line_users in user_lines:
        username_ = line_users.strip().split()[0]
        counts[username_] = 0
        for line_tasks in task_lines:
            if line_tasks.startswith(username_) and line_tasks.strip().endswith('Yes'):
                counts[username_] += 1

    return counts


def completed_count_no(file1, file2):
    with open(file1, 'r') as users:
        user_lines = users.readlines()
    with open(file2, 'r') as tasks:
        task_lines = tasks.readlines()
    counts = {}
    for line_users in user_lines:
        username_ = line_users.strip().split()[0]
        counts[username_] = 0
        for line_tasks in task_lines:
            if line_tasks.startswith(username_) and line_tasks.strip().endswith('No'):
                counts[username_] += 1
    return counts


"""
create function register new users
open user text as readable file
check user is admin
if user admin allow to proceed and register user
request admin enters new username and password, confirm password
if password does not match give error message re request information
else write the new username and password to our user file
print message to user that registration was successful
if not admin give error message return to menu 
"""


def reg_user():
    while True:
        with open('user.txt', 'r+') as open_file:
            if username != 'admin':
                print(f"{RED}You do not have the authorisation to register new users.\n")
                break
            elif username == 'admin':
                new_name = input(f"\n{WHITE}Enter new username: ")
                if new_name + ',' in open_file.read():
                    print(f"\n{RED}Username already registered please try another!")
                    continue
                new_password = input("Enter new password: ")
                confirm = input("Confirm your new password: ")
                if confirm != new_password:
                    print(f"\n{RED}Please make sure your password matches!")
                    continue
                else:
                    open_file.write(f"\n{new_name}, {new_password}")
                    print(f"\n{GREEN}New user registered!")
                    break
        continue


"""
create function add task
open tasks file as a+
request relevant task data from user
write data to file
print message to user to say task added
"""


def add_task():
    with open('tasks.txt', 'a+') as open_file:
        user = input("\nEnter the username whom the task is assigned to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (e.g. 12 Jan 2023): ").title()
        complete = 'No'
        open_file.write(f"\n{user}, {task_title}, {task_description}, {today_date}, {due_date}, {complete}")
        print(f"\n{GREEN}Task added to file!")


"""
open tasks file as r plus
create output variable
split each line in file to a list
add each item from list to the user-friendly, formatted output string
print output
"""


def view_all():
    with open('tasks.txt', 'r+') as open_file:
        output = f'{BLUE}–' * 90
        for line in open_file:
            split_line = line.split(', ')
            output += "\n"
            output += f"Task:\t\t\t\t {split_line[1]}\n"
            output += f"Assigned to:\t\t {split_line[0]}\n"
            output += f"Date assigned:\t\t {split_line[3]}\n"
            output += f"Due Date:\t\t\t {split_line[4]}\n"
            output += f"Task Complete?\t\t {split_line[5]}\n"
            output += f"Task Description:\n\t{split_line[2]}\n"
            output += "-" * 90
        print(output)


"""
create function that will check if a user has any tasks to view
open file and convert to list
if username is not in list print error message and return true
else return false
"""


def task_check():
    with open('tasks.txt', 'r+') as open_file:
        read_file = open_file.read()
        file_list = read_file.split()
        if username + ',' not in file_list:
            print(f"\n{RED}NO TASKS FOUND! Please add tasks ('a') before trying again.")
            return True
        else:
            return False


"""
open tasks file as r+
for users in file print user friendly header
create count equal to one
create output dictionary
for each line in file split to a list
if username does not match the first item our line list skip that line
if username does equal the first item of each list line add to our dictionary for the count position
add one to count
print values from dictionary
request user task choice or whether they would like to return to menu
if user decides to go to menu then break
if user inputs number higher than length of list or lower than 0 print error message and re-request input
if input valid print user selection key's value from dictionary
ask user for edit choice
if choice is to mark complete call mark complete function, break
if choice is to edit task call edit task function, break
add exit to menu option
"""


def view_mine():
    with open('tasks.txt', 'r+') as open_file:
        title = (f'{BLUE}–' * 90 + f"\nFIND ALL ASSIGNED TASKS FOR '{username}' BELOW\n{'-' * 90}")
        print(title)
        count = 1
        output_dict = {}
        for line in open_file:
            split_line = line.split(', ')
            if username != split_line[0]:
                continue
            elif username == split_line[0]:
                output_dict[count] = (
                    f"Task {count}:\t\t\t\t {split_line[1]}\n"
                    f"Assigned to:\t\t {split_line[0]}\n"
                    f"Date assigned:\t\t {split_line[3]}\n"
                    f"Due Date:\t\t\t {split_line[4]}\n"
                    f"Task Complete?\t\t {split_line[5]}\n"
                    f"Task Description:\n\t{split_line[2]}\n"
                    f"{'-' * 90}"
                )
                count += 1
                continue
        while True:
            for values in output_dict.values():
                print(f"{BLUE}{values}")

            user_choice = int(input(f"\n{WHITE}Enter task number you wish to view (enter -1 for main menu): \n"))
            if user_choice == -1:
                break
            elif user_choice < 0 or user_choice > len(output_dict):
                print(f"{RED}You have selected an invalid option, please try again!\n")
                continue
            else:
                task_num = output_dict[user_choice]
                print(f"{BLUE}{'-' * 90}\n{task_num}")
                edit_choice = input(f"{WHITE}Please choose one of the following options:\n"
                                    "\tmc - mark task complete\n"
                                    "\tet - edit the task\n"
                                    "\t-1 - return to menu\n"
                                    "\t: ")
                if edit_choice == "mc":
                    mark_complete('tasks.txt', username, user_choice)
                    break
                elif edit_choice == "et":
                    is_complete('tasks.txt', user_choice, username)
                    break
                elif edit_choice == "-1":
                    break


"""
create function for task report that takes a file as an argument
open file and create empty output string
set completed and uncompleted count to 0 
for each line in file  if the last word is yes add one to completed count
else add one to uncompleted count
calculate percentage uncompleted using uncompleted and line_count function
calculate overdue by calling is_overdue function and line count function
add relevant data to output string for total tasks, completed tasks, uncompleted tasks, number overdue and percentages 
for uncompleted as well as overdue
write this output to a new file named task_overview
print message to tell user that report has been generated
"""


def task_report(file):
    with open(file, "r+") as open_file:
        output = ''
        completed_count = 0
        uncompleted_count = 0
        lines = open_file.readlines()
        for line in lines:
            split_line = line.split()
            if split_line[-1] == "Yes":
                completed_count += 1
            else:
                uncompleted_count += 1
        percentage_uncompleted = (uncompleted_count / line_count('tasks.txt')) * 100
        percentage_overdue = (is_overdue('tasks.txt') / line_count('tasks.txt')) * 100
        output += f"The total number of tasks generated is: {line_count('tasks.txt')}\n"
        output += f"The total number of completed tasks is: {completed_count}\n"
        output += f"The total number of uncompleted tasks is: {uncompleted_count}\n"
        output += f"The total number of tasks overdue is: {is_overdue('tasks.txt')}\n"
        output += f"The percentage of uncompleted tasks is: {round(percentage_uncompleted, 2)}%\n"
        output += f"The percentage of overdue tasks is: {round(percentage_overdue, 2)}%"

    with open('task_overview.txt', 'w+') as new_file:
        new_file.write(output)
        print(f"\n{GREEN}Task overview report generated!\n")


"""
create function for user report which takes file as an argument
create empty output string
we will create new dictionaries calling functions for ease of user in calculations
create count dictionary by calling check usernames function
call yes count function to create dictionary containing how many tasks for each user have been completed
call no count function to create dictionary containing how many tasks for each user have not been completed
create dict of uncompleted and overdue count equal to uncompleted_overdue function using both files
add num users and num tasks to output variable using line_count function

create variable i equal to zero
while i is less than the length of our count dictionary
iterate through key and value of the count dictionary
remove comma from usernames
calculate percentage of tasks user has using their value for total tasks and number of total tasks for all users
call dict_percentage function to create new dict of percentage of own tasks completed
call dict_percentage function to create new dict of percentage of own tasks uncompleted
call match_values on percentage own completed and count dictionary for position i 
call match_values on percentage own uncompleted and count dictionary for position i
call match values on overdue and uncomplete dictionary and count dict to find overdue and incomplete percentage for i
add username to output 
their total tasks is the corresponding value
add percentage of total tasks to output
if percentage completed greater than 0 and less than 100 percentage completed equals 100 minus percentage uncompleted
else it is equal to our percentage completed variable
if value does not equal 0 calculate percentage using number overdue and uncomplete divided by value times 100
else if value is 0 then just add over_comp as our percentage
i plus one
round all calculation values to 2 decimal places for readablity 
write output to new file called user_overview.txt
print message to user to let them know report generated
"""


def user_report():
    output = ''
    count_dict = check_usernames('user.txt', 'tasks.txt')
    completed_dict_yes = completed_count_yes('user.txt', 'tasks.txt')
    completed_dict_no = completed_count_no('user.txt', 'tasks.txt')
    over_uncomp_dict = uncompleted_overdue('user.txt', 'tasks.txt')
    output += f"Total number of users is: {line_count('user.txt')}\n"
    output += f"Total number of tasks is: {line_count('tasks.txt')}\n"
    i = 0
    while i < len(count_dict):
        for key, value in count_dict.items():
            key = key[:-1]
            percentage_total_tasks = (value / line_count('tasks.txt')) * 100
            percentage_own_yes = dict_percentages(completed_dict_yes, count_dict)
            percentage_own_no = dict_percentages(completed_dict_no, count_dict)
            own_completed = match_values(percentage_own_yes, count_dict)[i]
            own_uncompleted = match_values(percentage_own_no, count_dict)[i]
            over_uncomp = match_values(over_uncomp_dict, count_dict)[i]
            output += f"\nStatistics for user '{key}'\n"
            output += f"Total tasks: {value}\n"
            output += f"Percentage of total tasks: {round(percentage_total_tasks, 2)}%\n"
            if 100 > match_values(percentage_own_yes, count_dict)[i] > 0:
                output += f"Percentage of own tasks completed: {round((100 - own_uncompleted), 2)}%\n"
            else:
                output += f"Percentage of own tasks completed: {round(own_completed, 2)}%\n"
            output += f"Percentage of own tasks uncompleted: {round(own_uncompleted, 2)}%\n"
            if value != 0:
                output += f"Percentage of own tasks uncompleted and overdue: {round(over_uncomp / value * 100, 2)}%\n"
            else:
                output += f"Percentage of own tasks uncompleted and overdue: {round(over_uncomp, 2)}%\n"
            i += 1

    with open('user_overview.txt', 'w+') as new_file:
        new_file.write(output)
        print(f"{GREEN}User overview report generated!")


"""
create function to view statistics
call task report and user report functions to ensure report files exist
print header
open task overview file 
print task overview header
print file
add formatting to show end of report

open user overview file
print header
print file
add formatting to show end of report
"""


def view_statistics():
    task_report('tasks.txt')
    user_report()
    print(f'{BLUE}–' * 90 + f'\nSTATISTICS\n' + '-' * 90)

    with open('task_overview.txt', 'r+') as open_file:
        print(f'{BLUE}–' * 90 + f'\nTASK OVERVIEW\n' + '-' * 90)
        print(open_file.read())
    print(f'{BLUE}–' * 90 + '\n')

    with open('user_overview.txt', 'r+') as open_file:
        print(f'{BLUE}–' * 90 + f'\nUSER OVERVIEW\n' + '-' * 90)
        print(open_file.read())
    print(f'{BLUE}–' * 90)
    print(f'{BLUE}–' * 90)


"""
open user file and create dictionary to store information in dictionary
"""
with open('user.txt') as f:
    login_dict = {k: v for line in f for (k, v) in [line.strip().split(None, 1)]}

"""
open user file as readable file
request username and password and inputs against dictionary
if username not in dictionary return error message and ask user to try again
do same for password
else if information matches dictionary sign user in
"""
with open('user.txt', 'r') as f:
    while True:
        username = input(f"{WHITE}Enter your username: ")
        password = input("Enter your password: ")
        if username + ',' not in login_dict:
            print(f"\n{RED}INVALID USERNAME OR PASSWORD! Please try again (Beware of case sensitivity).\n")
            continue
        elif password not in login_dict[username + ',']:
            print(f"\n{RED}INVALID USERNAME OR PASSWORD! Please try again (Beware of case sensitivity).\n")
            continue
        elif password in login_dict[username + ',']:
            print(f"\n{GREEN}You have successfully logged in!")
            break

"""
if user is not admin show standard menu 
request user choose one of menu options to register user, add task, view all tasks and view user specific tasks
lowercase user input to avoid input error
if user is admin add statistics and generate report option to standard menu
request admin chooses one of the options
lower to avoid input error
"""
while True:
    if username != 'admin':
        menu = input(f'\n{WHITE}Select one of the following Options below:\n'
                     f'r  - Registering a user\n'
                     f'a  - Adding a task\n'
                     f'va - View all tasks\n'
                     f'vm - View my tasks\n'
                     f'e  - Exit\n'
                     f': ').lower()
    else:
        menu = input(f'\n{WHITE}Select one of the following Options below:\n'
                     f'r  - Registering a user\n'
                     f'a  - Adding a task\n'
                     f'va - View all tasks\n'
                     f'vm - View my task\n'
                     f'vs - View statistics\n'
                     f'gr - Generate reports\n'
                     f'e  - Exit\n'
                     f': ').lower()

    """
    call corresponding function for menu option
    if menu option is vm call task choice function, if false go back to menu if true call view mine function
    if menu option is e exit program with message to user
    else let user know they have input an invalid option
    """

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()
        continue

    elif menu == 'va':
        view_all()
        continue

    elif menu == 'vm':
        if task_check():
            continue
        else:
            view_mine()
            continue

    elif menu == 'vs':
        view_statistics()
        continue

    elif menu == 'gr':
        task_report('tasks.txt')
        user_report()

    elif menu == 'e':
        print(f'\n{BLUE}Goodbye!!!')
        exit()

    else:
        print(f"\n{RED}You have made a wrong choice, Please Try again\n")
