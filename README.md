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
``` 
POST http:localhost:8000/logar/

{
    "username":"INSIRA UM USERNAME PRA LOGAR",
    "password":"INSIRA UMA SENHA PARA LOGAR"
}
```
ENVIE NO HEADER
``` 
GET http:localhost:8000/testar/
HEADER
"Authorization":"Token INSIRA SEU TOKEN"

```
Caso o token inserido seja válido o email cadastrado será informado
