import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "INVOICING_USERNAME": os.getenv("INVOICING_USERNAME"),
    "INVOICING_PASSWORD": os.getenv("INVOICING_PASSWORD"),
    "INVOICING_COMPANY": os.getenv("INVOICING_COMPANY"),
    "INVOICING_URL": os.getenv("INVOICING_URL"),
}
