from dotenv import load_dotenv
import os
load_dotenv()


url = str(os.environ.get("URI_TUTORIAS"))
port = int(os.environ.get("PORT_TUTORIAS"))