import pickle
def filter_dump(file_name, object, typename):
    dump_list = []
    for obj in object:
        if typename == type(obj):
            dump_list.append(obj)
    with open(file_name, "wb") as f:
        pickle.dump(dump_list, f)
