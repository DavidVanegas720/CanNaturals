from flask_app.config.mysqlconnection import connectToMySQL

class Productos_has_orders:

    def __init__(self, data):
        self.productos_id = data['productos_id']
        self.order_id = data['orderi_id']

        