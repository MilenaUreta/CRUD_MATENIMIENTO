from modelo.conexion import conexion
class ctr_grupo(conexion):
    def __init__(self):
      super().__init__()

    def consultargrupo(self,buscar):
        
        try:
            sql="select * from grupo where descripcion like'"+str(buscar)+"%' order by idgrupo"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
            if result.__len__()==0:
                print('\tSIN RESULTADOS PARA ESTA BUSQUEDA')
            else:
                print('\tID\tDESCRIPCION')
                for valor in result:
                     print('\t',valor[0],'\t',valor[1])
        except Exception as e:
            print('error en la consulta',e)
            self.conn.rollback()
        finally:
            self.cerrar()
        

#--------------------------------------------------------------------
    def insertagrupo(self,grp):
        correcto=False
        try:
            sql="INSERT INTO grupo (descripcion) VALUES (%s)"
            self.conectar()
            self.conector.execute(sql,grp.descripcion)
            self.conn.commit()
            correcto=True
        except Exception as e:
            print('error al insertar ',e)
            self.conn.rollback()
            correcto=False
        finally:
            self.cerrar()
        return correcto
#--------------------------------------------------------------------
    def modificagrupo(self,grp):
        correcto=False
        try:
            sql="update grupo set descripcion=%s where idgrupo=%s"
            self.conectar()
            self.conector.execute(sql,(grp.descripcion,grp.id))
            self.conn.commit()
            correcto=True
        except Exception as e:
            print('error al modificar ',e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
#---------------------------------------------------------------------
    def eliminagrupo(self,grp):
        correcto=False
        try:
            sql="delete from grupo where idgrupo=%s"
            self.conectar()
            self.conector.execute(sql,(grp.id,))
            self.conn.commit()
            correcto=True
        except Exception as e:
            print('error al eliminar ',e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
# ---------------------------------------------------------------------------------
    def buscarid(self,dato):
        existe=False
        try:
            sql="select * from grupo where idgrupo={}".format(dato)
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
            if result.__len__()==0:
                print('\tSIN RESULTADOS PARA ESTA BUSQUEDA')
            else:
                    print('\tID\tDESCRIPCION')
                    for valor in result:
                        print('\t',valor[0],'\t',valor[1])
        except Exception as e:
            print('error ',e)
        finally:
            self.cerrar()
        return existe
