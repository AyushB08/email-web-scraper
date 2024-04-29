import requests
from bs4 import BeautifulSoup
import re


def extract_emails(url):
    response = requests.get(url)

    raw_text = BeautifulSoup(response.content, 'html.parser')

    text_content = raw_text.get_text()

    # pattern to match email address r is used to avoid escape characters \b in beginning and end is used to ensure
    # that there is space between a word character (part of the email) and a non-word character (whitespace,
    # punctuation, etc) [A-Za-z0-9._%+-] defines the allowed characters for this section + gathers all the allowed
    # letters from the definition above @ matches @ symbol in email \. matches . in email [A-Z|a-z] matches domain in
    # email {2,} Ensures that domain is at least 2 characters long

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails_found = re.findall(email_pattern, text_content)

    return emails_found


link = "https://cs.ics.uci.edu/faculty/"
emails = extract_emails(link)

for email in emails:
    print(email)
