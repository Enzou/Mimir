from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view(name='static', path='static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('wiki', '/wiki')
    config.add_route('cipher', '/cipher')
    config.add_route('hash', '/hash')
    config.add_route('encoding', '/encoding')
    config.add_route('obfuscation', '/obfuscation')
    config.add_route('algo', '/algorithms')
    config.add_route('tools', '/tools')
    config.add_route('tools/rest', '/tools/rest')
    config.scan()
    return config.make_wsgi_app()

# TODO Ciphers:
# Skytale
# ATBASH
# CAESAR / Rot13
# Affine Cipher
# Rail Fence Cipher
# Keyword Cipher
# Beaufort Cipher
# Templar
# Porta
# Vigenere
# Gronsfeld
# Autokey
# Bacon
# Chaocipher
# ADFGVX
# Playfair
# Two-Square
# Tri-Sqaure
# One-Time-Pad
# BIFID
# TRIFID
# Hill Cipher
# Visual Crypto ?
# Engima
# RSA
# Blowfish
# Twofish
# Threefish
# Rijndael (AES)
# SCRYPT
# Elliptic Curve
# ChaCha
# Cast5
# Cast6
# ShaCal2
# Shamir's Secret Sharing (SSS)
# RC2
# RC4
# RC5
# RC6
# DES
# 3DES

# TODO Hashes:
# MD5
# SHA0 SHA1, SHA2-224, SHA2-256, SHA2-384, SHA2-512, SHA3-224, SHA3-256, SHA3-384, SHA3-512,
# SHAKE-128, SHAKE-256,
# WHirlpool
# HMAC-SHA1/256/512
# BCRYPT
# PBKDF2
# SipHash
# Skein
# Keccak
# Argon2