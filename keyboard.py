import convert

def gather_numbers()->list[float]:
    count = []
    while True or None:
        temp = input("poop: ")
        if temp == "done":
            break
        put = convert.str_to_float(temp)
        if put != None:
            count.append(put)
    return count



if __name__ == '__main__':
    a = gather_numbers()
    print(a)
