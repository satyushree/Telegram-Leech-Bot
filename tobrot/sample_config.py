import os

# DO NOT EDIT THIS FILE
# DO NOT EDIT THIS FILE
# DO NOT EDIT THIS FILE
# DO NOT EDIT THIS FILE

# READ README FOR CONFIG


class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1516163225:AAFNvtqWKHJcTYaGEtIziEw2DQpMdmvXw5A")
    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 1309280))
    API_HASH = os.environ.get("API_HASH", "af327dd857e0e65f80fefcf6d0af4afd")
    OWNER_ID = int(os.environ.get("OWNER_ID", 1243382770))
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = set(int(x) for x in os.environ.get("AUTH_CHANNEL", "-1001485521459").split())
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    SP_LIT_ALGO_RITH_M = os.environ.get(
        "SP_LIT_ALGO_RITH_M",
        "hjs"
    )
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 30))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech@TLeechr_Bot")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl@TLeechr_Bot")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", """[TorrentGenerator_Bot]
type = drive
scope = drive
root_folder_id = 1Ss-FUl2rRaTiLk1lq74yAcmj5i8dPJXj
token = {"access_token":"ya29.A0AfH6SMCnpzkVSL96IiMcNKef1Q0tAgqaJ9UqIIf-vBqzNQ2911iGQE5pJAjIapCipbtlC441sHStj84tXXPRxwE_qxb7E2E3xwq79wobky6Ow6flhk366Ld1LXncVodgJDke0lUV8c5saRLBimrn0pgsmHvb","token_type":"Bearer","refresh_token":"1//0g4JPYyDMkDucCgYIARAAGBASNwF-L9IrebVKrFnIdxrCVqK1Id-Ot6qdZPPSg-Bkn3iqIg07KkpPcE2ESiuS25Ymk7p4gGsJccY","expiry":"2021-02-24T19:54:46.0239209+05:30"}
team_drive = 0AKM0e85jWxEpUk9PVA""")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "TorrentLeech-Gdrive")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech@TLeechr_Bot")
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://shree.satyu.workers.dev")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech@TLeechr_Bot")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel@TLeechr_Bot")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize@TLeechr_Bot")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status@TLeechr_Bot")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail@TLeechr_Bot")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail@TLeechr_Bot")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "False")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl@TLeechr_Bot")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log@TLeechr_Bot")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone@TLeechr_Bot")
    UPLOAD_COMMAND = os.environ.get("UPLOAD_COMMAND", "upload@TLeechr_Bot")
    RENEWME_COMMAND = os.environ.get("RENEWME_COMMAND", "renewme@TLeechr_Bot")
