import visai_pb2

class ToProtoc:
    def __init__(self) -> None:
        pass

    def add(self, params:dict) -> bytes:
        self.reset()
        self.car.id           = params['id']
        self.car.image_data   = params['image_data']
        self.car.datetime     = params['datetime']
        self.car.bounding_box = params['bounding_box']
        self.car.lat          = params['lat']
        self.car.long         = params['long']
        return self.car.SerializeToString()

    def reset(self) -> None:
        self.car = visai_pb2.Car()
        