from tobrot.sample_config import Config

#read readme too before filling these stuffs

class Config(Config):
    TG_BOT_TOKEN= "1516163225:AAFNvtqWKHJcTYaGEtIziEw2DQpMdmvXw5A" #imp
    APP_ID = 1309280 #imp
    API_HASH = "af327dd857e0e65f80fefcf6d0af4afd" #imp
    AUTH_CHANNEL = [-1001485521459] #imp replace your_id with your id from telegram or delete
    INDEX_LINK = "https://shree.satyu.workers.dev"
    GLEECH_COMMAND = "gleech@TLeechr_Bot"
    YTDL_COMMAND = "ytdl@TLeechr_Bot"
    TELEGRAM_LEECH_COMMAND_G = "tleech@TLeechr_Bot"
    CLONE_COMMAND_G = "gclone@TLeechr_Bot"
    PYTDL_COMMAND_G = "pytdl@TLeechr_Bot"
    DESTINATION_FOLDER = "TorrentLeech-Gdrive"
    LEECH_COMMAND = "leech@TLeechr_Bot"
    RCLONE_CONFIG = """[TorrentGenerator_Bot]
type = drive
scope = drive
root_folder_id = 1Ss-FUl2rRaTiLk1lq74yAcmj5i8dPJXj
token = {"access_token":"ya29.A0AfH6SMCnpzkVSL96IiMcNKef1Q0tAgqaJ9UqIIf-vBqzNQ2911iGQE5pJAjIapCipbtlC441sHStj84tXXPRxwE_qxb7E2E3xwq79wobky6Ow6flhk366Ld1LXncVodgJDke0lUV8c5saRLBimrn0pgsmHvb","token_type":"Bearer","refresh_token":"1//0g4JPYyDMkDucCgYIARAAGBASNwF-L9IrebVKrFnIdxrCVqK1Id-Ot6qdZPPSg-Bkn3iqIg07KkpPcE2ESiuS25Ymk7p4gGsJccY","expiry":"2021-02-24T19:54:46.0239209+05:30"}
team_drive = 0AKM0e85jWxEpUk9PVA """
    #put your config(replacing new lines with \n) in triple quote like above: """<your one liner config>"""
