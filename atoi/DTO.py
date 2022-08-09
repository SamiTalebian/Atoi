class AtoiDTO:
    def deserializer(self, data):
        return{
            'atoi_string' : data['atoi']
        }