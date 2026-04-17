# ================================
# Activity - 2 (API + Web Scraping)
# ================================

# Import Libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# ================================
# API Requests (CRUD Operations)
# ================================

# GET Request
get_resp = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("GET Response:", get_resp.json())

# POST Request
post_resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"id": 1, "title": "Hello", "body": "World"}
)
print("\nPOST Response:", post_resp.json())

# PUT Request
put_resp = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"id": 1, "title": "Updated", "body": "Updated Body"}
)
print("\nPUT Response:", put_resp.json())

# DELETE Request
delete_resp = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print("\nDELETE Status Code:", delete_resp.status_code)

# HEAD Request
head_resp = requests.head("https://jsonplaceholder.typicode.com/posts/1")
print("\nHEAD Headers:", head_resp.headers)


# ================================
# Convert DataFrame to CSV
# ================================
# (Assuming filtered_data already exists)

df = pd.DataFrame(filtered_data)
df.to_csv("filtered_data.csv", index=False)


# ================================
# Web Scraping using BeautifulSoup
# ================================

# Fetch Webpage
response = requests.get("https://www.geeksforgeeks.org/java/java/")
soup = BeautifulSoup(response.content, "html.parser")

# Pretty Print HTML
print("\nParsed HTML:\n", soup.prettify())

# Extract Article Content
content = soup.find("div", class_="article-content")

if content:
    for para in content.find_all("p"):
        print(para.text.strip())
else:
    print("No article content found")



import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# -------------------------------
# 1. Send Request
# -------------------------------
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# -------------------------------
# 2. Parse HTML
# -------------------------------
soup = BeautifulSoup(response.text, "html.parser")

# -------------------------------
# 3. Extract Data
# -------------------------------
quotes = []
authors = []
tags_list = []

items = soup.find_all("div", class_="quote")

for item in items:
    # Quote text
    quote = item.find("span", class_="text").text
    
    # Author
    author = item.find("small", class_="author").text
    
    # Tags
    tags = [tag.text for tag in item.find_all("a", class_="tag")]
    tags = ", ".join(tags)
    
    quotes.append(quote)
    authors.append(author)
    tags_list.append(tags)

# -------------------------------
# 4. Create DataFrame
# -------------------------------
df = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags_list
})

# -------------------------------
# 5. Data Cleaning
# -------------------------------

# Remove special quotes (“ ”)
df["Quote"] = df["Quote"].apply(lambda x: re.sub(r'[“”"]', '', x))

# Remove extra spaces
df["Quote"] = df["Quote"].str.strip()

# Clean author names
df["Author"] = df["Author"].str.strip()

# -------------------------------
# 6. Save to CSV
# -------------------------------
df.to_csv("quotes_data.csv", index=False)

# -------------------------------
# 7. Output
# -------------------------------
print(df.head())