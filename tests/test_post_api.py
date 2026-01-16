from playwright.sync_api import Playwright
from api.clients.posts_client import PostClient
from api.utils.env_loader import BASE_URL

def test_create_and_get_post(playwright: Playwright):


    # Create Playwright API context
    api_context = playwright.request.new_context(
        base_url=BASE_URL,
    )

    # Initialize API client
    post_client = PostClient(api_context)

    # Define POST payload
    payload = {
        "title": "Playwright API Test",
        "body": "Testing API using Playwright Python",
        "userId": 1
    }

    # Create post
    create_response = post_client.create_post(payload)
    print("Create response status:", create_response.status)
    print("Create response body:", create_response.json())

    assert create_response.status == 201
    response_json = create_response.json()
    assert response_json["title"] == payload["title"]
    post_id = response_json["id"]

    #Get the created post
    get_response = post_client.get_post(post_id)
    print("Get response status:", get_response.status)
    print("Get response body:", get_response.json())

    assert get_response.status == 200
    assert get_response.json()["id"] == post_id

    #Cleanup API context
    api_context.dispose()
