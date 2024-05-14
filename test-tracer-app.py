import sys
import random

# Please refer to API documentation here:
# https://redocly.github.io/redoc/?url=https://api.witnesschain.com/static/transaction-tracer.json

import witnesschain

t = witnesschain.TransactionTracer ({
	"role"		: "app",
	"keyType"	: "ethereum",
	"privateKey"	: "ed9f0b916c7017e4d51edac23c79f5c3cc08107993cce093761e8c52f67e861f"
})

t.login()

if t.session == None:
	print("Login did not succeed")
	sys.exit(-1)	

transactionHash = "0x"

for x in range (0,65):
	d = random.randint(0,16) 
	transactionHash += "01234567890abcdef"[d]


print("\nTracing ... ",transactionHash)

r = t.trace ({
	"requestId"		: "EEEE",
	"chainId"		: "84532",
	"transactionHash"	: transactionHash,
})

print(r)
