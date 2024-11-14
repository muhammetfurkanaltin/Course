import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "TOKEN" 

    def getUser(self, username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()

    def getRepositories(self, username):
        response = requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()

    def createRepository(self, name):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        data = {
            "name": name,
            "description": "This is your first repository",
            "homepage": "https://github.com/muhammetfurkanaltin",
            "private" : False,
            "has_issues": True,
            "has_wiki": True
        }
        response = requests.post(self.api_url + '/user/repos', headers=headers, json=data)
        return response.json()

github = Github()

while True:
    secim = input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeciminiz: ")

    if secim == "4":
        break

    elif secim == "1":
        username = input("username: ")
        result = github.getUser(username)
        print(f"Name: {result['name']} Public repos: {result['public_repos']} Followers: {result['followers']}")

    elif secim == "2":
        username = input("username: ")
        result = github.getRepositories(username)
        for repo in result:
            print(repo['name'])

    elif secim == "3":
        name = input('Repository name: ')
        result = github.createRepository(name)
        print(result)

    else:
        print("Yanliş seçim")

