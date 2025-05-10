# Static-Application-Security-Testing

Static Application Security Testing(SAST) tools are used to scan code to identify vulnerabilities. SAST tools apply the following techniques to identify vulnerabilities:
- Pattern Matching 
- Data Follow Analysis(Taint Analysis)
- Control Flow Analysis
- Reachability Analysis
- Software Composition Analysis(SCA)


## SAST Techniques  
### Pattern Matching
Pattern matching searches code for a set of predefined patterns associated with vulnerabilities. This search can include simple string search or more complex snytax-aware pattern matching.  

### Data Follow Analysis(Taint Analysis)  
Data Follow Analysis(Taint Analysis) is used to detect injection and insecure handling of data vulnerabilies. The flow of data(untrusted user input - tainted data) from entry point into the application(source) to where it's used(sink) is tracked to identify if the tainted data reaches a sink without proper sanitatization.  

### Control Flow Analysis  

### Reachability Analysis  

### Software Composition Analysis(SCA)  