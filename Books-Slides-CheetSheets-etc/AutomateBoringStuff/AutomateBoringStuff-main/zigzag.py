import sys, time

indent = 0
indentIncrease = True

try:
    while True:
            print(' ' * indent, end='')         #print("" + str(indent), end="")
            print('*****')
            time.sleep(0.000000000000000001)

            if indentIncrease == True:
                indent = indent + 1

                if indent == 20:
                    indentIncrease = False

            else:
                indent = indent - 1

                if indent == 0:
                    indentIncrease = True

except KeyboardInterrupt:
    sys.exit()
