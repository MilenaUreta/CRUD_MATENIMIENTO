import sys
from controlador.controlgrupo import ctr_grupo
from controlador.controlplancuenta import ctr_plancuenta
from modelo.clases import *
from controlador.validar import validar
ctgrupo=ctr_grupo()
ctplan=ctr_plancuenta()
plan=plan_cuenta()
grupo=grupo()
validar=validar()
titulo='menu principal'
menu_opciones=['plan de cuentas','grupo de cuentas','salir']
menu_opciones2=['mostrar/buscar','nuevo','modificar','eliminar','menu principal']
menu_modificar=['descripcion','grupo','codigo','naturaleza','estado','todos','dejar de modificar en este plan']


def imprimir_opciones(titulo,opciones):
    print('-'*5,titulo.upper(),'-'*5,'\n')
    for i, c in enumerate(opciones): print((i+1),c.title())

while True:
    imprimir_opciones(titulo,menu_opciones)
    opcion=input('\topcion: ')
    while validar.validaingreso(opcion) or not opcion.isnumeric() or int(opcion)<=0 or int(opcion)>menu_opciones.__len__():
        opcion=input('\tingrese una opcion valida: ')
    opcion=int(opcion)
    if opcion==1:
        while True:
            titulo='menu plan de cuentas'
            imprimir_opciones(titulo,menu_opciones2)
            opcion=input('\topcion: ')
            while validar.validaingreso(opcion) or not opcion.isnumeric() or int(opcion)<=0 or int(opcion)>menu_opciones2.__len__():
                opcion=input('\tingrese una opcion valida: ')
            opcion=int(opcion)
            if opcion==1:
                print('-'*5,'mostrar/buscar'.upper(),'-'*5,'\n')
                print('\tsi no imgresa datos se mostraran todos los registros')
                plan.asigdesc=input('busqueda: '.title())
                while plan.asigdesc.isspace():
                    print('\tlos espacios cuentan como un dato en blanco')
                    print('\tsi presiona la tecla enter sin ingresar datos se mostraran todos los registros')
                    grupo.asigdesc=input('busqueda: '.title())
                ctplan.consultarplancuenta(plan.descripcion)
            
            elif opcion==2:
                print('-'*5,'nuevo plan de cuentas'.upper(),'-'*5,'\n')
                cantidad=input('cuntos planes desea agregar: ')
                while validar.validaingreso(cantidad) or not cantidad.isnumeric() or int(cantidad)<=0:
                    print('ingrese almenos 1 plan de cuentas')
                    cantidad=input('cuntos planes desea agregar: ')
                cantidad=int(cantidad)
                for i in range(cantidad):
                    print('\tdatos del ' +str(i+1)+'º plan')
                    plan.asigdesc=input('descripcion: ')
                    plan.asigcodigo=input('codigo (numerico): ')
                    plan.asignat=input('naturaleza A=Acreedora - D=Deudora : ').lower()
                    plan.asigestado=input('estado 1=Activo - 0=Inactivo : ')
                    ctgrupo.consultargrupo('')
                    plan.asiggrupo=input('estos son los grupos disponibles, selecciona 1\ngrupo de cuenta: ')
                    while validar.validaingreso(plan.descripcion):
                        plan.asigdesc=input('ingrese una descripcion valida: ')
                    while validar.validaingreso(plan.codigo) or not plan.codigo.isnumeric():
                        plan.asigcodigo=input('ingrese un codigo numerico valido: ')
                    while validar.validaingreso(plan.asignat):
                        plan.asignat=input('ingresa un caracter valido, naturaleza A=Acreedora - D=Deudora : ') 
                    while True:
                        if plan.naturaleza=='a'or plan.naturaleza=='d':
                            break
                        else:
                            plan.asignat=input('ingresa un caracter valido, naturaleza A=Acreedora - D=Deudora : ') 
                    while validar.validaingreso(plan.estado) or not plan.estado.isnumeric():
                        plan.asigestado=input('ingrese caractervalido, estado 1=Activo - 0=Inactivo : ')
                    while True:
                        if int(plan.estado)==1 or int(plan.estado)==0:
                            break
                        else:
                            plan.asigestado=input('ingrese caractervalido, estado 1=Activo - 0=Inactivo : ')
                    while validar.validaingreso(plan.idgrupo) or not plan.idgrupo.isnumeric():
                        ctgrupo.consultargrupo('')
                        plan.asiggrupo=input('\tseleciona un grupo\ngrupo de cuenta: ')
                    while not validar.existe('idgrupo','grupo',int(plan.idgrupo)):
                        ctgrupo.consultargrupo('')
                        plan.asiggrupo=input('\tel grupo que ingreso no existe selccione uno de esta lista\ngrupo de cuenta: ')
                    confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                    while validar.validaingreso(confirmar):
                        print('confirme la operacion')
                        confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                    while True:
                        if confirmar=='s' :
                            if ctplan.insertagrupo(plan):
                                ctplan.consultarplancuenta('')
                                print('agregado correctamente')
                                break
                            else:
                                print('error al insertar')
                                break
                        elif confirmar=='n':
                            print('operacion cancelada')
                            break
                        else:
                            print('confirme la operacion')
                            confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()

            elif opcion==3:
                print('-'*5,'modificar plan de cuentas'.upper(),'-'*5,'\n')
                cantidad=input('cuntos planes desea modificar: ')
                while validar.validaingreso(cantidad) or not cantidad.isnumeric() or int(cantidad)<=0:
                    print('modifique almenos 1 plan de cuentas')
                    cantidad=input('cuntos planes desea modificar: ')
                cantidad=int(cantidad)
                for i in range(cantidad):
                    ctplan.consultarplancuenta('')
                    plan.asigidplan=input('\testos son los planes disponibles, selecciona 1\nid del plan a modificar: ')
                    while validar.validaingreso(plan.idplancuenta) or not plan.idplancuenta.isnumeric() or not validar.existe('idplancuenta','plan_cuenta',int(plan.idplancuenta)):
                        plan.asigidplan=input('\tel plan que ingreso no existe, selecciona 1 de esta lisa\nid del plan a modificar: ')
                    ctplan.buscarid(plan.idplancuenta)
                    while True:
                        imprimir_opciones('campos a modificar del '+ str(i+1)+'º plan',menu_modificar)
                        opcion=input('\tseleccione el campo a modificar\n\topcion: ')
                        while validar.validaingreso(opcion) or not opcion.isnumeric() or int(opcion)<=0 or int(opcion)>menu_modificar.__len__():
                            opcion=input('\tingrese una opcion valida: ')
                        opcion=int(opcion)
                        if opcion==1:
                            print('-'*5,'modificar descripcion'.upper(),'-'*5,'\n')
                            plan.asigdesc=input('nueva descripcion: '.title())
                            while validar.validaingreso(plan.descripcion) or plan.descripcion.isnumeric():
                                print('inserta una descripcion valida')
                                plan.asigdesc=input('nueva descripcion: '.title())
                            confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while validar.validaingreso(confirmar):
                                print('confirme la operacion')
                                confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while True:
                                if confirmar=='s' :
                                    if ctplan.modificaplanpartes('descripcion',plan.descripcion,int(plan.idplancuenta)):
                                        ctplan.buscarid(plan.idplancuenta)
                                        print('modificado correctamente')
                                        break
                                    else:
                                        print('error al modificar')
                                        break
                                elif confirmar=='n':
                                    print('operacion cancelada')
                                    break
                                else:
                                    print('confirme la operacion')
                                    confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            ctplan.buscarid(plan.idplancuenta)
                        elif opcion==2:
                            print('-'*5,'cambiar de grupo'.upper(),'-'*5,'\n')            
                            ctgrupo.consultargrupo('')
                            plan.asiggrupo=input('\testos son los grupos disponibles, selecciona 1\nid del grupo: '.title())
                            while validar.validaingreso(plan.idgrupo) or not plan.idgrupo.isnumeric() or not validar.existe('idgrupo','grupo',int(plan.idgrupo)):
                                plan.asiggrupo=input('\tel grupo no existe, selecciona 1 de esta lista\nid del grupo: '.title())
                            confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while validar.validaingreso(confirmar):
                                print('confirme la operacion')
                                confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while True:
                                if confirmar=='s' :
                                    if ctplan.modificaplanpartes('grupo',plan.idgrupo,int(plan.idplancuenta)):
                                        print('modificado correctamente')
                                        break
                                    else:
                                        print('error al modificar')
                                        break
                                elif confirmar=='n':
                                    print('operacion cancelada')
                                    break
                                else:
                                    print('confirme la operacion')
                                    confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            ctplan.buscarid(plan.idplancuenta)
                            
                        elif opcion==3:
                            print('-'*5,'cambiar codigo'.upper(),'-'*5,'\n') 
                            plan.asigcodigo=input('nuevo codigo(numerico): '.title())
                            while validar.validaingreso(plan.codigo) or not plan.codigo.isnumeric():
                                plan.asigcodigo=input('ingrese un codigo numerico valido: ')
                            confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while validar.validaingreso(confirmar):
                                print('confirme la operacion')
                                confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while True:
                                if confirmar=='s' :
                                    if ctplan.modificaplanpartes('codigo',plan.codigo,int(plan.idplancuenta)):
                                        print('modificado correctamente')
                                        break
                                    else:
                                        print('error al modificar')
                                        break
                                elif confirmar=='n':
                                    print('operacion cancelada')
                                    break
                                else:
                                    print('confirme la operacion')
                                    confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            ctplan.buscarid(plan.idplancuenta)
                        elif opcion==4:
                            print('-'*5,'cambiar naturaleza'.upper(),'-'*5,'\n')
                            plan.asignat=input('naturaleza A=Acreedora - D=Deudora : ').lower()
                            while validar.validaingreso(plan.asignat):
                                plan.asignat=input('ingresa un caracter valido, naturaleza A=Acreedora - D=Deudora : ') 
                            while True:
                                if plan.naturaleza=='a'or plan.naturaleza=='d':
                                    break
                                else:
                                    plan.asignat=input('ingresa un caracter valido, naturaleza A=Acreedora - D=Deudora : ') 
                            confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while validar.validaingreso(confirmar):
                                print('confirme la operacion')
                                confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while True:
                                if confirmar=='s' :
                                    if ctplan.modificaplanpartes('naturaleza',plan.naturaleza,int(plan.idplancuenta)):
                                        print('modificado correctamente')
                                        break
                                    else:
                                        print('error al modificar')
                                        break
                                elif confirmar=='n':
                                    print('operacion cancelada')
                                    break
                                else:
                                    print('confirme la operacion')
                                    confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            ctplan.buscarid(plan.idplancuenta)
                        elif opcion==5:
                            print('-'*5,'cambiar estado'.upper(),'-'*5,'\n')
                            plan.asigestado=input('estado 1=Activo - 0=Inactivo : ')
                            while validar.validaingreso(plan.estado) or not plan.estado.isnumeric():
                                plan.asigestado=input('ingrese caractervalido, estado 1=Activo - 0=Inactivo : ')
                            while True:
                                if int(plan.estado)==1 or int(plan.estado)==0:
                                    break
                                else:
                                    plan.asigestado=input('ingrese caractervalido, estado 1=Activo - 0=Inactivo : ')
                            confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while validar.validaingreso(confirmar):
                                print('confirme la operacion')
                                confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            while True:
                                if confirmar=='s' :
                                    if ctplan.modificaplanpartes('estado',plan.estado,int(plan.idplancuenta)):
                                        print('modificado correctamente')
                                        break
                                    else:
                                        print('error al modificar')
                                        break
                                elif confirmar=='n':
                                    print('operacion cancelada')
                                    break
                                else:
                                    print('confirme la operacion')
                                    confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            ctplan.buscarid(plan.idplancuenta)
                        elif opcion==6:
                            print('-'*5,'modificar todos los campos'.upper(),'-'*5,'\n')
                            plan.asigdesc=input('descripcion: ')
                            plan.asigcodigo=input('codigo (numerico): ')
                            plan.asignat=input('naturaleza A=Acreedora - D=Deudora : ').lower()
                            plan.asigestado=input('estado 1=Activo - 0=Inactivo : ')
                            ctgrupo.consultargrupo('')
                            plan.asiggrupo=input('estos son los grupos disponibles, selecciona 1\ngrupo de cuenta: ')
                            while validar.validaingreso(plan.descripcion):
                                plan.asigdesc=input('ingrese una descripcion valida: ')
                            while validar.validaingreso(plan.codigo) or not plan.codigo.isnumeric():
                                plan.asigcodigo=input('ingrese un codigo numerico valido: ')
                            while validar.validaingreso(plan.asignat):
                                plan.asignat=input('ingresa un caracter valido, naturaleza A=Acreedora - D=Deudora : ') 
                            while True:
                                if plan.naturaleza=='a'or plan.naturaleza=='d':
                                    break
                                else:
                                    plan.asignat=input('ingresa un caracter valido, naturaleza A=Acreedora - D=Deudora : ') 
                            while validar.validaingreso(plan.estado) or not plan.estado.isnumeric():
                                plan.asigestado=input('ingrese caractervalido, estado 1=Activo - 0=Inactivo : ')
                            while True:
                                if int(plan.estado)==1 or int(plan.estado)==0:
                                    break
                                else:
                                    plan.asigestado=input('ingrese caractervalido, estado 1=Activo - 0=Inactivo : ')
                                while validar.validaingreso(plan.idgrupo) or not plan.idgrupo.isnumeric():
                                    ctgrupo.consultargrupo('')
                                    plan.asiggrupo=input('\tseleciona un grupo\ngrupo de cuenta: ')
                                while not validar.existe('idgrupo','grupo',int(plan.idgrupo)):
                                    ctgrupo.consultargrupo('')
                                    plan.asiggrupo=input('\tel grupo que ingreso no existe selccione uno de esta lista\ngrupo de cuenta: ')
                                confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                                while validar.validaingreso(confirmar):
                                    print('confirme la operacion')
                                    confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                                while True:
                                    if confirmar=='s' :
                                        if ctplan.modificaplan(plan):
                                            print('modificado correctamente')
                                            break
                                        else:
                                            print('error al modificar')
                                            break
                                    elif confirmar=='n':
                                        print('operacion cancelada')
                                        break
                                    else:
                                        print('confirme la operacion')
                                        confirmar=input('\t¿guardar cambios? s=si n=no : '.title()).lower()
                            ctplan.buscarid(plan.idplancuenta)
# ----------------------------------------------------------------------------------------------------------
                        else:
                            break
            elif opcion==4:
                print('-'*5,'eliminar plan de cuentas'.upper(),'-'*5,'\n')
                cantidad=input('cuntos planes desea eliminar: ')
                while validar.validaingreso(cantidad) or not cantidad.isnumeric() or int(cantidad)<=0:
                    print('elimine almenos 1 plan de cuentas')
                    cantidad=input('cuntos planes desea eliminar: ')
                cantidad=int(cantidad)
                for i in range(cantidad):
                    ctplan.consultarplancuenta('')
                    plan.asigidplan=input('\testos son los planes disponibles, selecciona 1\nid del '+str(i+1)+'º plan a eliminar: ')
                    while validar.validaingreso(plan.idplancuenta) or not plan.idplancuenta.isnumeric():
                        plan.asigidplan=input('\tselecciona 1 de los planes de esta lista\nid del '+str(i+1)+'º plan a eliminar: ')
                    while validar.validaingreso(plan.idplancuenta) or not validar.existe('idplancuenta','plan_cuenta',int(plan.idplancuenta)):
                        plan.asigidplan=input('\tel plan que ingreso no existe, selecciona 1 de esta lista\nid del plan a eliminar: ')
                    confirmar=input('guardar cambios? s=si - n=no: '.title()).lower()
                    while validar.validaingreso(confirmar) or confirmar.isnumeric():
                        print('confirme la operacion')
                        confirmar=input('guardar cambios? s=si - n=no: '.title()).lower()
                    while True:
                            if confirmar=='s' or confirmar=='n':
                                if confirmar=='s':
                                    if ctplan.eliminaplan(plan):
                                        print('\teliminado correctamente')
                                        break
                                    else:
                                        print('\terror al eliminae') 
                                        break
                                else:
                                    print('\toperacion cancelada')
                                    break               
                            else:
                                print('confirme la operacion')
                                confirmar=input('¿guardar cambios? s=si - n=no: '.title()).lower()
                    ctplan.consultarplancuenta('')
            else :
                confirmar=input('¿volver al menu principla? s=si n=no : '.title()).lower()
                # while validar.validaingreso(confirmar) or confirmar.isnumeric():
                #     confirmar=input('\tconfirme la operacion\n¿volver al menu principla? s=si n=no : '.title()).lower()
                while True:
                    if confirmar=='s' or confirmar=='n':
                        titulo='menu principal'
                        break
                    else:
                        confirmar=input('\tconfirme la operacion\n¿volver al menu principla? s=si n=no : '.title()).lower()
                if confirmar=='s':
                    break
                else:
                    print('operacion cancelada')

    elif opcion==2:
        while True:
                titulo='menu grupo de cunetas'
                imprimir_opciones(titulo,menu_opciones2)
                opcion=input('\topcion: ')
                while validar.validaingreso(opcion) or not opcion.isnumeric() or int(opcion)<=0 or int(opcion)>menu_opciones2.__len__():
                  opcion=input('\tingrese una opcion valida: ')
                opcion=int(opcion)
                if opcion==1:
                    print('-'*5,'mostrar/buscar'.upper(),'-'*5,'\n')
                    print('\tsi no imgresa datos se mostraran todos los registros')
                    grupo.asigdesc=input('busqueda: '.title())
                    while grupo.asigdesc.isspace():
                        print('\tlos espacios cuentan como un dato en blanco')
                        print('\tsi presiona la tecla enter sin ingresar datos se mostraran todos los registros')
                        grupo.asigdesc=input('busqueda: '.title())
                    ctgrupo.consultargrupo(grupo.descripcion)

                elif opcion==2:
                    print('-'*5,'nuevo grupo'.upper(),'-'*5,'\n')
                    cantidad=input('cuntos grupos desea agregar: ')
                    while validar.validaingreso(cantidad) or not cantidad.isnumeric() or int(cantidad)<=0:
                        print('ingrese almenos 1 grupo')
                        cantidad=input('cuntos grupos desea agregar: ')
                    cantidad=int(cantidad)
                    for i in range(cantidad):
                        grupo.asigdesc=input('descripcion: '.title())
                        while validar.validaingreso(grupo.descripcion) or grupo.descripcion.isnumeric():
                            print('inserta una descripcion valida')
                            grupo.asigdesc=input('descripcion: '.title())
                        while  validar.existe('descripcion','grupo',grupo.descripcion):
                            print('el grupo ya existe, intenta de nuevo')
                            grupo.asigdesc=input('descripcion: '.title())
                        confirmar=input('guardar? s=si - n=no: '.title()).lower()
                        while validar.validaingreso(confirmar) or confirmar.isnumeric():
                            print('confirme la operacion')
                            confirmar=input('guardar? s=si - n=no: '.title()).lower()
                        while True:
                                if confirmar=='s' or confirmar=='n':
                                    if confirmar=='s':
                                        if ctgrupo.insertagrupo(grupo):
                                            print('\tagregado correctamente')
                                            break
                                        else:
                                            print('\terror al agrrgar') 
                                            break
                                    else:
                                        print('\toperacion cancelada')
                                        break               
                                else:
                                    print('confirme la operacion')
                                    confirmar=input('¿guardar? s=si - n=no: '.title()).lower()
                elif opcion==3:
                    print('-'*5,'modificar'.upper(),'-'*5,'\n')
                    cantidad=input('cuntos grupos desea modificar: ')
                    while validar.validaingreso(cantidad) or not cantidad.isnumeric() or int(cantidad)<=0:
                        print('modifique almenos 1 grupo')
                        cantidad=input('cuntos grupos desea modificar: ')
                    cantidad=int(cantidad)
                    for i in range(cantidad):
                        ctgrupo.consultargrupo('')
                        grupo.asigid=input('\testos son los grupos disponibles, selecciona 1\nid del grupo: '.title())
                        while validar.validaingreso(grupo.id) or not grupo.id.isnumeric() or not validar.existe('idgrupo','grupo',int(grupo.id)):
                             grupo.asigid=input('ingresa el id de un grupo de la lista: '.title())
                        ctgrupo.buscarid(grupo.id)
                        grupo.asigdesc=input('nueva descripcion: ')
                        while validar.validaingreso(grupo.descripcion) or grupo.descripcion.isnumeric() or validar.existe('descripcion','grupo',grupo.descripcion):
                            print('el grupo ya existe o la descripcion no es valida, intentalo de nuevo')
                            grupo.asigdesc=input('nueva descripcion: ')
                        confirmar=input('¿gusrdar? s=si - n=no: '.title()).lower()
                        while validar.validaingreso(confirmar) or confirmar.isnumeric():
                            print('confirme la operacion')
                            confirmar=input('¿gusrdar? s=si - n=no: '.title()).lower()
                        while True:
                            if confirmar=='s' or confirmar=='n':
                                if confirmar=='s':
                                    if ctgrupo.modificagrupo(grupo):
                                        print('\tmodificado correctamente')
                                        break
                                    else:
                                        print('\terror al modificar') 
                                        break
                                else:
                                    print('\toperacion cancelada')
                                    break               
                            else:
                                print('confirme la operacion')
                                confirmar=input('¿gusrdar? s=si - n=no: '.title()).lower()
                elif opcion==4:
                    cantidad=input('cuntos grupos desea eliminar: ')
                    while validar.validaingreso(cantidad) or not cantidad.isnumeric() or int(cantidad)<=0:
                        print('elimine almenos 1 grupo')
                        cantidad=input('cuntos grupos desea eliminar: ')
                    cantidad=int(cantidad)
                    for i in range(cantidad):
                        print('-'*5,'eliminar'.upper(),'-'*5,'\n')
                        ctgrupo.consultargrupo('')
                        grupo.asigid=input('\testos son los grupos disponibles, selecciona 1\nid del grupo: '.title())
                        while validar.validaingreso(grupo.id) or not grupo.id.isnumeric() or not validar.existe('idgrupo','grupo',int(grupo.id)):
                            grupo.asigid=input('ingresa el id de un grupo de la lista: '.title())
                        confirmar=input('¿gusrdar? s=si - n=no: '.title()).lower()
                        while validar.validaingreso(confirmar) or confirmar.isnumeric():
                            print('confirme la operacion')
                            confirmar=input('¿gusrdar? s=si - n=no: '.title()).lower()
                        while True:
                            if confirmar=='s' or confirmar=='n':
                                if confirmar=='s':
                                    if ctgrupo.eliminagrupo(grupo):
                                        print('\teliminado correctamente')
                                        break
                                    else:
                                        print('\terror al eliminar') 
                                        break
                                else:
                                    print('\toperacion cancelada')
                                    break               
                            else:
                                print('confirme la operacion')
                                confirmar=input('¿gusrdar? s=si - n=no: '.title()).lower()
                            
                elif opcion==5:
                    confirmar=input('¿volver al menu principla? s=si n=no : '.title()).lower()
                    while True:
                        if confirmar=='s' or confirmar=='n':
                            titulo='menu principal'
                            break
                        else:
                            confirmar=input('\tconfirme la operacion\n¿volver al menu principla? s=si n=no : '.title()).lower()
                    if confirmar=='s':
                        break
                    else:
                        print('operacion cancelada')
    else:
        confirmar=input('¿salir? s=si n=no : '.title()).lower()
        while True:
            if confirmar=='s' or confirmar=='n':
                break
            else:
                confirmar=input('\tconfirme la operacion\n¿salir? s=si n=no : '.title()).lower()
        if confirmar=='s':
            print('\tgracias por usar este servicio'.title())
            sys.exit(1)
            break
        else:
            print('operacion cancelada')
