"""
Modulde containing utiliy functions to facilitate api interaction with the github api

CopyRight @ Brian Obot 2023
"""

import requests
import environ


env = environ.Env()

# reading .env file
environ.Env.read_env()

username = env("USER")
token = env("TOKEN")

api_url = f"https://api.github.com/"


def get_all_repos(user):
    """return a list of repos dict attributes associated with a particular github user"""
    pass


def get_repo_by_name(username, repo_name):
    """return dictionary data on a particular repo associated with a particular user """
    response_data = requests.get(api_url + f"repos/{username}/{repo_name}", auth=(username, token))
    return response_data.json()


def get_repo_content(user, repo_name, file_path):
    """ return dictionary data on the content of a particular user's github repo """
    response_data = requests.get(api_url + f"repos/{username}/{repo_name}/content/{file_path}", auth=(username, token))
    return response_data.json()