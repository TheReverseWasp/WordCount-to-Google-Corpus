import json

def comZero(n):
    s = str(n)
    while len(s) < 4:
        s = "0" + s
    return s

def main():
    filenames = []
    jf = {}
    for i in range(0, 32):
        filenames.append("2gm-" + comZero(i))
    jf["filenames"] = filenames
    with open("filenames.json", "w") as jsonfile:
        json.dump(jf, jsonfile)

if __name__ == "__main__":
    main()
