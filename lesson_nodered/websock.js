[{"id":"8a35e954.75ca18","type":"websocket-client","path":"wss://echo.websocket.org","wholemsg":"false"},{"id":"b9daffe8.4625","type":"inject","name":"","topic":"","payload":"Hello There","payloadType":"string","repeat":"","crontab":"","once":false,"x":110.09942626953125,"y":41.090911865234375,"z":"bf38135c.40c7f","wires":[["13873077.ec78d"]]},{"id":"13873077.ec78d","type":"websocket out","name":"","server":"","client":"8a35e954.75ca18","x":333.0994110107422,"y":71.09091186523438,"z":"bf38135c.40c7f","wires":[]},{"id":"5f130abd.a0ecf4","type":"websocket in","name":"","server":"","client":"8a35e954.75ca18","x":146.5,"y":120.09091186523438,"z":"bf38135c.40c7f","wires":[["1189d2dc.ee762d"]]},{"id":"1189d2dc.ee762d","type":"debug","name":"","active":true,"console":"false","complete":"false","x":363.0994110107422,"y":156.09091186523438,"z":"bf38135c.40c7f","wires":[]}]

