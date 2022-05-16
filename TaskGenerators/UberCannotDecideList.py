
from todoist.api import TodoistAPI
import random
import config

key = config.API_TOKEN
projectId = config.PROJECT_ID_UberCannotDecideList
api = TodoistAPI(key)
api.sync()
listWithAllUberListTasks = []

for project in api.state['items']:


    if(project["project_id"] == projectId):
        listWithAllUberListTasks.append(project["content"])

print(random.choice(listWithAllUberListTasks))

