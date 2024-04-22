import requests

URL = "https://www2.eecs.berkeley.edu/Faculty/Lists/CS/faculty.html" # webpage to scrape
page = requests.get(URL)

text = page.text.lower()

print(text)

index = 0
emails = []

domain_name = "@berkeley.edu" # domain name
unique_string = "@berkeley.edu"  # unique string that tells the algorithm there is an email
ending_string = ">"  # ending string that tells the algorithm to stop
ending_string_array = [">", " "] # possible ending string array if there is more than one possible ending string
# only use either ending_string or ending_string_array

while index < len(text):

    next_email = text.find(unique_string, index)
    if next_email == -1:
        break
    email = ""
    counter = next_email - 1
    while counter >= 0:

        if text[counter] in ending_string_array:
            break
        email = text[counter] + email
        counter -= 1

    email += domain_name

    emails.append(email)
    index = next_email + 1

for i in range(len(emails)):
    print(emails[i])

# simply copy and paste the emails into the recipients section of your email
