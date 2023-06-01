class PrimeGenerator:
    def __init__(self):
        self.next_prime = 2
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    def generate(self):
        while True:
            if self.is_prime(self.next_prime):
                prime = self.next_prime
                self.next_prime += 1
                return prime
            self.next_prime += 1

prime_generator = PrimeGenerator()
print(prime_generator.generate())
print(prime_generator.generate())
print(prime_generator.generate())
