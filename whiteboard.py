'''
Print out all of the strings in the following array that represent a number divisible by 3:
[
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]
The expected output for the above input is:

nine hundred ninety nine
twelve
eighteen
six
twelve

'''
# if num is divisible by three. return the num 
#if i wanted to i could store the return True values in a list
# just going to be looping through the list
# doing mathematical problems not with integers but with strings.
# looking up list data. looking up strings and accomadating math to them.
nums = [
  "five",
  "twenty six",
  "nine hundred ninety nine",
  "twelve",
  "eighteen",
  "one hundred one",
  "fifty two",
  "forty one",
  "seventy seven",
  "six",
  "twelve",
  "four",
  "sixteen"
]
# print(nums)
# textnum = ['']
for i in nums:
    print(i)
#     textnum.append(i)
# print(textnum)

textnum = nums 
print(textnum)
# for i in nums:
# # for i in range(10):
#     if i % 3 == 0:
#         print(i)
#     else:
#         pass
#     # print(i)
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    # for word in textnum:
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

# print(text2int("seven billion one hundred million thirty one thousand three hundred thirty seven"))
# print(text2int("twenty six"))
print(text2int("one hundred twenty six"))
# keeps erroring when you pass in a list instead of typing them out directly as an arg.
# print(text2int(textnum, numwords={}))
#7100031337
