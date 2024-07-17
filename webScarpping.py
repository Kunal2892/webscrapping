from bs4 import BeautifulSoup
import requests

url = 'https://hprera.nic.in/PublicDashboard'

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    print("Webpage fetched successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")
    response = None

if response and response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with id 'reg-Projects'
    reg_projects_div = soup.find('div', id='reg-Projects')

    if reg_projects_div:
        # Find all project elements within this div
        projects = reg_projects_div.find_all('div', class_='px-2 pt-2', limit=6)

        if projects:
            # Print the first 6 projects with some formatting
            for i, project in enumerate(projects, start=1):
                print(f"Project {i}:")
                print(project.get_text(strip=True))  # Extract and print the text content of each project
                print("-" * 50)
        else:
            print("No project elements found within the specified div.")
    else:
        print("Element with id 'reg-Projects' not found.")
else:
    print("Unable to fetch the webpage")
