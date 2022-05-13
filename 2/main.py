from pprint import pprint
import requests
import os


TOKEN = ''

class YaUploader:
    host = 'https://cloud-api.yandex.net/v1/disk/resources'
    
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json', 
            'Accept': 'application/json', 
            'Authorization': f'OAuth {self.token}'
        }
    def upload_link(self, file_path: str):
        url = f'{self.host}/upload'
        headers = self.get_headers()
        response = requests.get(f'{url}?path={file_path}', headers=headers)
        print(f'{url}?path={file_path}')
        pprint(response.json())
        return response.json().get('href')

    def upload_file(self, file_path: str, file_name):
        url = self.upload_link(file_path)
        headers = self.get_headers()
        response = requests.put(url, data=open(file_name, 'rb'), headers=headers)
        pprint(response.json())

    def new_list(self, path):
        headers = self.get_headers()
        requests.put(f'{self.host}?path={path}', headers=headers)
        print(f'{self.host}?path={path}')
    


if __name__ == '__main__':
    yadisk = YaUploader(TOKEN)
    yadisk.upload_file('file2.txt', '/home/vladpyrkov/Request/2/file2.txt')