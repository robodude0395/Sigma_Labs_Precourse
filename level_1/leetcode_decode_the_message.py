#This is the most optimal solution with O(n) time complexity where n is
#the character count in message.

#Link to leetcode solution:
#https://leetcode.com/problems/decode-the-message/solutions/7232292/my-solution-by-omar_maaouane_veiga_0395-q9dx
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitution_table = {" ":" "}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0
        
        #Build substitution table
        for letter in key:
            if letter not in substitution_table:
                substitution_table[letter] = alphabet[index]
                index += 1

        decoded_message = ""

        for letter in message:
            decoded_message += substitution_table[letter]

        return decoded_message

solver = Solution()

#This code shows the first two test cases for the leetcode problem
print(solver.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv") == "this is a secret")
print(solver.decodeMessage("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb") == "the five boxing wizards jump quickly")