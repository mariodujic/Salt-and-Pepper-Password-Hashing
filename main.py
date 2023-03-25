import hashlib
import numpy

# User's password
password = b'us3rPassw0rd'

# Random salt
salt_one = b'dfep3'
salt_two = b'cvuxiopc'
char_sum = numpy.frombuffer(password, "uint8").sum()
salt = ''
if char_sum % 2 == 0:
    salt = salt_one
else:
    salt = salt_two

# Application pepper, preferably stored in a secure configuration file, outside the source code
pepper = b'2k3k4o0'

# Hashed password
hashed = hashlib.sha3_256(salt + pepper + password).hexdigest()

if __name__ == '__main__':
    # User's hashed password
    print(hashed)
