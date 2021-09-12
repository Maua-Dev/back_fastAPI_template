import json
import os


class ProjConfig:
    PROJ_ROOT_ABS_PATH = os.path.abspath('.')

    @staticmethod
    def getDeployment():
        return ProjConfig.fromJSON(os.path.join(ProjConfig.PROJ_ROOT_ABS_PATH, 'config', 'files', 'deployment.json'))

    @staticmethod
    def getFastapi():
        return ProjConfig.fromJSON(os.path.join(ProjConfig.PROJ_ROOT_ABS_PATH, 'config', 'files', 'fastapi.json'))

    @staticmethod
    def fromJSON(path):
        with open(path) as file:
            return json.load(file)
