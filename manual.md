# CLI Tool for Creating CA and Client Certificates

## Introduction

The CLI tool provided allows users to create a CA (Certificate Authority) certificate and a corresponding client certificate. The tool prompts the user to enter the required attributes for both the CA and client certificates and generates the certificates accordingly.

## Installation

To use the CLI tool, follow the steps below:

1. Make sure you have Python installed on your system. If not, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the repository or download the code files from the provided source.

3. Open a terminal or command prompt and navigate to the directory where the code files are located.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the `cryptography` library, which is required for certificate generation.

## Usage

Once you have installed the dependencies, you can use the CLI tool by following these steps:

1. Open a terminal or command prompt and navigate to the directory where the code files are located.

2. Run the following command to execute the CLI tool:

   ```
   python main.py
   ```

3. The tool will prompt you to enter the attributes for the CA certificate. Enter the requested information, such as the common name, organization, and country.

4. After entering the CA attributes, the tool will prompt you to enter the attributes for the client certificate. Again, enter the requested information.

5. Once you have provided all the required attributes, the tool will generate the CA certificate and the client certificate.

6. The tool will display the paths to the generated certificate files. You can find the CA certificate at the specified path and the client certificate at another specified path.

## Example

Here is an example of how to use the CLI tool:

```
$ python main.py
Enter CA Common Name: My CA
Enter CA Organization: My Organization
Enter CA Country: US
Enter Client Common Name: John Doe
Enter Client Organization: Acme Inc.
Enter Client Country: CA
```

After entering the above information, the tool will generate the certificates and display the paths to the generated files:

```
CA certificate created: /path/to/ca_certificate.crt
Client certificate created: /path/to/client_certificate.crt
```

You can then use the generated certificates for your desired purposes.

## Conclusion

The CLI tool provided allows users to easily create CA and client certificates by entering the required attributes. It simplifies the process of certificate generation and provides the necessary files for further use.