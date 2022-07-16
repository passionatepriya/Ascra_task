def single_flatten_list(nested_list):
    single_list = []
    for element in nested_list:
        if type(element) is list:
            for item in element:
                if item is None or item=="nill" or item=="null":
                    pass
                
                else:
                    single_list.append(item)
        else:
            if element is None or element=="nill" or element=="null":
                pass
            else:
                single_list.append(element)
    return single_list




nested_list = [1,None,[ 2,None, 3,"nill", 4], [5,"null", 6, 7], [8, 9, 10]]
print('Single Flatten List', single_flatten_list(nested_list))