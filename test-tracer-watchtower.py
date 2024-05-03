import asyncio

import witnesschain

async def main():
#
	t = witnesschain.TransactionTracer ({
		"role"			: "watchtower",
		"keyType"		: "ethereum",
		"privateKey"		: "ed9f0b916c7017e4d51edac23c79f5c3cc08107993cce093761e8c52f67e861f",
		"currentlyWatching"	: "84532"
	})

	t.login()

	print("\n===> Running ...");
	await t.run()
	print("\n===> Done running...");
#

if __name__ == "__main__":
	asyncio.run(main())
