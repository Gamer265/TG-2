from forwarder.sample_config import Config

class Development(Config):
    API_KEY = "5076883469:AAHBE3rqirV3AL8hiYvl6bok_0AW6pghsqg"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001331185454,-1001440212716,-1001641752361,-1001396178915,-1001416330356,-1001403795963,-1001787156904,-1001777242213]
    TO_CHATS = [-1001707942957]
   
    REMOVE_TAG = False
    WORKERS = 32
    
