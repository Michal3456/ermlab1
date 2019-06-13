import random
def first_total_method_inputs():
    id=1
    print("Inscribe  [<First flank>[space]<Second flank>[space]<Third flank>] ")
    s_flank=input()
    print(s_flank)
    return s_flank

def write_to_file(s_flank, path_to_file_trojkoty: str):
    s_flank_2 = s_flank.split()
    flank_1 = int(s_flank_2[0])
    flank_2 = int(s_flank_2[1])
    flank_3 = int(s_flank_2[2])
    for id in range(0,100000):
        with open(path_to_file_trojkoty, "a") as files:
            try:
                files.write("%d %d %d %d\n" %(id, flank_1, flank_2, flank_3))
            except:
                return -1
            finally:
                flank_1 = random.randint(1, 9)
                flank_2 = random.randint(1, 9)
                flank_3 = random.randint(1, 9)
    return 0
def print_result():
    print("Oto efekt:")
    with open('trojkaty.txt',"r") as files:
        try:
            text = files.read()
        finally:
            print(text)

if __name__ == '__main__':
    write_to_file(first_total_method_inputs(),'trojkaty.txt')
    print_result()