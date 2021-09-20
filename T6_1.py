with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    result = []
    while line:
        new_tuple = (line.split(' - - ')[0], line.split(' - - ')[1].split('"')[1].split(' ')[0], line.split(' - - ')[1].split(' ')[3])
        result.append(new_tuple)
        line = f.readline()
print(result)
print(result[0])
print(result[-1])
