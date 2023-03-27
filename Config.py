import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "25831196"))
    API_HASH = os.environ.get("API_HASH", "84ffda4305e49d8d4a164f53ebcfeac2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5956936783:AAHYbZcYDSlG2vTfrAOtrK2ctbbMRCfVVL4")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLEBu4DPeJvP643CpDoHP-S2_W2X6Hr0ScM5yUL-FjTXGGLNGHJcJQNpxKjcVIbDguPxfQAShw9mSEJT8VWQernezeBittO0GWcHMbLpBAt6QNDEhNIGeBHOky_PJVZhB6nNu601gmJR8DpxPkesCUpZ9SSK4A75N9aEgYOIbYCAy1UXxNTFv9CeC0J31sGHNQmtBvGX5XR3yeQaYS02_3KQCJzCNr2XuEyjBf7pC9EvlTfbHMBLoYLb6-BVO3mZqZUs2S2J66V0Hd3WBW6VWyOuc8OOtyfE49y32c3Av3by25-5czJH4xm7gDHdFSb5mKMWGtQ8C499AhAQpEe-k5LCdsg=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "GroovyTBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
