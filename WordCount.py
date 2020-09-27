import re
import json
import threading
import time

dicFile = {}
dicResultados = {}
regWord = "[a-z]*$"
pathDatos = "Datos/"
pathResultados = "Resultados/"
filenames = []

def threadfun(filename):
    print("Thread " + filename + " beggining...")
    with open(pathDatos + filename, "r") as rf:
        while True:
            line = rf.readline()
            if not line:
                break
            line = line.lower()
            line = re.findall("[a-z]+", line)
            for i in line:
                if i in dicFile[filename]:
                    dicFile[filename][i] += 1
                else:
                    dicFile[filename][i] = 1
    print("Thread " + filename + " writting...")
    with open(pathResultados + filename +".json", "w") as wf:
        json.dump(dicFile[filename], wf)
    print("Thread " + filename + " finished... :D")

def joiner(filenames, ini, fin):
    print("Joiner beggining...")
    for i in range(ini, fin):
        if i == len(filenames):
            break
        filename = filenames[i]
        print("Joining file " + filename)
        for k, v in dicFile[filename].items():
            if k in dicResultados:
                dicResultados[k] += v
            else:
                dicResultados[k] = v
        dicFile[filename] = {}
    with open(pathResultados + "Resultado_final.json", "w") as wf:
        json.dump(dicResultados, wf)
    print("Joiner finished")

def getThread(filenames):
    threadList = []
    for i in filenames:
        threadList.append(threading.Thread(target=threadfun, args=(i,)))
    return threadList

def main():
    with open("filenames.json", "r") as jsonfile:
        filenames = json.load(jsonfile)
    for i in filenames["filenames"]:
        dicFile[i] = {}
    filenames = filenames["filenames"]
    threadList = getThread(filenames)
    ini, fin = 0, 0

    start_time = time.time()
    joinerthread = threading.Thread(target=joiner, args=(filenames, 0, 0,))
    joinerthread.start()
    while fin < len(threadList):
        it1, it2 = 0, 0
        while it1 < 8:
            threadList[ini].start()
            ini += 1
            it1 += 1
            if ini == len(threadList):
                break
        while it2 < 8:
            threadList[fin].join()
            fin += 1
            it2 += 1
            if fin == len(threadList):
                break
        joinerthread.join()
        joinerthread = threading.Thread(target=joiner, args=(filenames, fin - 8, fin))
        joinerthread.start()
        print(fin-8, fin)
    joinerthread.join()

    print("Tiempo de ejecución: ", time.time() - start_time)

if __name__ == "__main__":
    main()
