1. Test Case: Valid Login Credentials
   Inputs:

- CUIT: "12345678901"
- PASSWORD: "password123"
- COMPANY: "MyCompany"

Expected Output:

- The script should successfully login to the AFIP website and select the "MyCompany" option.

2. Test Case: Invalid Login Credentials
   Inputs:

- CUIT: "09876543210"
- PASSWORD: "password321"
- COMPANY: "MyCompany"

Expected Output:

- The script should fail to login to the AFIP website and raise an error.

3. Test Case: Empty CUIT for a client
   Inputs:

- CUIT: ""
- CONDITION: "1"

Expected Output:

- The script should successfully generate an invoice for the given client, even though the CUIT is empty.

4. Test Case: Invalid Client Condition
   Inputs:

- CUIT: "11111111111"
- CONDITION: "10"

Expected Output:

- The script should fail to generate an invoice for the given client and raise an error, as the provided condition value is not valid.

5. Test Case: Generating an Invoice for a Client
   Inputs:

- CUIT: "22222222222"
- CONDITION: "1"

Expected Output:

- The script should successfully generate an invoice for the given client, with the correct sell point, concept, date range, condition IVA, and payment method.
