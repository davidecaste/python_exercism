#!/usr/bin/env python3

def transform(legacy_data):
    new_dic = {}
    for key, lst in legacy_data.items():
        for item in lst:
            new_dic[item.lower()] = key 
    return new_dic