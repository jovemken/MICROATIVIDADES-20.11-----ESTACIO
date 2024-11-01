def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario('Admin')  # Teste com 'Admin'
loginUsuario('admin')  # Teste com 'admin'
loginUsuario('User')   # Teste com 'User'
loginUsuario('usuário') # Teste com 'usuário'
