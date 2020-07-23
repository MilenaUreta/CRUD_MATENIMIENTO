class grupo:
    def __init__(self,codigo=0,descripcion=''):
        self.__id=codigo
        self.__descripcion=descripcion
    @property
    def id(self):
        return self.__id
    @id.setter
    def asigid(self,valor):
        self.__id=valor
    
    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def asigdesc(self,valor):
        self.__descripcion=valor

class plan_cuenta (grupo):
    def __init__(self,idplancuenta=1,idgrupo=0,codigo='',descripcion='',naturaleza='',estado=False,):
        grupo.__init__(self,idgrupo)
        self.__idplancuenta=idplancuenta
        self.__codigo=codigo
        self.__descripcion=descripcion
        self.__naturaleza=naturaleza
        self.__estado=estado
        self.__grupo=idgrupo
    @property
    def idplancuenta(self):
        return self.__idplancuenta
    @idplancuenta.setter
    def asigidplan(self,valor):
        self.__idplancuenta=valor
    
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def asigcodigo(self,valor):
        self.__codigo=valor
    
    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def asigdesc(self,valor):
        self.__descripcion=valor
    
    @property
    def naturaleza(self):
        return self.__naturaleza
    @naturaleza.setter
    def asignat(self,valor):
        self.__naturaleza=valor

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def asigestado(self,valor):
        self.__estado=valor
    
    @property
    def idgrupo(self):
        return self.__grupo
    @idgrupo.setter
    def asiggrupo(self,valor):
        self.__grupo=valor
    


   

