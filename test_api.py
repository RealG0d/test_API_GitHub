import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
REPO_NAME = os.getenv('REPO_NAME')


def create_repo():
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'name': REPO_NAME,
        'description': 'Тестовый репозиторий',
        'public': True
    }
    response = requests.post(f'https://api.github.com/user/repos', headers=headers, json=data)
    if response.status_code == 201:
        print(f'Репозиторий {REPO_NAME} создан успешно')
    else:
        print(f'Ошибка создания репозитория: {response.text}')


def check_repo():
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.get(f'https://api.github.com/users/{GITHUB_USERNAME}/repos', headers=headers)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            if repo['name'] == REPO_NAME:
                print(f'Репозиторий {REPO_NAME} существует')
                return
        print(f'Репозиторий {REPO_NAME} не существует')
    else:
        print(f'Ошибка проверки репозитория: {response.text}')


def delete_repo():
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.delete(f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}', headers=headers)
    if response.status_code == 204:
        print(f'Репозиторий {REPO_NAME} удален успешно')
    else:
        print(f'Ошибка удаления репозитория: {response.text}')


if __name__ == '__main__':
    create_repo()
    check_repo()
    delete_repo()
