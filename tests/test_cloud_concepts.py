import unittest
from src.chapter1_cloud_concepts import cloud_computing_overview, cloud_service_models, cloud_deployment_models, cloud_architecture

class TestCloudConcepts(unittest.TestCase):
    def test_cloud_computing_overview(self):
        expected = {
            "definition": "Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.",
            "benefits": ["Scalability", "Cost-effectiveness", "Flexibility", "Accessibility"]
        }
        self.assertEqual(cloud_computing_overview(), expected)

    def test_cloud_service_models(self):
        expected = [
            {
                "model": "IaaS (Infrastructure as a Service)",
                "description": "Provides virtualized computing resources over the internet. Examples include AWS EC2, Google Compute Engine, and Microsoft Azure Virtual Machines.",
                "examples": ["AWS EC2", "Google Compute Engine", "Microsoft Azure Virtual Machines"]
            },
            {
                "model": "PaaS (Platform as a Service)",
                "description": "Provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the underlying infrastructure. Examples include AWS Elastic Beanstalk, Google App Engine, and Microsoft Azure App Service.",
                "examples": ["AWS Elastic Beanstalk", "Google App Engine", "Microsoft Azure App Service"]
            },
            {
                "model": "SaaS (Software as a Service)",
                "description": "Provides a complete software application to customers over the internet. Examples include Salesforce, Google Workspace, and Microsoft Office 365.",
                "examples": ["Salesforce", "Google Workspace", "Microsoft Office  365"]
            }
        ]
        self.assertEqual(cloud_service_models(), expected)

    def test_cloud_deployment_models(self):
        expected = [
            {
                "model": "Public Cloud",
                "description": "Cloud resources are owned and operated by third-party cloud service providers and delivered over the internet. Examples include AWS, Google Cloud, and Microsoft Azure.",
                "examples": ["AWS", "Google Cloud", "Microsoft Azure"]
            },
            {
                "model": "Private Cloud",
                "description": "Cloud resources are owned and operated by a single organization, and the cloud infrastructure is provisioned for exclusive use by that organization. Examples include VMware vCloud and OpenStack.",
                "examples": ["VMware vCloud", "OpenStack"]
            },
            {
                "model": "Hybrid Cloud",
                "description": "A combination of public and private clouds that are connected, allowing data and applications to be shared between them. This provides greater flexibility and more deployment options.",
                "examples": []
            }
        ]
        self.assertEqual(cloud_deployment_models(), expected)

    def test_cloud_architecture(self):
        expected = [
            {
                "component": "Load Balancing",
                "description": "Distributes incoming network traffic across multiple servers to ensure no single server bears too much load."
            },
            {
                "component": "Auto-scaling",
                "description": "Dynamically adjusts the number of active servers based on the current load."
            },
            {
                "component": "Disaster Recovery",
                "description": "Ensures that data and services can be quickly restored after a disaster or outage."
            }
        ]
        self.assertEqual(cloud_architecture(), expected)

if __name__ == '__main__':
    unittest.main()

# Ensure that the functions return structured data instead of printing it
def cloud_computing_overview():
    return {
        "definition": "Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction.",
        "benefits": ["Scalability", "Cost-effectiveness", "Flexibility", "Accessibility"]
    }

def cloud_service_models():
    return [
        {
            "model": "IaaS (Infrastructure as a Service)",
            "description": "Provides virtualized computing resources over the internet. Examples include AWS EC2, Google Compute Engine, and Microsoft Azure Virtual Machines.",
            "examples": ["AWS EC2", "Google Compute Engine", "Microsoft Azure Virtual Machines"]
        },
        {
            "model": "PaaS (Platform as a Service)",
            "description": "Provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the underlying infrastructure. Examples include AWS Elastic Beanstalk, Google App Engine, and Microsoft Azure App Service.",
            "examples": ["AWS Elastic Beanstalk", "Google App Engine", "Microsoft Azure App Service"]
        },
        {
            "model": "SaaS (Software as a Service)",
            "description": "Provides a complete software application to customers over the internet. Examples include Salesforce, Google Workspace, and Microsoft Office 365.",
            "examples": ["Salesforce", "Google Workspace", "Microsoft Office 365"]
        }
    ]

def cloud_deployment_models():
    return [
        {
            "model": "Public Cloud",
            "description": "Cloud resources are owned and operated by third-party cloud service providers and delivered over the internet. Examples include AWS, Google Cloud, and Microsoft Azure.",
            "examples": ["AWS", "Google Cloud", "Microsoft Azure"]
        },
        {
            "model": "Private Cloud",
            "description": "Cloud resources are owned and operated by a single organization, and the cloud infrastructure is provisioned for exclusive use by that organization. Examples include VMware vCloud and OpenStack.",
            "examples": ["VMware vCloud", "OpenStack"]
        },
        {
            "model": "Hybrid Cloud",
            "description": "A combination of public and private clouds that are connected, allowing data and applications to be shared between them. This provides greater flexibility and more deployment options.",
            "examples": []
        }
    ]

def cloud_architecture():
    return [
        {
            "component": "Load Balancing",
            "description": "Distributes incoming network traffic across multiple servers to ensure no single server bears too much load."
        },
        {
            "component": "Auto-scaling",
            "description": "Dynamically adjusts the number of active servers based on the current load."
        },
        {
            "component": "Disaster Recovery",
            "description": "Ensures that data and services can be quickly restored after a disaster or outage."
        }
    ]