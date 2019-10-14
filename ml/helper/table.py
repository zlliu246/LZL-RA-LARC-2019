e = enumerate

class Table():
    def __init__(self):
        self._data = {}

    def setTable(self, dic):
        
        assert len(set([len(i) for i in list(dic.values())])) == 1

        self._num_values = len(list(dic.values())[0])

        for k,v in dic.items():
            try:
                v = list(v)
            except:
                print("dictionary values must be of type list")
                return

            max_length = 0
            for i in v:
                this_length = len(str(i))
                if this_length > max_length:
                    max_length = this_length

            if len(str(k)) > max_length:
                max_length = len(str(k))
            
            self._data[k] = {"max_length":max_length, "data":v}
            

    def show(self):
        data = self._data
        lengths = [v["max_length"] for k,v in data.items()]

        def divider():
            print("+-" + "".join(["-"*i+"-+-" for i in lengths]))

        print()
        divider()
        print("| " + "".join([k+" "*(data[k]["max_length"]-len(k))+" | " for k in data]))
        divider()

        for i in range(self._num_values):
            print("| " + "".join([str(val["data"][i]) + " "*(val["max_length"]-len(str(val["data"][i]))) + " | " for val in data.values()]))
            divider()
        
        print()
        divider()
        print("| " + "".join([k+" "*(data[k]["max_length"]-len(k))+" | " for k in data]))
        divider()


        print()
