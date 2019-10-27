import Output
import Logic
import Input

Output.init()
url = 'localhost:3000/lettertext.txt'

while True:
    circuit = Input.parser(url)
    res = Logic.result(circuit)
    print(res)
    Output.write(res)