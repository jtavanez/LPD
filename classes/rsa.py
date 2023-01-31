#import math
import random

class rsa:
    
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def coprime(self, a, b):
        return self.gcd(a, b) == 1

    def modinv(self, a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

    def encrypt(self, message, e, n):
        return pow(message, e, n)

    def decrypt(self, encrypted, d, n):
        return pow(encrypted, d, n)

    def generate_keys(self):
        p = random.randint(10, 20)
        q = random.randint(10, 20)
        while not self.coprime(p, q):
            q = random.randint(10, 20)
        n = p * q
        phi = (p-1) * (q-1)
        e = random.randint(1, phi)
        while not self.coprime(e, phi):
            e = random.randint(1, phi)
        d = self.modinv(e, phi)
        public_key = (e, n)
        private_key = (d, n)
        return (public_key, private_key)

    