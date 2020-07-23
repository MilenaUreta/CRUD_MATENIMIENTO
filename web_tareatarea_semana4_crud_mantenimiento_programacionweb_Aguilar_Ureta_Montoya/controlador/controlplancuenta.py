from modelo.conexion import conexion
class ctr_plancuenta(conexion):
    def __init__(self):
      super().__init__()

    def consultarplancuenta(self,buscar):
        try:
            sql="SELECT p.idplancuenta,p.descripcion,g.descripcion,p.codigo,p.naturaleza,p.estado from plan_cuenta as p, grupo as g where p.descripcion like'"+str(buscar)+"%' and p.grupo=g.idgrupo"
            # sql="select * from plan_cuenta where descripcion like'"+str(buscar)+"%' order by idplancuenta"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
            if result.__len__()==0:
                
                print('\tSIN RESULTADOS PARA ESTA BUSQUEDA')
            else: 
                    print('\t{}\t{:20}\t{:10}\t{:10}\t{}\t{}'.format('id','descripcion','grupo','codigo','nat','estado').title())
                    for valor in result:
                        naturaleza=str(valor[4])
                        if valor[5]==1:
                            estado='a'
                        else:
                            estado='i'
                        print('\t{}\t{:20}\t{:10}\t{:10}\t{}\t{}'.format(valor[0],valor[1],valor[2],valor[3],naturaleza.upper(),estado.upper()))          
        except Exception as e:
            print('error en la consulta',e)
            self.conn.rollback()
        finally:
            self.cerrar()
#--------------------------------------------------------------------------
    def insertagrupo(self,pln):
        correcto=True 
        try:
            sql="INSERT INTO plan_cuenta( grupo, codigo, descripcion, naturaleza, estado) VALUES (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql,(pln.idgrupo,pln.codigo,pln.descripcion,pln.naturaleza,pln.estado))
            self.conn.commit()
        except Exception as e:
            print('error al insertar ',e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
#----------------------------------------------------------
    def modificaplan(self,pln):
        correcto=True 
        try:
            sql="UPDATE plan_cuenta SET grupo=%s,codigo=%s,descripcion=%s,naturaleza=%s,estado=%s WHERE idplancuenta=%s"
            self.conectar()
            self.conector.execute(sql,(pln.idgrupo,pln.codigo,pln.descripcion,pln.naturaleza,pln.estado,pln.idplancuenta))
            self.conn.commit()
        except Exception as e:
            print('error al modificar ',e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto    

# 2------------------------------------------------------------
    def modificaplanpartes(self,campo,dato,idplan):
        correcto=True 
        try:
            sql="UPDATE plan_cuenta SET {}='{}' WHERE  idplancuenta='{}'".format(campo,dato,idplan)
            self.conectar()
            self.conector.execute(sql)
            self.conn.commit()
        except Exception as e:
            print('error al modificar ',e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto    
#-----------------------------------------------------------
    def eliminaplan(self,pln):
        correcto=True 
        try:
            sql="delete from plan_cuenta where idplancuenta=%s"
            self.conectar()
            self.conector.execute(sql,(pln.idplancuenta))
            self.conn.commit()
        except Exception as e:
            print('error al eliminar ',e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto
# ------------------------------------------------------------------
    def buscarid(self,dato):
        existe=False
        try:
            sql="select * from plan_cuenta where idplancuenta={}".format(dato)
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
            if result.__len__()==0:
                print('\tSIN RESULTADOS PARA ESTA BUSQUEDA')
            else:
                    print('\t{}\t{}\t{}\t{:20}\t{}\t{}'.format('id','grupo','codigo','descrpcion','nat','estado').title())
                    for valor in result:
                        naturaleza=str(valor[4])
                        if valor[5]==1:
                            estado='activo'.upper()
                        else:
                            estado='inactivo'.upper()
                    print('\t{}\t{}\t{}\t{:20}\t{}\t{}'.format(valor[0],valor[1],valor[2],valor[3],naturaleza.upper(),estado))          
        except Exception as e:
            print('error ',e)
        finally:
            self.cerrar()
        return existe


