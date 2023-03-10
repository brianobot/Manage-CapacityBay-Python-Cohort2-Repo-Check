import requests
from get_repos import get_all_repos, get_repo_by_name
from prettytable import PrettyTable

# initialize and clean the student list
students = open('student_github_username.txt').readlines()
students = sorted([student.strip() for student in students])

repo_name = "CapacityBay-Python-Cohort-2"


print("###########################################################")
print(f"Current Registered Students : Total Number: {len(students)}")
print("###########################################################")
for index, student in enumerate(students, start=1):
    print(index, ": ", student)


table = PrettyTable()
table.field_names = ["Student Name", "Repo Name", 'status', "Created Date"]


for student in students:
    response_data = get_repo_by_name(student, repo_name)
    
    if response_data['message'] == "Not Found":
        print(f"{repo_name} Not FOund! for STudent = {student}")
        table.add_row([student, repo_name, "Not Found", None])
    
    elif response_data['message'].startswith("API rate limit exceeded for"):
        print("----------------------------------------------------------------------------")
        print("FAILED! API rate limited! Try Again Later or Use Authenticated API Requests")
        print("----------------------------------------------------------------------------")

    else:
        print('reponse = ', response_data)
        table.add_row([student, repo_name, "Found", response_data['created_at']])



if __name__ == "__main__":
    print(table)