import pandas as pd
import re
import csv  


def read_txt_file(file_name):
    f = open(file_name, "r")
    return f.read()


def write_csv_file(data):
    header = ["Permission", "Role", "Role Type"]

    with open('permission_full.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write the data
        writer.writerows(data)


if __name__ == "__main__":
    target_string = read_txt_file('permissions_raw.txt')
    count = 0
    re_list = list(re.finditer(r'([\w]+\.[\w]+\.+[\w])\w+', target_string))
    end_re_list = re_list + ['']
    data = []

    for match, match2 in zip(re_list, end_re_list[1:]):
        count += 1
        start = match.end()
        if match2 == "":
            end = -1
        else:
            end = match2.start()
        
        permission = match.group()
        # print("match", count, match.group(), "start index", start, "End index", end)
        list_sep = target_string[start:end]
        arr_list_sep = list_sep.split("\n")
        for role in arr_list_sep:
            if role != '':
                role_type = ''
                if role.startswith("Owner") or role.startswith("Editor") or role.startswith("Viewer"):
                    role_type = "Basics Role"
                else:
                    role_type = "Predefined Role"
                data.append([permission, role, role_type])

    write_csv_file(data)