def read_metod(path_to_file_trojkoty):
    print("***************files*******************")
    with open(path_to_file_trojkoty) as files:
        try:
            print(files.read())
        except:
            return -1
    print("***************the end*******************")
    return 0


def my_total_metod(path_to_file_trojkoty: str, path_to_file_obwody: str):
    try:
        with open(path_to_file_trojkoty) as files:
            for line in files:
                line2 = line.split()
                print(line2)
                try:
                    id = int(line2[0])
                    # print(id)
                    flank1 = int(line2[1])
                    flank2 = int(line2[2])
                    flank3 = int(line2[3])
                    if id < 10:
                        sum = ["id:[", str(id), "]**************circuit:[", str(flank1 + flank2 + flank3), ']\n']
                    else:
                        sum = ["id:[", str(id), "]*************circuit:[", str(flank1 + flank2 + flank3), ']\n']
                    if flank1 + flank2 >= flank3 or flank1 + flank2 >= flank3 or flank1 + flank2 >= flank3:
                        with open(path_to_file_obwody, 'a') as files3:
                            files3.writelines(sum)
                            files3.close()
                    # print(flank1)
                    # print(flank2)
                    # print(flank3)
                except IndexError:
                    print('Koniec pliku')
    except:
        return -1
    finally:
        print("Oto efekt:")
        return 0

if __name__ == '__main__':
    read_metod('obwody.txt')
    my_total_metod('/home/michu/PycharmProjects/pierwsze_programy/trojkaty.txt', 'obwody.txt')
    read_metod('obwody.txt')