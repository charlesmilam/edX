'''
If f(a, b) returns a + b
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
If f(a, b) returns a > b
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
'''
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter_keys = {}
    inter_ans = {}

    for idx, key in enumerate(d1.keys()):
        if key in d2.keys():
            inter_keys[idx] = key

    print inter_keys
    # for key in inter_keys:
    #     inter_ans[key] = f(d1[key], d2[key])

dict_interdiff(d1, d2)
