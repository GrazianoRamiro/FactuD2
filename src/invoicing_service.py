import math
import numpy as np
import pandas as pd

from invoicing_rpa import InvoicingRPA


class InvoicingService:
    @classmethod
    def anonymous_invoicing(cls):
        try:
            amount = int(input("\nPlease enter amount to invoice: "))
        except ValueError:
            print("That's not a valid amount!")

        invoices = InvoicingService.calculate_invoices(amount)

        print(f"Invoices to generate: {invoices}")
        print(f"Total amount to be invoiced: {np.sum(invoices)}")

        while True:
            proceed = input("\nOk to proceed? [y]/n: ").lower()

            if proceed == "n":
                print("Aborting...")
                break
            elif proceed == "y" or proceed == "":
                print("Starting...")

                invoicingRPA = InvoicingRPA()
                invoicingRPA.log_in()

                for invoice_amount in invoices:
                    invoicingRPA.generate_invoice({"AMOUNT": invoice_amount})

                break

    @classmethod
    def named_invoicing(cls):
        invoices = pd.read_csv("clients.csv")

        invoices.CUIT = invoices.CUIT.astype(str)
        invoices.CONDITION = invoices.CONDITION.astype(str)

        print(f"\nInvoices to generate:\n {invoices}")
        print(f"\nTotal amount to be invoiced: {np.sum(invoices.AMOUNT)}")

        while True:
            proceed = input("\nOk to proceed? [y]/n: ").lower()

            if proceed == "n":
                print("Aborting...")
                break
            elif proceed == "y" or proceed == "":
                print("Starting...")

                invoicingRPA = InvoicingRPA()
                invoicingRPA.log_in()

                for _, invoice in invoices.iterrows():
                    invoicingRPA.generate_invoice(invoice)

                break

    @classmethod
    def calculate_invoices(cls, amount):
        invoice_limit = int(config["INVOICING_LIMIT"])
        invoices_quantity = math.floor(amount / invoice_limit)

        invoices = []

        for _ in np.arange(0, invoices_quantity):
            invoices.append(invoice_limit)

        remaining_amount = amount - invoice_limit * invoices_quantity

        if remaining_amount > 0:
            invoices.append(amount - invoice_limit * invoices_quantity)

        return invoices
