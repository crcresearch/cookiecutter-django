import os
import random

with open('/app/secretkey.txt', 'w') as f:
    secretkey = ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]
    )

    f.write(secretkey)
