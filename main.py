import ca_certificate
import client_certificate
def get_ca_attributes():
    """
    Function to ask user for CA attributes and return them.
    Returns:
        dict: A dictionary containing the CA attributes.
    """
    ca_attributes = {}
    ca_attributes['common_name'] = input("Enter CA Common Name: ")
    ca_attributes['organization'] = input("Enter CA Organization: ")
    ca_attributes['country'] = input("Enter CA Country: ")
    return ca_attributes
def get_client_attributes():
    """
    Function to ask user for client attributes and return them.
    Returns:
        dict: A dictionary containing the client attributes.
    """
    client_attributes = {}
    client_attributes['common_name'] = input("Enter Client Common Name: ")
    client_attributes['organization'] = input("Enter Client Organization: ")
    client_attributes['country'] = input("Enter Client Country: ")
    return client_attributes
def create_certificates():
    ca_attributes = get_ca_attributes()
    client_attributes = get_client_attributes()
    ca_certificate_file = ca_certificate.create_ca_certificate(ca_attributes)
    client_certificate.create_client_certificate(client_attributes, ca_certificate_file)
if __name__ == "__main__":
    create_certificates()