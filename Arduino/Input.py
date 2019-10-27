import urllib.request

def parser():

    s = input('--> ')

    width = 0
    height = 0
    arrayzs = [["","","","","","",""],["","","","","","",""],["","","","","","",""]]

    for line in s:
        line = line.decode(encoding)
        line = line.split(">")
        for element in line:
            element = element.strip()
            if height < 3:
                if width < 7:
                    arrayzs[height][width] = element
                    width = width + 1
                else :
                    height = height + 1
                    width = 0
            else:
                print("too many lines")
                break

    return arrayzs
