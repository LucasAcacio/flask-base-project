from service.auth_service import get_user_roles

def user_authentication(roles, authHeader):
    ''''
        Handle authentication here. 
        Role based authentication example...
    '''
    if not authHeader:
        return False

    userRoles = get_user_roles(authHeader)

    for role in roles:
        if role not in userRoles:
           return False
    return True
