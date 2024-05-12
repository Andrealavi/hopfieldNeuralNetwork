from typing import Optional

class HopfieldNetwork:
    def __init__(self) -> None:
        self.patterns: list[list[list[int]]] = []
        self.weigths: list[list[float]] = []

    def add_pattern(self, pattern: list[list[int]]) -> None:
        self.patterns.append(pattern)

    def train(self) -> None:
        self.weigths = []
        n: int = len(self.patterns[0][0])*len(self.patterns[0][0])

        for i in range(n):
            row_weigths: list[float] = []

            for j in range(n):
                if (i == j):
                    row_weigths.append(0.0)
                else:
                    sum: float = 0.0

                    for k in range(len(self.patterns)):
                        sum += self.patterns[k][i // len(self.patterns[0][0])][i % len(self.patterns[0][0])] * self.patterns[k][j // len(self.patterns[0][0])][j % len(self.patterns[0][0])]
                        

                    sum *= 1/len(self.patterns)
                    row_weigths.append(sum)

            self.weigths.append(row_weigths)

    def get_weights(self) -> list[list[float]]:
        return self.weigths
    
    def print_weights(self) -> None:
        for i in range(len(self.weigths)):
            for j in range(len(self.weigths[0])):
                print(self.weigths[i][j], sep=' ', end=' ')
            print()

    def checkMatch(self, classification) -> Optional[list[list[int]]]:
        for pattern in self.patterns:
            isEqual: bool = True
            for i in range(len(pattern)):
                for j in range(len(pattern[0])):
                    if (-1 if classification[i][j] == 0 else 1) != pattern[i][j]:
                        isEqual = False

            if isEqual:
                return classification                    

        return None

    def classify(self, img: list[list[int]]) -> Optional[list[list[int]]]:
        prev: list[list[int]] = img
        curr: list[list[int]] = []

        for k in range(100):
            for i in range(len(prev)):
                row_curr: list[int] = []

                for j in range(len(prev[0])):
                    sum: float = 0.0

                    for l in range(len(self.weigths[0])):
                        sum += self.weigths[(i * len(prev[0])) + (j % len(prev[0]))][l] * prev[l // len(self.patterns[0])][l % len(self.patterns[0][0])]

                    if (sum > 0):
                        row_curr.append(1)
                    else:
                        row_curr.append(0)

                curr.append(row_curr)
            prev = curr
            curr = []

        return self.checkMatch(prev)

