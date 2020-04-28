207demography
===

Time:       2 weeks

Team:       2

Language:   Python


The project
----
The world population growth is a cause for concern for most people: 1 billion people in 1800, 2 billion peo-ple in 1927, 6 billion people in 2000 and more than 7.5 billion people today... Predicting future population using past censuses is therefore a key concept.

Along with this subject, you will find a file named `207demography_data.csv`, which gives an estimation of every country’s population from 1960 onwards. If world population growth seems exponential in the long-term, in a shorter term it seems linear: using this data, **you must establish the linear least squares regression** that will allow you to **predict population depending on the year**.

In the following,**Y** is the population (in million people) and **X** the year. With one or several country codes as inputs, your program will print:
* The **aX** and **bX** coefficients of the linear fit ```Y = aX * X + bX```
* The root-mean-square deviation of this fit
* The population prediction in 2050 according to this fit
* The **aY** and **bY** coefficients of the linear fit ```X = aY * Y + bY ```
* The root-mean-square deviation of this fit
* The population prediction in 2050, according to this fit
* The correlation coefficient between **X** and **Y**

## USAGE:

```
>> ./207demography -h
USAGE
    ./207demography code [...]
    
DESCRIPTION
code    country code
```


Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva) and [**PATRICIA MONFA-MATAS**](https://github.com/patumm)
