from cryptography.fernet import Fernet

SYMMETRIC_KEY = b'sPNtfIsUt6UkUbJgA1NdSWCqjUmOFZRH7MR9xQ_g38k='  

def descifrar_dato(dato_reporte):
    llave_parseada = Fernet(SYMMETRIC_KEY)
    dato_descifrado_reporte = llave_parseada.decrypt(dato_reporte.encode())  
    return dato_descifrado_reporte.decode()  

def cifrar_dato(dato):
    fernet = Fernet(SYMMETRIC_KEY)
    dato_cifrado = fernet.encrypt(dato.encode())
    return dato_cifrado.decode() 

    
