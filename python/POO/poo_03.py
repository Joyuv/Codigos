class aluno:

    def __init__(self, aluno, matricula, curso):
        self.__aluno = aluno
        self.__matricula = matricula
        self.__curso = curso

    def get_aluno(self):
        return self.__aluno
    def get_matricula(self):
        return self.__matricula
    def get_curso(self):
        return self.__curso
    
    def set_aluno(self, aluno):
        self.__aluno = aluno
    def set_matricula(self, matricula):
        self.__matricula = matricula
    def set_curso(self, curso):
        self.__curso = curso

