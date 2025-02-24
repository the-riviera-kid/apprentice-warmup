# Warmup Exercises

These are presented - very roughly - in increasing order of difficulty. For each one, make a git repository (online if you like), a virtual environment, and write tests.

1. Write a FizzBuzz function that takes a number, and returns a list of strings, each containing one "number". What's FizzBuzz? https://en.wikipedia.org/wiki/Fizz_buzz

2. Write a function that takes a string, and returns True if that string is a palindrome.

3. Write a function that takes a string, and returns True if that string is a palindrome, or if it's *nearly* a palindrome. "Nearly a palindrome" is defined as "a palindrome with extra letters as the end." Minimum length of the palindrome part is 3 characters.
```
poop -> True
crap -> False
Madam, I'm Adam -> True
tent -> False
tenet -> True
tenets -> True (extra letters at the end, so it's nearly a palindrome)
babble -> True (extra letters at the end, "bab" is a palindrome)
levelling -> True (extra letters at the end)
lotto -> False ("otto" is palindromic, but the extra letter is at the *start*, so it doesn't count.)
aardvark -> False (i suppose "aa" is a palindrome, but it's too short to count.)
```

4. Read exercise 5, but don't write the code. Write a suite of tests for it.

5. Write a function that takes as input a dictionary, and a target string. The input dictionary may be nested (i.e. contain other dictionaries). Return True if *any* dictionary in the tree contains a key matching the target string.

6. Write a program to report on how many rude words Shakespeare ever used, i.e.:
```
"fuck": 3
"shit": 9
"piss": 0
"zounds": 3
```
(I don't know what the actual numbers would be, you'll find out!)
https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

7. Write a program to print ASCII Font versions of any text you give it. i.e.:
```
> python ascii-font.py A word
  *       * * *  ***  ***   ***
 * *      * * * *   * *  *  *  *
*   *      * *  *   * *  *  *  *
*****      * *  *   * ****  *  *
*   *      * *   ***  *   * *** 
```

Be as creative as you like!

8. Write a Base64 encode/decode program

9. Write a Connect 4 game!



