def format_input(inp_list, inp_bound) -> list:
    result = []
    inp_list = [['0:00', inp_bound[0]]]+inp_list+[[inp_bound[1], '24:00']]
    for i in inp_list:
        h, m = i[0].split(':')
        h1, m1 = i[1].split(':')
        result.append([int(h)*60+int(m), int(h1) * 60 + int(m1)])
    return result


def get_free_time(inp_list) -> list:
    result = []
    for i in range(0, len(inp_list) - 1, 1):
        if inp_list[i + 1][0] - inp_list[i][1] >= 30:
            result.append([inp_list[i][1], inp_list[i + 1][0]])
    return result


def format_output(inp_list) -> list:
    result = []
    for i in inp_list:
        hour_from = str(i[0]//60)
        minute_from = str(i[0] % 60)
        hour_to = str(i[1]//60)
        minute_to = str(i[1] % 60)
        result.append([hour_from+':'+minute_from, hour_to+':'+minute_to])
    return result


def get_free_block(cal1, bound1, cal2, bound2) -> list:
    return format_output(
             get_free_time(
                    sorted(format_input(cal1, bound1)+format_input(cal2, bound2))))

