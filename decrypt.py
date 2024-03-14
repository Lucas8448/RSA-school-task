from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

#hente privat nøkkel
privFile = input("Filnavn til din private nøkkel: ")
with open(privFile, "rb") as File:
  private_key = RSA.import_key(File.read())

#Initialiserer RSA cipher for dekryptering
cipherRsa = PKCS1_OAEP.new(private_key)

#Leser inn kryptert melding, og dekrypterer
kryptert_melding_b64 = input("Skriv inn den krypterte meldingen: ")
kryptert_melding = base64.b64decode(kryptert_melding_b64)
melding = cipherRsa.decrypt(kryptert_melding)

print("Dekryptert melding: ", melding.decode())