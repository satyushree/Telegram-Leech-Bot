from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1476931837:AAFVU1wy7Y9WKh-lxOx5XYPUsnIT5Mt_f3E"
    APP_ID = 1309280
    API_HASH = "af327dd857e0e65f80fefcf6d0af4afd"
    OWNER_ID = 1243382770
    AUTH_CHANNEL = [-1001195135562]
    DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[ffmg]
type = drive\n
client_id = 437611717237-cohifba2pi09vdkg8i4osf9t58tqj8er.apps.googleusercontent.com\n
client_secret = 1QAQdobw0XXAAfZjRn0ITF6w\n
scope = drive\n
root_folder_id = 1Ss-FUl2rRaTiLk1lq74yAcmj5i8dPJXj\n
token = {"access_token":"ya29.A0AfH6SMA9J7PDzd-5V-8OlOcfVO4Mc_GZSQ-0PsnQWuXZXTIcka2ljreP9cRLvkPxI_rlbR6LHGSafMHt7ZVjSA4reSNAehEw00lAR8_-QgxUa-dUqr_ocVHLbS84lPCzKIH8P7lAWdwzDwVte1u0yH-0Hjzd","token_type":"Bearer","refresh_token":"1//0gNvii4scilMBCgYIARAAGBASNwF-L9IroVv4pg_aTu627eGOpNv7HjRxjUOof_OFCxGOdHA2Af2tUgB0YsRGsxrSdVRMBNNKyqc","expiry":"2021-02-07T18:59:45.7438573+05:30"}\n
team_drive = 0AKM0e85jWxEpUk9PV
"""
