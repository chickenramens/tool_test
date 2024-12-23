import unittest
import os
from cryptography import x509
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta
from new_client_certificate import create_client_certificate

class TestClientCertificateCreation(unittest.TestCase):
    def setUp(self):
        self.attributes = {
            'C': 'US',
            'ST': 'California',
            'L': 'San Francisco',
            'O': 'My Company',
            'OU': 'My Division',
            'CN': 'mycompany.com'
        }
        self.output_path = '/tmp/test_cert_output'
        self.validity_days = 365

    def test_certificate_creation(self):
        cert_path = create_client_certificate(self.attributes, self.output_path, self.validity_days)
        key_path = os.path.join(self.output_path, 'client_key.pem')

        # Check if the certificate and key files are created
        self.assertTrue(os.path.exists(cert_path), "Certificate file was not created.")
        self.assertTrue(os.path.exists(key_path), "Key file was not created.")

        # Verify the validity period of the certificate
        with open(cert_path, "rb") as cert_file:
            cert_data = cert_file.read()
            cert = x509.load_pem_x509_certificate(cert_data)
            not_before = cert.not_valid_before
            not_after = cert.not_valid_after
            expected_not_after = not_before + timedelta(days=self.validity_days)

            self.assertEqual(not_after, expected_not_after, "Certificate validity period is incorrect.")

        # Clean up
        os.remove(cert_path)
        os.remove(key_path)
        os.rmdir(self.output_path)

if __name__ == '__main__':
    unittest.main()
