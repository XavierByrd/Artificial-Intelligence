class Trainer(object):

    # Constructor
    def __init__(self, x, y, answer):

        # The input array has a bias of 1 built into it
        # This is so that inputs of 0 do not 'break' the network
        self.inputs = [x, y, 1]
        self.answer = answer
