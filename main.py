from time import sleep
from pybit.unified_trading import WebSocket

def handle_message(m):
	print(m)

def handle_ticker(m):
	d = m.get('data', {})
	print(d['symbol'], d['lastPrice'], sep=":")

def main():
	ws = WebSocket(
		testnet = False,
		channel_type = "spot",
	)

	ws.ticker_stream(symbol="BTCUSDT", callback=handle_ticker)



if __name__ == '__main__':
	main()
