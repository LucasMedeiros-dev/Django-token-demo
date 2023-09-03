# DJANGO REST USO DE TOKEN DEMO
É uma demo simples para exibir o uso de um token jwt para autenticação  
# ENDPOINTS
http:localhost:8000/registrar/  
http:localhost:8000/logar/  
http:localhost:8000/testar/  
# REQUESTS
```
POST http:localhost:8000/registrar/
E envie no body um form com
{
    "username":"INSIRA UM USERNAME PRA REGISTRAR",
    "password":"INSIRA UMA SENHA PARA REGISTRAR",
    "email":"INSIRA UM EMAIL PARA REGISTRAR"
}
```
![image](https://github.com/LucasMedeiros-dev/Django-token-demo/assets/39228907/4fbf44e8-4e36-4528-ae03-b6945a0e0ad7)

``` 
POST http:localhost:8000/logar/

{
    "username":"INSIRA UM USERNAME PRA LOGAR",
    "password":"INSIRA UMA SENHA PARA LOGAR"
}
```
![image](https://github.com/LucasMedeiros-dev/Django-token-demo/assets/39228907/9c4c45db-b2c3-4935-9c5a-8e1068f41da4)

ENVIE NO HEADER
``` 
GET http:localhost:8000/testar/
HEADER
"Authorization":"Token INSIRA SEU TOKEN"

```
Caso o token inserido seja válido o email cadastrado será informado  
![image](https://github.com/LucasMedeiros-dev/Django-token-demo/assets/39228907/b4ee2374-3665-4be5-bcbc-c3bcd4fad76e)  
Caso seja inválido  
![image](https://github.com/LucasMedeiros-dev/Django-token-demo/assets/39228907/d04fdf1e-b038-40e6-8c01-1a48b5bd6f03)  


