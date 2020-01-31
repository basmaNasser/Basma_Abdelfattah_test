## Q2

### Description

 The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than 
 the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.


### The Answer

source directory: `./compare_strings`

- Run `pip3 install q2`

usage: 
```
from compare_strings.compare_strings import strings,check_input
```
### Example:
```
result = compare_strings('1.1','1.2')

o/p: string1 (1.1) less than string2 (1.2)
```
> It will return:</br>
> text message if the first number is greater than, less than or equal the second number 
