class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []

        for char in s:
            if char in "{[(":
                tracker.append(char)
            else:
                # We've encountered a closed bracket but no open brackets
                if len(tracker) == 0:
                    return False

                bra = tracker.pop()
                if bra != "{" and char == "}":
                    return False

                if bra != "[" and char == "]":
                    return False

                if bra != "(" and char == ")":
                    return False

        return len(tracker) == 0
