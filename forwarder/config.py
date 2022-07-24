from forwarder.sample_config import Config

class Development(Config):
    API_KEY = "5076883469:AAHBE3rqirV3AL8hiYvl6bok_0AW6pghsqg"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001542591369,-1001440212716]
    TO_CHATS = [-1001703238624]
   
    REMOVE_TAG = False
    WORKERS = 16
    
