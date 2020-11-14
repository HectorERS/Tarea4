from tinyec import registry
import secrets
import elgamal

dicc = elgamal.generate_keys()
publicKey = dicc['publicKey']
cipher = elgamal.encrypt(publicKey, "This is the message I want to encrypt")
privateKey = dicc['privateKey']

plaintext = elgamal.decrypt(privateKey, cipher)

print(type(publicKey))
print(cipher)
print(plaintext)
print(publicKey)
