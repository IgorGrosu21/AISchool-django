# Documentation

## Auth
### RefreshView
- Token: no
- Body: refresh token
- Return: access token

### SignUpView
- Token: no
- Body: email, password
- Return: access token

### LogInView
- Token: no
- Body: email, password
- Return: access token

### RestoreView
- Token: no
- Body: email, code, password, step (int)
- Return: access token

### LogOutView
- Token: Bearer
- Body: no
- Return: 'succes' or 'unauthorized'

### LogOutAllView
- Token: Bearer
- Body: no
- Return: 'succes' or 'unauthorized'

### UserView
- Token: Bearer
- Body: no
- Return: user email
