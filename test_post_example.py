
""" This test uses Playwright’s API request context to send a POST request to an external API, 
    validate the response status and body, and demonstrate API automation without launching a browser
"""
from playwright.sync_api import Playwright

def test_create_post_api(playwright: Playwright):
    # Create API request context-This creates an isolated API client, similar to a Postman collection
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
    )

    # Send POST request-
    response = api_context.post(
        "/posts",
        data={
            "title": "Playwright API Test",
            "body": "Testing API using Playwright Python",
            "userId": 1
        }
    )

    # Display output
    print("Status Code:", response.status)
    print("Response Body:", response.json())

    # Assertions
    assert response.status == 201
    assert response.json()["title"] == "Playwright API Test"
