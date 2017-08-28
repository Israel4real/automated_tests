import random
import string

domains = [ "gmail.com", "live.com", "yahoo.com"]
chars = string.hexdigits


def create_prefix(length=5):
    "Creates random email prefix"
    return ''.join(random.choice(chars) for i in range(length))


def generate_email():
    "Returns randomly generated email"
    return 'eme.test+'+ create_prefix() + '@' + random.choice(domains)
