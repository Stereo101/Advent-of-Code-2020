import requests
import os

#Utility script to download input quickly or use a local copy if already downloaded

#set this to your aoc session cookie from browser dev tools
AOC_SESSION = os.environ["AOC_SESSION"]



class Session(requests.Session):
    def __init__(self, year: int, day: int) -> None:
        super().__init__()
        self.year = year
        self.day = day
        self.cookies = requests.cookies.cookiejar_from_dict({'session': AOC_SESSION})

    @property
    def url(self) -> str:
        return f'https://adventofcode.com/{self.year}/day/{self.day}'

    @property
    def fname(self) -> str:
        return f"day{self.day}.input"

    def problem(self) -> str:
        return self.get(f'{self.url}/input').text

    def fp(self,BIGBOY=False):
        if(not os.path.exists(self.fname)):
            with open(self.fname,"w") as f:
                f.write(self.problem())
        if(BIGBOY):
            return open("bigboy.txt")
        return open(self.fname,"r")
        

    def solution(self, level: int, answer) -> None:
        r = self.post(f'{self.url}/answer', data={
            'level': level,
            'answer': answer
        })
        if 'That\'s the right answer!' in r.text:
            return
        lines = r.text.splitlines()
        for line in lines:
            if '<article>' in line:
                raise RuntimeError(line)
        raise RuntimeError(r.text)
