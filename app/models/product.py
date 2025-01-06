class Product:
    def __init__(self, id, title, price, description, category, image):
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.image = image
    
    def to_dict(self):
        """Convert product instance to dictionary, excluding id if it's None"""
        data = {
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'category': self.category,
            'image': self.image
        }
        if self.id is not None:
            data['id'] = self.id
        return data
