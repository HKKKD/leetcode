def rangeBitwiseAnd(m,n):
    shift = 0
    #find the common left header (or, same prefix) of m and n
    while m != n:
        m >>= 1 #shift to right by 1 bit
        n >>= 1
        shift += 1
    #then shift back to left to form the final result
    #(the remaining bits are not the same, so definitely result in 0 after AND)
    return m << shift

print rangeBitwiseAnd(5,7)