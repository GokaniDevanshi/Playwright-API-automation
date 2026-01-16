class PostClient:
    def __init__(self, api_context):
        self.api_context = api_context

    def create_post(self, payload):
        # Use JSON
        return self.api_context.post("/posts", data=payload)

    def get_post(self, post_id):
        return self.api_context.get(f"/posts/{post_id}")
