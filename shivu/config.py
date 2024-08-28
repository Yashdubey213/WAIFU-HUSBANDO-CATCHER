class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6643029630"
    sudo_users = "6643029630", "7130472271"
    GROUP_ID =  -1002077799136
    TOKEN = "7318749803:AAHfbP321t9OtBAGsbY_CO6eUT29DD0Tv-I"
    mongo_url = "mongodb+srv://mehoca2283:q9unKKrK4gAZvf7U@cluster0.imuhxkw.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b30e42bc296a04a9400af.jpg", "https://telegra.ph/file/b30e42bc296a04a9400af.jpg"]
    SUPPORT_CHAT = "TALK_2_REL4TE"
    UPDATE_CHAT = "TALK_2_REL4TE"
    BOT_USERNAME = "Rio_songbot"
    CHARA_CHANNEL_ID = "-1002077799136"
    api_id = 25128421
    api_hash = "933fd8b53dabcf5c814c47a4f6911623"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
