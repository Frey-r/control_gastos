class BarcodeController:
    def __init__(self,digits):
        self.pais = digits[0:2]
        self.empresa_marca = digits[3:5]
        self.producto = digits[6:-2]
        self.control = digits[-1]
        pass

    def get_producto(self):
        return self.producto
    
    def get_control(self):
        return self.control
    
    def get_pais(self):
        return self.pais
    
    def get_empresa_marca(self):
        return self.empresa_marca