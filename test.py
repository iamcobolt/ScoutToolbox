import validators


def is_valid_domain(domain):
    if validators.domain(domain):
        return True
    return False


domain = "www.example"
if is_valid_domain(domain):
    print("Valid domain")
else:
    print("Invalid domain")
    