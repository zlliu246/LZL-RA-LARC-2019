from ml.helper.text_preprocessor import *

def get_vectorized_test_x(lis, vec):
    for i,val in enumerate(lis):
        lis[i] = clean(val)
    return vec.transform(lis)