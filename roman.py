global roman_list
roman_list = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
def romanrev(rom):
    # if rom <= 20:
        for i in rom:
            print(roman_list[i])
rom = list(input().split())
romanrev(rom)
