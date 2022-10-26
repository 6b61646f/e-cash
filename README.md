I've developed a new e-cash system. The idea is to help our current system to be more efficient and fair, i will first describe some of the features that i focused on to achieve this system.
- You just need a simple mobile phone
- Anyone can use it anywhere without any discrimination, whether you are poor, rich, latin, asian, african, it doesn't matter.
- A system that is as close as possible to the current cash system.
- Stop giving money to banks to lend it to others and make money at our expense. (I can understand that this helps the economic but still cause world crises).
- Make everything transparent and easily accessible to everyone who uses it.
- And for me the most important thing, that it is easy to use and to understand how it works.

Having explained the characteristics on which I have based, I want to emphasize that this is not an idea that pretends to disparage other cryptocurrencies or to create a decentralized system, as I believe that we can take advantage of the little faith we have in our governments to give us the security in our money instead of giving it to people we don't know. Because to be honest our system is not that bad it just needs to be upgraded and to do it right, by example stop forcing us to have a bank account or to prove absolutely everything we pay.

Let's see how it works, it is quite simple since it is already used in a similar way in a lots of applications, and it's thanks to digital signatures. You can watch this video that explains it quite well for those who don't know what digital signatures are: 
https://www.youtube.com/watch?v=_zyKvPvh808

Basically a central entity in which we trust, for example a central bank, will create the receipts that are documents that represent money, to give them legitimacy and that they cannot be falsified, these will be signed with the private key of the central bank, once this digital document is created it can be distributed by the people, this central bank will have public servers where everyone can see and download the receipts that are published, these receipts are updated each time they change ownership. 
To change the owner, you need to create a document called transfer ownership, which is similar to the receipt, only two things change, the first is that instead of putting owner, it puts the person who sends it and the person who receives it, and the second is that the person who sends it signs it instead of the central bank.

Let's make an example to understand it:
- Receipt: id, value, owner, time stamp and signature (server private key)
- Transfer ownership: id, value, from, to, time stamp and signature (sender private key)
Alice send to Bob
1. Alice ask for a public key to Bob
2. Bob send to Alice a new public key that correspond him
3. Alice send a solicitation transfer ownership to the server and signed
4. The server verify the signature and proceed to change the ownership of the document and signed
5. Alice send to Bob the id of the document
6. Bob go to the server to check is the new owner of that document and download localy the proof

If the server act malicious then Bob can proof that he was the owner thanks to the fact that it has the proof localy and is signed by the server, for the server to prevent Bob reclaiming when he already send a transaction the server show the proof of the solicitation signed by Bob.

Alice and Bob talk with each other in any app like session,signal,briar,etc

To prevent censorship from the server each owner is being identify by a unique public key, a new one is generated for each receipt and they are not reused making it hard to trace, also the transaction is sent via relay nodes, so the server doesn't know where the transaction came from.
There is no double spending because the server updates the new owner and the previous one will not be able to do anything even if he has a receipt that says that he is the owner.
This system is quite fast since receipts and ownership solicitations weigh very little and creating new keys as well as signing with a simple mobile can be done very quickly.

The system uses the Ed25519 curve, which is already quite safe, although at any time the system could be updated to the Ed448 curve.
In addition, the system uses the blake2b hash protocol to encrypt the transfer ownership before signing it and then signing the hash, this makes it even more secure.

https://www.docusign.com/sites/default/files/ds_subpage_diagram2.svg

To make this work worldwide without the need for an internet connection, we can use technologies such as Bluetooth Mesh (similar to Bridgefy), LoRa Mesh Network (MeshCom, Meshtastic) and even satellites.

And I want to end this by saying that I am open to any questions or improvements that you may find to this system, I also want to share some basic scripts that I created in order to understand a little better how it works, forgive my programming since it is the first one that I do and simply I dedicated myself to copying and pasting from different pages that I found and I would also like to apologize for my English as it is not my main language.
