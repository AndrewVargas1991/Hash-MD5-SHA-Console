import hashlib
import os

bufferSize = 65536

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 =hashlib.sha384()
sha512 = hashlib.sha512()

caminho = input('Selecione um arquivo: ').replace('"', '')
if os.path.isfile(caminho):
    with open(caminho, 'rb') as arquivo:
        while True:
            data = arquivo.read(bufferSize)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha224.update(data)
            sha256.update(data)
            sha384.update(data)
            sha512.update(data)

print("\nHashes do arquivo:")
print("   MD5: {0}".format(md5.hexdigest()))
print("  SHA1: {0}".format(sha1.hexdigest()))
print("SHA224: {0}".format(sha224.hexdigest()))
print("SHA256: {0}".format(sha256.hexdigest()))
print("SHA384: {0}".format(sha384.hexdigest()))
print("SHA512: {0}".format(sha512.hexdigest()))

input('\nAperte ENTER para sair...')