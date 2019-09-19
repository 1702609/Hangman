import json

class statManager:
    gameWin = True

    @staticmethod
    def updateStat():
        if statManager.gameWin:
            requiredStat = "totalWin"
        else:
            requiredStat = "totalLoss"
        with open('stat.json', 'r+') as f:
            dataStat = json.load(f)
            previousNumber = dataStat[requiredStat]
            dataStat[requiredStat] = previousNumber + 1
            f.seek(0)
            f.truncate()
            json.dump(dataStat, f)

    @staticmethod
    def setWin(flag):
        statManager.gameWin = flag

    @staticmethod
    def getWin():
        with open('stat.json', 'r+') as f:
            dataStat = json.load(f)
            win = dataStat["totalWin"]
        return win

    @staticmethod
    def getLoss():
        with open('stat.json', 'r+') as f:
            dataStat = json.load(f)
            loss = dataStat["totalLoss"]
        return loss