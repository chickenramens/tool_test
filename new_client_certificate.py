from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta
import os

def create_client_certificate(attributes, output_path, validity_days=365):
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Build subject and issuer
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, attributes.get('C', 'US')),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, attributes.get('ST', 'California')),
        x509.NameAttribute(NameOID.LOCALITY_NAME, attributes.get('L', 'San Francisco')),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, attributes.get('O', 'My Company')),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, attributes.get('OU', 'My Division')),
        x509.NameAttribute(NameOID.COMMON_NAME, attributes.get('CN', 'mycompany.com')),
    ])

    # Create certificate
    certificate = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.utcnow()
    ).not_valid_after(
        datetime.utcnow() + timedelta(days=validity_days)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName(attributes.get('CN', 'mycompany.com'))]),
        critical=False,
    ).sign(private_key, hashes.SHA256())

    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)

    # Write private key to file
    with open(f"{output_path}/client_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Write certificate to file
    with open(f"{output_path}/client_cert.pem", "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

    return f"{output_path}/client_cert.pem"

# Example usage
attributes = {
    'C': 'US',
    'ST': 'California',
    'L': 'San Francisco',
    'O': 'My Company',
    'OU': 'My Division',
    'CN': 'mycompany.com'
}
output_path = '/path/to/output'
validity_days = 365

create_client_certificate(attributes, output_path, validity_days)

