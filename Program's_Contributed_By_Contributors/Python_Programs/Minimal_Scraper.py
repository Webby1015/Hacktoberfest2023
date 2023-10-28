# pip install requests

import requests

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was not successful
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        return str(e)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    html_content = get_html_content(url)
    print("HTML Content:")
    print(html_content)
