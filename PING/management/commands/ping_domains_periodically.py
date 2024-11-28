import logging
from smtplib import SMTPException

import requests
from django.apps import apps
from django.conf import settings
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.conf import settings

Domain = apps.get_model(settings.DOMAIN_MODEL)


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("domain_check.log"),
        logging.StreamHandler()
    ]
)


def check_domains():
    domains = Domain.objects.values('domain_url')
    unreachable_domains = []

    for domain in domains:
        try:
            response = requests.get(domain['domain_url'], timeout=30)
            if response.status_code == 200:
                logging.info(f"{domain['domain_url']} is reachable with status code {response.status_code}")
            else:
                logging.warning(f"{domain['domain_url']} returned status code {response.status_code}")

        except requests.exceptions.RequestException as e:
            unreachable_domains.append((domain['domain_url'], str(e)))
            logging.error(f"{domain['domain_url']} is not reachable. Error: {e}")

    if unreachable_domains:
        message = "\n".join([f"{url}: {error}" for url, error in unreachable_domains])

        try:
            print("Attempting to send email...")
            send_mail(
                subject=f"Unreachable Domains Report",
                message=f"The following domains are not reachable:\n\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=["hadeezah18@gmail.com", "ifeanyi@maekandex.com.ng", "justin@maekandex.com.ng"],
            )
            print("Email sent successfully.")
        except SMTPException as e:
            print(f"failed to send email: {e}")
            logging.error(f"Failed to send email. Error: {e}")


class Command(BaseCommand):
    help = 'Checks if domains are reachable at given intervals'

    def handle(self, *args, **options):
        check_domains()




