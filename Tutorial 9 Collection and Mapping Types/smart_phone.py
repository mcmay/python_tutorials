class SmartPhone:
    def __init__(self, obj):  # dunder methods: double underlines methods
        self.brand = obj['brand']
        self.model = obj['model']
        self.price = obj['price']
        self.cam_res = obj['maximum camera resolution']
        self.cell_tech = obj['cellular tech']
        self.scrn_sz = obj['screen size']
        self.scrn_res = obj['screen resolution']
        self.ram_sz = obj['RAM size']
        self.model_year = obj['model year']

    def __repr__(self):
        desc = f'brand: {self.brand}\n model: {self.model}\n price: US${round(self.price, 2)}\n ' \
               f'maximum camera resolution: {self.cam_res} MP\n cellular tech: {self.cell_tech}\n ' \
               f'screen size: {round(self.scrn_sz, 2)} in\n screen resolution: {self.scrn_res} pixels\n ' \
               f'RAM size: {self.ram_sz} GB\n model_year: {self.model_year}\n'

        return desc

    def __eq__(self, other):
        if isinstance(other, SmartPhone):
            me = (self.brand, self.model, self.price, self.cam_res, self.cell_tech, self.scrn_sz,
                  self.scrn_res, self.ram_sz, self.model_year)
            you = (other.brand, other.model, other.price, other.cam_res, other.cell_tech, other.scrn_sz,
                   other.scrn_res, other.ram_sz, other.model_year)

            return me == you

        return NotImplemented

    def __hash__(self):
        return hash((self.brand, self.model, self.price, self.cam_res, self.cell_tech, self.scrn_sz,
                  self.scrn_res, self.ram_sz, self.model_year))