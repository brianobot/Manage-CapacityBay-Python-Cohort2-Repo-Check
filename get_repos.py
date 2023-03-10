import requests

api_url = f"https://api.github.com/users/"


def get_all_repos(user):
    """return a list of repos dict attributes associated with a particular github user"""
    pass


def get_repo_by_name(username, repo_name):
    """return dictionary data on a particular repo associated with a particular user """
    response_data = requests.get(api_url+f"repos/{username}/{repo_name}")
    return response_data.json()


