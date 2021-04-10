# Calculate XOR from 1 to n
# Efficient method
def computeXOR(n) :
    rem = n % 4
    if rem == 0 :
        return n
    if rem == 1 :
        return 1
    if rem == 2 :
        return n + 1
    return 0

def solution(start, length):
    if (length== 0):
        return 0
    if (length == 1):
        return start
    # Get first two lines
    result = computeXOR(start + 2*(length-1))
    # Remove XOR of previus lines if doens't start at 1
    # Needed since we are using a more efficient method for XOR
    if start > 1:
        result = result ^ computeXOR(start - 1)
    # -2 Since we covered the first 2 rows
    for i in range(length-2):
        nrElems = length - 2 - i
        init = start + length*(2 + i) - 1
        #Xor the previus result with the end of the row and removing the in between with (computeXor(init))
        result = result ^ computeXOR(init + nrElems) ^ computeXOR(init)
    return result


print(solution(0,3))
print(solution(17,4))
