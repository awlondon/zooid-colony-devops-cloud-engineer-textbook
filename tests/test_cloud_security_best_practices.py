import unittest
from src.chapter4_cloud_security_best_practices import iam_overview, encryption_overview, network_security_overview, compliance_standards_overview, least_privilege_overview

class TestCloudSecurityBestPractices(unittest.TestCase):
    def test_iam_overview(self):
        expected = {
            "definition": "Identity and Access Management (IAM) controls who can access cloud resources and what actions they can perform.",
            "examples": ["AWS IAM", "Azure AD"],
            "benefits": ["Fine-grained access control", "Reduced risk of unauthorized access"],
            "edge_cases": ["IAM policies should not grant unnecessary permissions", "IAM roles should be reviewed regularly"]
        }
        result = iam_overview()
        self.assertEqual(result, expected)
        self.assertIn("AWS IAM", result["examples"])
        self.assertIn("Azure AD", result["examples"])
        self.assertIn("Fine-grained access control", result["benefits"])
        self.assertIn("Reduced risk of unauthorized access", result["benefits"])
        self.assertIn("IAM policies should not grant unnecessary permissions", result["edge_cases"])
        self.assertIn("IAM roles should be reviewed regularly", result["edge_cases"])

    def test_encryption_overview(self):
        expected = {
            "definition": "Encryption protects data at rest and in transit.",
            "examples": ["AES", "RSA"],
            "benefits": ["Data confidentiality", "Protection against data breaches"],
            "edge_cases": ["Encryption keys should be rotated regularly", "Encryption should be used for sensitive data only"]
        }
        result = encryption_overview()
        self.assertEqual(result, expected)
        self.assertIn("AES", result["examples"])
        self.assertIn("RSA", result["examples"])
        self.assertIn("Data confidentiality", result["benefits"])
        self.assertIn("Protection against data breaches", result["benefits"])
        self.assertIn("Encryption keys should be rotated regularly", result["edge_cases"])
        self.assertIn("Encryption should be used for sensitive data only", result["edge_cases"])

    def test_network_security_overview(self):
        expected = {
            "definition": "Network security ensures secure communication and access control.",
            "examples": ["Firewalls", "Network segmentation"],
            "benefits": ["Prevention of unauthorized access", "Detection of malicious activities"],
            "edge_cases": ["Network segmentation should be implemented to isolate critical systems", "Firewalls should be configured to block unauthorized traffic"]
        }
        result = network_security_overview()
        self.assertEqual(result, expected)
        self.assertIn("Firewalls", result["examples"])
        self.assertIn("Network segmentation", result["examples"])
        self.assertIn("Prevention of unauthorized access", result["benefits"])
        self.assertIn("Detection of malicious activities", result["benefits"])
        self.assertIn("Network segmentation should be implemented to isolate critical systems", result["edge_cases"])
        self.assertIn("Firewalls should be configured to block unauthorized traffic", result["edge_cases"])

    def test_compliance_standards_overview(self):
        expected = {
            "definition": "Compliance standards ensure adherence to industry regulations and best practices.",
            "examples": ["SOC 2", "HIPAA", "PCI DSS"],
            "benefits": ["Legal compliance", "Enhanced customer trust"],
            "edge_cases": ["Compliance audits should be conducted regularly", "Compliance policies should be documented and reviewed"]
        }
        result = compliance_standards_overview()
        self.assertEqual(result, expected)
        self.assertIn("SOC 2", result["examples"])
        self.assertIn("HIPAA", result["examples"])
        self.assertIn("PCI DSS", result["examples"])
        self.assertIn("Legal compliance", result["benefits"])
        self.assertIn("Enhanced customer trust", result["benefits"])
        self.assertIn("Compliance audits should be conducted regularly", result["edge_cases"])
        self.assertIn("Compliance policies should be documented and reviewed", result["edge_cases"])

    def test_least_privilege(self):
        expected = {
            "definition": "Grant users only the permissions necessary to perform their job functions.",
            "examples": ["Role-based access control", "Least privilege policies"],
            "benefits": ["Reduced attack surface", "Improved security posture"],
            "edge_cases": ["Least privilege policies should be reviewed regularly", "Least privilege should be enforced for all users"]
        }
        result = least_privilege_overview()
        self.assertEqual(result, expected)
        self.assertIn("Role-based access control", result["examples"])
        self.assertIn("Least privilege policies", result["examples"])
        self.assertIn("Reduced attack surface", result["benefits"])
        self.assertIn("Improved security posture", result["benefits"])
        self.assertIn("Least privilege policies should be reviewed regularly", result["edge_cases"])
        self.assertIn("Least privilege should be enforced for all users", result["edge_cases"])

    def test_least_privilege_edge_cases(self):
        result = least_privilege_overview()
        self.assertIn("Role-based access control", result["examples"])
        self.assertIn("Least privilege policies", result["examples"])
        self.assertIn("Reduced attack surface", result["benefits"])
        self.assertIn("Improved security posture", result["benefits"])
        self.assertNotIn("Non-existent example", result["examples"])
        self.assertNotIn("Non-existent benefit", result["benefits"])

    def test_network_security_edge_cases(self):
        result = network_security_overview()
        self.assertIn("Firewalls", result["examples"])
        self.assertIn("Network segmentation", result["examples"])
        self.assertIn("Prevention of unauthorized access", result["benefits"])
        self.assertIn("Detection of malicious activities", result["benefits"])
        self.assertIn("Network segmentation should be implemented to isolate critical systems", result["edge_cases"])
        self.assertIn("Firewalls should be configured to block unauthorized traffic", result["edge_cases"])
        self.assertNotIn("Non-existent example", result["examples"])
        self.assertNotIn("Non-existent benefit", result["benefits"])

    def test_compliance_standards_edge_cases(self):
        result = compliance_standards_overview()
        self.assertIn("SOC 2", result["examples"])
        self.assertIn("HIPAA", result["examples"])
        self.assertIn("PCI DSS", result["examples"])
        self.assertIn("Legal compliance", result["benefits"])
        self.assertIn("Enhanced customer trust", result["benefits"])
        self.assertIn("Compliance audits should be conducted regularly", result["edge_cases"])
        self.assertIn("Compliance policies should be documented and reviewed", result["edge_cases"])
        self.assertNotIn("Non-existent example", result["examples"])
        self.assertNotIn("Non-existent benefit", result["benefits"])

if __name__ == '__main__':
    unittest.main()