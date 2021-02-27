


if __name__ == "__main__":
    while True:
        try:
            length = int(input())
            input_set = set()
            for i in range(length):
                temp = int(input())
                input_set.add(temp)
            input_set = list(input_set)

            input_set.sort()
            for item in input_set:
                print(item)
        except Exception as ex:
            break