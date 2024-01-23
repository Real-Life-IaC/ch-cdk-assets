from greeting import generate_greeting


def lambda_handler(event: dict, context: dict) -> dict:
    """Lambda handler"""

    name = event.get("name", "World")
    message = generate_greeting(name)

    return {"message": message}
