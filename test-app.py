import random

import witnesschain

t = witnesschain.TransactionTracer ({
	"role"		: "app",
	"keyType"	: "ethereum",
	"privateKey"	: "ed9f0b916c7017e4d51edac23c79f5c3cc08107993cce093761e8c52f67e861f"
})

t.login()

for i in range(0,1000):
#
	transactionHash = "0x"

	for x in range (0,65):
		d = random.randint(0,16) 
		transactionHash += "01234567890abcdef"[d]

	if t.session == None:
		break

	print("\nTracing ... [",i,"]",transactionHash)

	r = t.trace ({
		"requestId"		: "EEEE",
		"chainId"		: "84532",
		"transactionHash"	: transactionHash,
	})
#
