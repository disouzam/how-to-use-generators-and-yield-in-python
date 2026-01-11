def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            print(f"{num} is a palindromic number")
            i = (yield num)
            
            if i is not None:
                print(f"This is the value send method sent: {i}. num is {num} but it will become {i}")
                num = i
            else:
                print(f"Next calls send no value and them i values: {i} and num stays at: {num}")
        num += 1


pal_gen = infinite_palindromes()
for i in pal_gen:
    print(f"Next was just called and returned: {i}")
    digits = len(str(i))
    print(f"Send method will be called with value: {10 ** (digits)}")
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))
