class Asistente:
    rut=0
    num_asiento=0
    valor=0

    def __int__(self):
        self.rut=11111111
        self.num_asiento=1
        self.valor=120000

    def setRut(self,rut):
        if len(rut)==8:
            if rut[0:8].isdigit():
                self.rut=rut
                return True
            else:
                print("Ingrese solo numeros")
                return False
        else:
            print("Largo incorrecto")
            return False