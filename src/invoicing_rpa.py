from rpa import RPA
from env import config, constants
import time

from utils import get_start_and_end_of_month

elements = {
    "login_input_username": "F1:username",
    "login_btn_next": "F1:btnSiguiente",
    "login_input_password": "F1:password",
    "login_btn_submit": "F1:btnIngresar",
    "btn_next": "Continuar >",
    "btn_gen_receipts": "btn_gen_cmp",
    "select_sales_point": "puntodeventa",
    "select_concept": "idconcepto",
    "btn_start_date": "fsd_btn",
    "btn_end_date": "fsh_btn",
    "input_start_date": "fsd",
    "input_end_date": "fsh",
    "select_recipient_condition": "idivareceptor",
    "input_recipient_cuit": "nrodocreceptor",
    "form_recipient": "formulario",
    "check_payment_method_others": "formadepago7",
    "input_service_description": "detalle_descripcion1",
    "select_unit_of_measure": "detalle_medida1",
    "input_invoice_amount": "detalle_precio1",
    "btn_generate_invoice": "btngenerar",
    "input_main_menu": "Menú Principal",
}


class InvoicingRPA:
    def __init__(self):
        self.rpa = RPA()
        self.rpa.navigate(config["INVOICING_URL"])

    def log_in(self):
        username_input = self.rpa.find("input", "id", elements["login_input_username"])
        username_input.send_keys(config["INVOICING_USERNAME"])
        self.rpa.find_and_click("input", "id", elements["login_btn_next"])

        password_input = self.rpa.find("input", "id", elements["login_input_password"])
        password_input.send_keys(config["INVOICING_PASSWORD"])
        self.rpa.find_and_click("input", "id", elements["login_btn_submit"])

        self.rpa.find_and_click("input", "value", config["INVOICING_COMPANY"])

    def generate_invoice(self, invoice):
        self.step_generate_receipt()
        self.step_sales_point()
        self.step_emission_details()
        self.step_recipient_details(
            invoice.get("CUIT", ""), invoice.get("CONDITION", "")
        )
        self.step_operation_details(invoice.get("AMOUNT", ""))
        self.step_generate()

    def step_generate_receipt(self):
        self.rpa.find_and_click("a", "id", elements["btn_gen_receipts"])
        time.sleep(0.9)

    def step_sales_point(self):
        sales_point_input = self.rpa.find(
            "select", "id", elements["select_sales_point"]
        )
        time.sleep(0.9)
        sales_point_input.select_by_index(constants["sales_point_index"])
        time.sleep(0.5)
        self.next_step()

    def step_emission_details(self):
        concept_input = self.rpa.find("select", "id", elements["select_concept"])
        concept_input.select_by_index(constants["concept_services_index"])
        time.sleep(0.5)

        start_date, end_date = get_start_and_end_of_month()

        start_date_input = self.rpa.find("input", "id", elements["input_start_date"])
        start_date_input.clear()
        start_date_input.send_keys(start_date)

        end_date_input = self.rpa.find("input", "id", elements["input_end_date"])
        end_date_input.clear()
        end_date_input.send_keys(end_date)

        self.next_step()

    def step_recipient_details(self, cuit, condition):
        iva_condition_input = self.rpa.find(
            "select", "id", elements["select_recipient_condition"]
        )
        iva_condition_input.select_by_index(condition or "3")

        cuit_input = self.rpa.find("input", "id", elements["input_recipient_cuit"])
        cuit_input.send_keys(cuit or "")

        self.rpa.find_and_click("form", "id", elements["form_recipient"])
        time.sleep(0.5)

        self.rpa.find_and_click("input", "id", elements["check_payment_method_others"])
        self.next_step()

    def step_operation_details(self, amount):
        service_input = self.rpa.find(
            "textarea", "id", elements["input_service_description"]
        )
        service_input.send_keys(constants["service_description"])
        self.rpa.wait()

        unit_of_measure_input = self.rpa.find(
            "select", "id", elements["select_unit_of_measure"]
        )
        unit_of_measure_input.select_by_index(constants["unit_of_measure_units_index"])
        self.rpa.wait()

        amount_input = self.rpa.find("input", "id", elements["input_invoice_amount"])
        amount_input.send_keys(amount)
        self.next_step()

    def step_generate(self):
        self.rpa.find_and_click("input", "id", elements["btn_generate_invoice"])
        time.sleep(0.9)

        self.rpa.accept_alert()
        time.sleep(0.9)

    def next_step(self):
        next_step_btn = self.rpa.find("input", "value", elements["btn_next"])
        next_step_btn.click()
        time.sleep(0.5)
        return

    def return_to_main_menu(self):
        self.rpa.find_and_click("input", "value", elements["input_main_menu"])
