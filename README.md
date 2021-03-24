# remfunc

Ever needed a python module on a system where you can only install pure python libs, for example Pythonista for IOS? This is a workaround you can use if you have a webserver (or computer reachable over the internet). You run the remfunc server part on your computer and in Pythonista you create an instance of the client and use it to send code to the server which gets executed there and the result returned. Yeah! Now you can use pandas in Pythonista!

## Installation

Just a quick "pip remfunc" on the computer that´s going to be the server and on the one the that will be the client.

## Usage

### Start the server

```python
import remfunc

rfunc = remfunc
rfunc.start_server(host,port,debug = False)  
#Set debug to True to print diagnostic stuff
#host  is a string, port an int
```

## Init the client (in Pythonista on IOS or where ever you want)
```python
import remfunc
rfunc = remfunc.client(host,port)
```
## After init of the client you can use it to send code to the server and get the results

CODE has to be a string, seperate lines using \n

```python
code = "first line of code \n"
code = code + "second line of code \n"

result = rfunc.do(code)
```
In case of a runtime error .do returns the error message

## Random suggestions
- You could do multiprocessing by creating multiple instances of the server using ProcessPoolExecutor, be sure to give each instance its own port though
