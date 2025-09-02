# def countDigits(n):
#     return len(str(n))

# or mod with 10 and divide by 10
def countDigits(n):
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

result = countDigits(2234)
print(result)
