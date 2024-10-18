def get_name(email):
    """Extract the name from an email address."""
    name_part = email[: email.index("@")]
    name = " ".join(name_part.split(".")).title()
    return name


email_dict = {}
email = input("Email: ").strip()
while email != "":
    name = get_name(email)
    response = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if response.startswith("n"):
        name = input("Name: ").strip()
    email_dict[name] = email
    email = input("Email: ").strip()

print()
for name, email in email_dict.items():
    print(f"{name} ({email})")
