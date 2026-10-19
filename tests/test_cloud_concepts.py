import unittest
from src.chapter1_cloud_concepts import cloud_computing_overview, cloud_service_models, cloud_deployment_models, cloud_architecture

class TestCloudConcepts(unittest.TestCase):
    def test_cloud_computing_overview(self):
        expected = "Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction."
        self.assertEqual(cloud_computing_overview(), expected)

    def test_cloud_service_models(self):
        expected = ["IaaS (Infrastructure as a Service): Provides virtualized computing resources over the internet. Examples include AWS EC2, Google Compute Engine, and Microsoft Azure Virtual Machines.", "PaaS (Platform as a Service): Provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the underlying infrastructure. Examples include AWS Elastic Beanstalk, Google App Engine, and Microsoft Azure App Service.", "SaaS (Software as a Service): Provides a complete software application to customers over the internet. Examples include Salesforce, Google Workspace, and Microsoft Office 365."]
        self.assertEqual(cloud_service_models(), expected)

    def test_cloud_deployment_models(self):
        expected = ["Public Cloud: Cloud resources are owned and operated by third-party cloud service providers and delivered over the internet. Examples include AWS, Google Cloud, and Microsoft Azure.", "Private Cloud: Cloud resources are owned and operated by a single organization, and the cloud infrastructure is provisioned for exclusive use by that organization. Examples include VMware vCloud and OpenStack.", "Hybrid Cloud: A combination of public and private clouds that are connected, allowing data and applications to be shared between them. This provides greater flexibility and more deployment options."]
        self.assertEqual(cloud_deployment_models(), expected)

    def test_cloud_architecture(self):
        expected = ["Load Balancing: Distributes incoming network traffic across multiple servers to ensure no single server bears too much load.", "Auto-scaling: Dynamically adjusts the number of active servers based on the current load.", "Disaster Recovery: Ensures that data and services can be quickly restored after a disaster or outage."]
        self.assertEqual(cloud_architecture(), expected)

if __name__ == '__main__':
    unittest.main()

# Ensure that the functions return structured data instead of printing it
def cloud_computing_overview():
    return "Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that can be rapidly provisioned and released with minimal management effort or service provider interaction."

def cloud_service_models():
    return ["IaaS (Infrastructure as a Service): Provides virtualized computing resources over the internet. Examples include AWS EC2, Google Compute Engine, and Microsoft Azure Virtual Machines.", "PaaS (Platform as a Service): Provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the underlying infrastructure. Examples include AWS Elastic Beanstalk, Google App Engine, and Microsoft Azure App Service.", "SaaS (Software as a Service): Provides a complete software application to customers over the internet. Examples include Salesforce, Google Workspace, and Microsoft Office 365."]

def cloud_deployment_models():
    return ["Public Cloud: Cloud resources are owned and operated by third-party cloud service providers and delivered over the internet. Examples include AWS, Google Cloud, and Microsoft Azure.", "Private Cloud: Cloud resources are owned and operated by a single organization, and the cloud infrastructure is provisioned for exclusive use by that organization. Examples include VMware vCloud and OpenStack.", "Hybrid Cloud: A combination of public and private clouds that are connected, allowing data and applications to be shared between them. This provides greater flexibility and more deployment options."]

def cloud_architecture():
    return ["Load Balancing: Distributes incoming network traffic across multiple servers to ensure no single server bears too much load.", "Auto-scaling: Dynamically adjusts the number of active servers based on the current load.", "Disaster Recovery: Ensures that data and services can be quickly restored after a disaster or outage."]