
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, photocard):
        if photocard.idPhotocard not in self.carrito.keys():
            self.carrito[photocard.idPhotocard]={
                "photocard_id":photocard.idPhotocard, 
                "marca": photocard.marca,
                "modelo": photocard.modelo,
                "precio": str (photocard.precio),
                "cantidad": 1,
                "total": photocard.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==photocard.idPhotocard:
                    if value["cantidad"] < photocard.stock:
                        value["cantidad"] = value["cantidad"]+1
                        value["precio"] = photocard.precio
                        value["total"]= value["total"] + photocard.precio
                    else:
                        value["cantidad"] = value["cantidad"]+0
                    break
        self.guardar_carrito()


    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, photocard):
        id = photocard.idPhotocard
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,photocard):
        for key, value in self.carrito.items():
            if key == photocard.idPhotocard:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- photocard.precio
                if value["cantidad"] < 1:   
                    self.eliminar(photocard)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 
