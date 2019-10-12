def histogram(values):
    for i in values:
        output = ""
        while(i > 0):
            output = output + "*"
            i = i - 1
        print(output)
print(histogram([2,4,6,8]))
