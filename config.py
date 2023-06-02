import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21288218")

API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6067754375:AAGVGSGTqaiJ2vziLKcbr43tnyY54rc3p3g") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Kdramaland_official") 

DB_NAME = os.environ.get("DB_NAME","User_Data")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://RENAMESNOWPROBOT:RENAMESNOWPROBOT@cluster0.uaf4ivm.mongodb.net/?retryWrites=true")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/f97e69d8f524048e6f908.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6065594762').split()]

PORT = os.environ.get("PORT", "8080")
