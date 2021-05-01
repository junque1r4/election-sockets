class CreateElection:
    def __init__(self, candidates=None) -> None:
        if candidates is None:
            self.candidates = list()
        
        self.candidates = list()

    def set_candidates(self, **kwargs: str) -> None:
        for key, value in kwargs.items():
            self.candidates.append([
                {f'{value}': f'{key}'},
                {'votes': 0}
            ])

    def vote_for(self, candidate: str = None):
        for each in self.candidates:
            if each[0].get(candidate, 0) != 0:
                each[1]['votes'] += 1

    def show(self):
        data = ''
        for each in self.candidates:
            for k, v in each[0].items():
                data += f'\nCandidato {v} de numero {k}'

        return f'{data}'

    def show_info(self):
        data = ''
        for each in self.candidates:
            for k, v in each[0].items():
                for y, z in each[1].items():
                    data += f'\nVotos para {v}[{k}]: {z}'

        return f'{data}'
