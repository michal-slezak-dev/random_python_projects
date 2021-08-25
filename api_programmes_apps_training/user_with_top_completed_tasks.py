import json
import requests
from collections import defaultdict


def count_completed_tasks_frequency(tasks):
    completedTasksByUser = defaultdict(int)

    for entry in tasks:
        if entry["completed"] == True:
            completedTasksByUser[entry["userId"]] += 1
    return completedTasksByUser


def get_users_with_top_frequency(frequency_dict):
    winning_users = []
    maxCompletedTaskFrequency = max(frequency_dict.values())

    for userId, numberOfCompletedTasks in frequency_dict.items():
        if numberOfCompletedTasks == maxCompletedTaskFrequency:
            winning_users.append(userId)
    return winning_users


def get_user_names_win(users_win_list, key="id"):
    conj_param = key + "="

    i = 0
    for item in users_win_list:
        i += 1
        if i == len(users_win_list):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&" + key + "="
    return conj_param


response = requests.get("https://jsonplaceholder.typicode.com/todos")
try:
    tasks = response.json()
except json.decoder.JSONDecodeError:
    print("NIEPRAWIDŁOWY FORMAT!")
else:
    completedTasksByUser = count_completed_tasks_frequency(tasks)
    users_win = get_users_with_top_frequency(completedTasksByUser)
# print(completedTasksByUser)
# print(users_win)


conj_param = get_user_names_win(users_win)
# print(conj_param)
response_users = requests.get(
    "https://jsonplaceholder.typicode.com/users", params=conj_param
)
users = response_users.json()

# print(users)

for user in users:
    print("Osoby, które dostają nagrodę to: ", user["name"])
