import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import secrets

def encrypt_js_file(file_path, out_path, key):
    with open(file_path, 'r') as file:
        js_code = file.read().encode('utf-8')
    
    iv = get_random_bytes(16)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(js_code, 16))
    
    encrypted_code = base64.b64encode(iv + encrypted_data).decode('utf-8')
    
    with open(out_path, 'w') as output_file:
        output_file.write('(function(){var encryptedCode = "' + encrypted_code + '";var iv = encryptedCode.slice(0, 24);var encryptedData = encryptedCode.slice(24);var decryptedData = CryptoJS.AES.decrypt(encryptedData, CryptoJS.enc.Utf8.parse("' + key + '"), {iv: CryptoJS.enc.Utf8.parse(iv), padding: CryptoJS.pad.Pkcs7, mode: CryptoJS.mode.CBC });var decryptedCode = decryptedData.toString(CryptoJS.enc.Utf8); eval(decryptedCode);})();')


key = secrets.token_hex(16) 
encrypt_js_file('mmm.js', 'mkkk.js', key)