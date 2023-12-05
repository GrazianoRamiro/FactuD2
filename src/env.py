import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "INVOICING_USERNAME": os.getenv("INVOICING_USERNAME"),
    "INVOICING_PASSWORD": os.getenv("INVOICING_PASSWORD"),
    "INVOICING_COMPANY": os.getenv("INVOICING_COMPANY"),
    "INVOICING_URL": os.getenv("INVOICING_URL"),
    "INVOICING_LIMIT": os.getenv("INVOICING_LIMIT"),
}

constants = {
    "sales_point_index": "1",
    "concept_services_index": "2",
    "service_description": "Servicios Informaticos",
    "unit_of_measure_units_index": "7",
}
