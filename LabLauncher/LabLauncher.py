import Lab0101
import Lab0102
import Lab0103
import Lab0105
import Lab0106
import Lab0107
import Lab0108
import Lab0201
import Lab0211
import Lab0212

functions = {
    "0101": Lab0101.launch,
    "0102": Lab0102.launch,
    "0103": Lab0103.launch,
    "0105": Lab0105.launch,
    "0106": Lab0106.launch,
    "0107": Lab0107.launch,
    "0108": Lab0108.launch,
    "0201": Lab0201.launch,
    "0211": Lab0211.launch,
    "0212": Lab0212.launch
}


myline = input()

if myline in functions:
    functions[myline]()
else:
    print("Invalid command")
            
