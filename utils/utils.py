def get_flat_list(list_of_lists):
    """This method merges list of sublists into a flat list"""
    flat_list = []
    for sublist in list_of_lists:
        for item in sublist:
            flat_list.append(item)
    return flat_list


def count_word_occurrences(data_list, *args):
    counted = {}
    for item in data_list:
        for key in item:
            subcounted = {}
            for arg in args:
                arg_count = item[key].lower().count(arg.lower())
                subcounted[f"{arg} occurrences"] = arg_count
            counted[key] = subcounted
    return counted


def count_average_word_occurrence(data_list, str1, str2, str3):
    str1_counted = 0
    str2_counted = 0
    str3_counted = 0
    for item in data_list:
        for key in item:
            str1_count = item[key].lower().count(str1.lower())
            str2_count = item[key].lower().count(str2.lower())
            str3_count = item[key].lower().count(str3.lower())
            str1_counted += str1_count
            str2_counted += str2_count
            str3_counted += str3_count
    return {f"{str1} average occurrence": str1_counted/len(data_list),
            f"{str2} average occurrence": str2_counted/len(data_list),
            f"{str3} average occurrence": str3_counted/len(data_list)}
