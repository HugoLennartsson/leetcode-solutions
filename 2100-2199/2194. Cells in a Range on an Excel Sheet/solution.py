class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return_list = list()

        for uni in range(ord(s[0]), ord(s[-2]) + 1):
            for num in range(int(s[1]), int(s[-1]) + 1):
                cell = chr(uni) + str(num)
                return_list.append(cell)
        return return_list