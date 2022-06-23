class Solution:
    def decodeString2(self, s: str) -> str:
        stack = []
        token = ""
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                if len(token) > 0 and 'a' <= token[-1] <= 'z':
                    stack.append(token)
                    token = ""
                token += s[i]
            elif 'a' <= s[i] <= 'z':
                if len(token) > 0 and '0' <= token[-1] <= '9':
                    stack.append(token)
                    token = ""
                token += s[i]
            elif s[i] == '[':
                stack.append(int(token))
                stack.append("[")
                token = ""
            else:  # ']'
                stack.append(token)
                combined = ""
                while stack:
                    word = stack.pop()
                    if word == "[":
                        count = stack.pop()
                        temp = ""
                        for _ in range(count):
                            temp = temp + combined
                        combined = temp
                        break
                    else:
                        combined = word + combined
                stack.append(combined)
                token = ""
        if len(token) > 0:
            stack.append(token)

        res = ""
        while stack:
            res = stack.pop() + res
        return res

    def decodeString(self, s: str) -> str:
        stack = []
        count = 0
        word = ''
        for ch in s:
            if ch == '[':
                stack.append(word)
                stack.append(count)
                word = ''
                count = 0
            elif ch == ']':
                num = stack.pop()
                prev = stack.pop()
                word = prev + num * word
            elif ch.isdigit():
                count = count * 10 + int(ch)
            else:  # ch.isalpha():
                word += ch
        print(word)
        return word


if __name__ == '__main__':
    sol = Solution()
    # assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    # assert sol.decodeString("3[a2[c]]") == "accaccacc"
    # assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert sol.decodeString("3[a]2[b3[fgh]4[c]]") == "aaabfghfghfghccccbfghfghfghcccc"