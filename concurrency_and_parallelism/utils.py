import time 
import logging
import requests

#logging.basicConfig(level=logging.DEBUG)

class WebsiteDownException(Exception):
    pass 


def ping_website(address, timeout=20):
    """
    Check if a website is down. A website is considered down
    if either the status_cod >= 400 or if the timeout expires

    Throw a WebsiteDownException if any of the website down conditions are met
    """
    try: 
        response = requests.head(address, timeout=timeout)
        if response.status_code >= 400:
            logging.warning(f"Website {address} returned status_code{response.status_code}")
            raise WebsiteDownException()
    except requests.exceptions.RequestException:
        logging.warning(f"Timeout expired for website {address}")
        raise WebsiteDownException()


def notify_owner(address):
    """
    Send the owner of the address a notification that their website is down

    For now, we're just going to sleep for 0.5 seconds but this is where you
    would send an email, push notification or text-message
    """
    logging.info(f"Notifying the owner of {address} website")
    time.sleep(0.5)


def check_website(address):
    """
    Utility function: check if a website is down, if so, notify the user
    """
    try:
        ping_website(address)
    except WebsiteDownException:
        notify_owner(address)