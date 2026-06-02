class Solution:
    def isValid(self, s: str) -> bool:
        braket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in s:
            if i not in braket_map:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != braket_map[i]:
                        return False

        return not stack                   