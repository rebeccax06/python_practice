print("Welcome to my palindrome program!")
class Palindrome:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        newNum = 0
        og_int = x
        if x ==0:
            return True
        while x >0:
         newNum = newNum * 10 + x%10
         x //= 10
       
        return newNum == og_int

number = int(input("Enter a number to determine if it's a palindrome: "))
print(Palindrome().isPalindrome(number))
while True:
    continue_program = input("Do you want to continue? (yes/no): ").lower()
    if continue_program.startswith("y"):
        number = int(input("Enter a number to determine if it's a palindrome: "))
        print(Palindrome().isPalindrome(number))
    else:
        break