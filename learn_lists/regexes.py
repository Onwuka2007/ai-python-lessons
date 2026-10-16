import re

email = input("What is your email: ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)*\w+\.(com|edu)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# from URL
url = input("URL: ").strip()

if matches := re.search(r"^(http(s)?://)?(?:www\.)?x\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(3)}")
