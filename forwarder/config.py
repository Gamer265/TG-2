from forwarder.sample_config import Config

class Development(Config):
    API_KEY = "5076883469:AAHBE3rqirV3AL8hiYvl6bok_0AW6pghsqg"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001331185454,-1001440212716,-1001641752361,-1001396178915,-1001416330356,-1001403795963,-1001787156904,-1001777242213,-1001446423835,-1001512980117,-1001688123020,-1001519594625,-1001575537946,-1001564430294,-1001533184367,-1001537898136,-1001721377011,-1001366147158,-1001708952928]
    TO_CHATS = [-1001700407935]
   
    REMOVE_TAG = False
    WORKERS = 128
    
