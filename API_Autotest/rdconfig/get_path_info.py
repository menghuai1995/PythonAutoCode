import os

class GetPathInfo():
    def __init__(self):
        pass


    def getPeojectPath(self):
        project_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        return project_path

    def getFileName(self,file):
        path = self.getPeojectPath()
        filePath = os.path.join(path, "datas")
        fileName = os.path.join(filePath, file)

        return fileName
