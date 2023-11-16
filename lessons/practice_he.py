from typing import List, Dict

def zip(str_list: List[str], int_list: List[int]) -> Dict[str, int]:
    if len(str_list) != len(int_list):
        return {}  # Different lengths, return an empty dictionary

    zipped_dict = dict(zip(str_list, int_list))
    return zipped_dict
