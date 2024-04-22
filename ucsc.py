import requests

URL = "https://engineering.ucsc.edu/departments/computer-science-and-engineering/people/" # webpage to scrape
page = requests.get(URL)

text = page.text.lower()

print(text)

index = 0
emails = []

domain_name = "@ucsc.edu" # domain name
unique_string = "@ucsc.edu<"  # unique string that tells the algorithm there is an email
ending_character = ">"  # ending string that tells the algorithm to stop

while index < len(text):

    next_email = text.find(unique_string, index)
    if next_email == -1:
        break
    email = ""
    counter = next_email - 1
    while counter >= 0:
        if text[counter] in ending_character:
            break
        email = text[counter] + email
        counter -= 1

    email += domain_name

    emails.append(email)
    index = next_email + 1

for i in range(len(emails)):
    print(emails[i])

# simply copy and paste the emails into the recipients section of your email
