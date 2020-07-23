from modelo.conexion import conexion
from modelo.clases import plan_cuenta
plan=plan_cuenta()
class validar(conexion):
    
    def validaingreso(self,valor):
        if valor.isspace() or valor.__len__()==0:
            return True
        else:
           return False
#-------------------------------------------------------------------
    def existe(self,campo,tabla,dato):
        existe=False
        try:
            sql="select {} from {}".format(campo,tabla)
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
            for valor in result:
               if valor[0]==dato:
                   existe=True
                   break
        except Exception as e:
            print('error ',e)
        finally:
            self.cerrar()
        return existe
#---------------------------------------------------------------------
   