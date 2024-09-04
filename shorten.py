import requests

def shorturl(longurl):
        
        response = requests.get(f'http://tinyurl.com/api-create.php?url={longurl}')
        
        
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: Unable to shorten URL. Status code: {response.status_code}"


longurl = input("Enter the URL to shorten: ")
shorturl = shorturl(longurl)
print(f"Shortened URL: {shorturl}")
