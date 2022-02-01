# arrows-encrypt
Simple little cipher algorithm based on the Vigenère shift cipher and base-4.

This is a simple multi-step encryption Algorithm based on the Vigenère Cipher. The possible encryptable values range from ASCII/Unicode 32 to 126 (inclusive).
For encryption, each character is shifted by the corresponding ASCII value in the key, the shifted ASCII value is then converted from decimal (base-10) to base-4, and finally the new base-4 number is mapped to one of four directional arrow symbols. The decryption process is the inverse.

Plaintext: "This is a secret."

Generated OTP key: 99j<(S;`2k(2bl8o>

Ciphertext: ▾◂▸▾▴◂▴◂▾▾▾▴▴▸▴▴▴◂◂▴▴▸▸▾▴◂▸▸▾◂▴▴▾▸▴▸▾◂◂▸▾▸◂▸▾▸▾▸▾▴▾◂▾▾▸▸▾▸▸▾▾◂▾▴▾▴▸▴
