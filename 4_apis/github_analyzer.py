import requests 

def analyze_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
   
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Public Repos: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
        print(f"Following: {data['following']}")
    else:
        print("User not found")

if __name__ == "__main__":
    analyze_github_user(input("Enter the github username: "))
    
