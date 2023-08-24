## Summary
This is a project that takes in a file in the format
`<url><white_space><long_value>`
and returns the top x urls in descending order of the `long_value`.

For example, if this file was the input:
```
http://api.tech.com/item/121345 9
http://api.tech.com/item/122345 350
http://api.tech.com/item/123345 25
http://api.tech.com/item/124345 231
http://api.tech.com/item/125345 111
```

The output of 2 urls would be:
```
http://api.tech.com/item/122345
http://api.tech.com/item/124345
```

## Prerequisites
This project assumes you have Python3.8+ and Git locally installed on your machine.

## Execution Steps
To execute this code, follow these steps:
1. Git clone the repository: 
`git clone https://github.com/mazayan/ch-tech-problem.git`
2. Execute the file: 
`python src/main.py`
3. Enter absolute file path

## Testing
This project contains a series of unit tests for happy and sad path testing.
To execute the unit tests, run: 
`python -m unittest`

## Complexity
This program uses the built in sorted() python function. This sets the time complexity to O(nlogn) where n is the number of lines in the given file. The space complexity is O(n) where n is the number of key, value pairs generated from parsing the inputed file. 

## Edge Cases
This program takes into account a few edge cases including:
* Invalid inputs when providing the file path (path not existing & a directory path given instead of a file)
* File provided is empty
* File provided has some valid entries and some none valid entries. To account for small typos in large files, lines that do not follow the expected format will be skipped over

## Known Limitations
This program stores the file in memory by using the .open() command, which could cause an issue with very large datasets. To account for this, the underlying infrastructure used to execute this code should be able to handle the memory requirements.

## AWS Architecture
If implementing this project in AWS, a proposed architecture diagram is included in `ch_arch_diagram.png`. This architecture diagram illustrates a user publishing a file to S3, using event bridge to trigger a lambda function to execute the python code, and finally publishing the output to an SNS topic with email subscriptions. Given further requirements, this can be modified as needed.