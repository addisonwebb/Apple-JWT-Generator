import jwt
import time

# Team ID
team_id = 'DK07BE4QJA'

# Key ID
key_id = 'ASL1737N84'

# Private Key
private_key = b'-----BEGIN PRIVATE KEY-----\nMIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgaHJzKVQTtzGdPpw/\nYQ2LE3QxLYimXsYJaiCieBhhqwygCgYIKoZIzj0DAQehRANCAASiGbpU+CNTH/UF\niqnW9IMBBhhYJL61McJVjYWIX1JTa5NYL0MdMAy/WgF6Vw3QWx6x/4cJB3mfsXKs\n40t0mfGT\n-----END PRIVATE KEY-----'

issued_timestamp = time.time()
expiration_timestamp = issued_timestamp + 1800

encoded = jwt.encode({'iss': team_id,'iat': issued_timestamp,'exp': expiration_timestamp}, private_key, algorithm='ES256', headers={'kid': key_id})

print(encoded)
