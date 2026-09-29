
## Explanation

**5. Longest Palindromic Substring**

In this problem we are given a string `s`. We are tasked to find the longest palindromic substring of `s`. To do this, we are going to be using <a href="https://www.geeksforgeeks.org/dsa/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/">Manacher's Algorithm</a>. This will allow us to solve the problem with linear time complexity, instead of using brute force or dynamic programming that will require quadratic time.

We start by preprocessing the input string by surrounding each character with `#` and also inserting `^` and `$` as start and end sentinels. 

```Python
T = "^#" + "#".join(s) + "#$"
```

After that we create a variable `n` to keep track of the length of `T` as well as an array filled with $0$ with the length of `n`. 

```Python
n = len(T)
P = [0] * n
```

Now we define two variables, `C` and `R`. `C` is representing the index of the center character of the palindrome that extends the highest index in the string. `R` represents the index that the palindrome with center at `C` reaches.

```Python
    C = 0
    R = 0 
```

Now we start out main loop. We are going to iterate through our constructed string. 

```Python
for i in range(1, n -1):
```

For each iteration we create a variable `i_mirror` that is the index symmetric to the current index `i` with respect to the center `C`.

```Python
    i_mirror = 2 * C - i
```

After that we check if whether the current index `i` lies inside the right boundary of the furthest reaching palindrome. If that is the case we set `P[i]` to the smallest value between `R - i` and `P[i_mirror]`. The entire region around `i_mirror`. The symmetry around C is guaranteed up to the distance `R - i`. That means that if `i_mirror` extends beyond `R - 1` we know nothing about the characters past `R`. So we pick the smaller of the two. 

```Python
    if R > i:
        P[i]  = min(R - i, P[i_mirror])
```

Then we extend the palindrome centered at i outward as far as possible while comparing the letters on both sides. We do this until the letters differ. 

```Python 
    while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
        P[i] += 1
```

After that we check if the rightmost index of the palindrome centered at i is larger than the rightmost boundary reached by any palindrome processed so far. If it is we update our new center to `i` as well as our new right most boundary to `i + P[i]`. 

```Python 
    if i + P[i] > R:
        C = i
        R = i + P[i]
```

Each element `P[i]` represents the radius of the longest palindrome centered at `i` in `T`. We find the largest value in P, and find its index as well. We store these in `max_len` and `center_index`.

```Python
max_len, center_index = max((val, idx) for idx, val in enumerate(P))
```

Then we find the starting index of our palindrome, by subtracting our `center_index` by our `max_len`. However, this will only find the start index in `T`. To find the start index of the palindrome in the input array we need to divide by $2$ as well. 

```Python
start = (center_index - max_len) // 2
```

After that we return the substring that we have determined is the largest palindrome by slicing the input string.

```Python
return s[start:start + max_len]
```

**Time Complexity** 

We have to iterate through each index `T` once. This gives us linear time complexity <code><i>O(n)</i></code>.

**Space Complexity**

P will have the size of len(T). This is linear <code><i>O(n)</i></code>.