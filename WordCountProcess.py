import re
import json
from multiprocessing import Process
import time

dicFile = {}
dicResultados = {}
regWord = "[a-z]*$"
pathDatos = "Datos/"
pathResultados = "Resultados/"

def processfun(filename):
    print("Process " + filename + " beggining...")
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
    print("Process " + filename + " writting...")
    with open(pathResultados + filename +".json", "w") as wf:
        json.dump(dicFile[filename], wf)
    print("Process " + filename + " finished... :D")

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

def getProcess(filenames):
    ProcessList = []
    for i in filenames:
        ProcessList.append(Process(target=processfun, args=(i,)))
    return ProcessList

def main():
    with open("filenames.json", "r") as jsonfile:
        filenames = json.load(jsonfile)
    for i in filenames["filenames"]:
        dicFile[i] = {}
    filenames = filenames["filenames"]
    processList = getProcess(filenames)
    ini, fin = 0, 0

    start_time = time.time()

    joinerprocess = Process(target=joiner, args=(filenames,0,0,))
    joinerprocess.start()
    while fin < len(processList):
        it1, it2 = 0, 0
        while it1 < 8:
            processList[ini].start()
            ini += 1
            it1 += 1
            if ini == len(processList):
                break
        while it2 < 8:
            processList[fin].join()
            fin += 1
            it2 += 1
            if fin == len(processList):
                break
        joinerprocess.join()
        joinerprocess = Process(target=joiner, args=(filenames, fin - 8, fin))
        joinerprocess.start()
    joinerprocess.join()

    print("Tiempo de ejecución: ", time.time() - start_time)

if __name__ == "__main__":
    main()
