import requests

def get_dummy_data():
    """
    Fetches a single post from a dummy API.
    Returns the post data as a dictionary if successful.
    """
    api_url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(api_url)

    if response.ok:
        data = response.json()
        return data
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None

if __name__ == "__main__":
    post = get_dummy_data()

    if post:
        print("Successfully fetched data from the API:")
        print(f"User ID: {post['userId']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body'][:50]}...") # Print a truncated version of the body
    else:
        print("Failed to fetch data.")