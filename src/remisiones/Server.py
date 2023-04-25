from dotenv import load_dotenv
import os
load_dotenv()


url = str(os.environ.get("URL_REMISIONES"))
port = int(os.environ.get("PORT_REMISIONES"))