from dotenv import load_dotenv
import os
load_dotenv()


url = str(os.environ.get("URLGESTIONUSUARIOS"))
port = int(str(os.environ.get("PUERTOGESTIONUSUARIOS")))