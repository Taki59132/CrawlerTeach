import requests

if __name__ == "__main__":
    url = 'https://www.dcard.tw/f'
    response = requests.get(url)
    print(response)
    
    print(response.text)