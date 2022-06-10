class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        token = ""
        i = 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                while '0' <= s[i] <= '9':
                    token += s[i]
                    i += 1
                stack.append(int(token))
                token = ""
            elif 'a' <= s[i] <= 'z':
                while '0' <= s[i] <= '9':
                    token += s[i]
                    i += 1
                stack.append(int(token))
                token = ""
            elif s[i] != '[':
                token += s[i]
            if s[i] == ']':
                word = token
                while stack and isinstance(stack[-1],str):
                    word += stack.pop()
                count = stack.pop()
                combined = ""
                for _ in range(count):
                    combined += word
                stack.append(combined)
                token = ""
            i += 1
        res = ""
        while stack:
            res = stack.pop() + res
        print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"