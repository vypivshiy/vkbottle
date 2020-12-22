from .abc import ABCTokenGenerator
from typing import List


class ConsistentTokenGenerator(ABCTokenGenerator):
    def __init__(self, tokens: List[str]):
        self.tokens = tokens
        self.index = 0

    async def get_token(self) -> str:
        i = self.index
        self.index = i + 1 if i < len(self.tokens) + 1 else 0
        return self.tokens[i]
