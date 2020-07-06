# tex-citation-checker
A python script that finds total number of citations and counts for each citation in a Latex file (using the \cite command).

## Required Packages
[Numpy](https://numpy.org/)

## Usage
```
python3 cite_count.py your-tex-file.tex
```

## Output
Output is directly printed into the console output listing the total number of citations along with the individual counts for each unique reference. The keywords listed are those that are passed into the \cite command within your Latex document.
```
Total Citations: 12
keyword1             : 8
keyword2             : 3
keyword3             : 1
```
