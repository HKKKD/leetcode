def plusOne(digits):
   digits[-1] += 1
   i = len(digits)-1
   while i >= 0:
       if digits[i] >= 10:
           if i-1 >= 0:
               digits[i-1] += 1
               digits[i] = 0
           else:
               digits[i] = 1
               digits.append(0)
       i -= 1
   return digits
print plusOne([1,2,3,9,9])