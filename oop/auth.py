import uuid 

class AuthSystem:
    def login(self,user):
        user.login = True
        user.key = uuid.uuid4()
        return user.key