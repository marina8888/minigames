import binascii
def main():
    a = "Dima"
    print("a = " + str(a)+'\n')
    # translate "Dima" string into utf-8 format:
    print('in utf-8: ')
    print(str(a.encode("utf-8")) + '\n')
    utf_dima = a.encode("utf-8")
    # translate "Dima" into hex:
    print("a in hex is:")
    print(utf_dima.hex()+'\n')
    # https: // en.wikipedia.org / wiki / Base36
    #translate "Dima" into base 36 system. Call int(number=0, base=10):
    print("a in dec is:")
    print(int(a, 36))


if __name__ == "__main__":
    main()
