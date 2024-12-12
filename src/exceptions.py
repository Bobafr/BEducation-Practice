#Это класс, нужный для поиска ошибок в случае когда небыло переданно необходимые детали окружения
#К примеру имя БД

class MissingEnvironment(Exception):
    def __init__(self, var_name):
        self.var_name = var_name
    def __str__(self):
        return f"Variable with name {self.var_name} is missing"
    pass