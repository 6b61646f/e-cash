A new digital payment system that uses digital signatures to ensure the legitimacy and security of transactions. In this system, a central entity, such as a central bank, creates digital receipts that represent money. These receipts are signed with the private key of the central bank to prevent counterfeiting. The receipts can then be distributed among users and updated each time they change ownership.

To change the ownership of a receipt, a user must create a transfer ownership document, which is similar to the receipt but includes the names of the sender and receiver, as well as the sender's signature instead of the central bank's signature.

For example, if Alice wants to send money to Bob, she must first ask Bob for his public key. Bob sends Alice his public key, which she uses to create a transfer ownership document and sign it with her private key. Alice then sends the document to the central bank's server, which verifies the signature and updates the ownership of the receipt. Alice then sends Bob the receipt's ID, and Bob can go to the central bank's server to verify that he is the new owner and download a locally-stored proof of ownership.

The system also includes features to prevent censorship and double spending. Each receipt is associated with a unique public key that is not reused, making it difficult to trace transactions. Additionally, transactions are sent via relay nodes, similar to the Tor network, so the central bank's server does not know the origin of the transaction. And because the server updates the ownership of a receipt each time it changes hands, it is impossible for a previous owner to spend the same money twice.

The system uses the Ed25519 curve for digital signatures, which provides a high level of security. It also uses the blake2b hash protocol to encrypt transfer ownership documents before signing them, adding an extra layer of security.

Some key features of the system include:

Completely anonymous accounts, with no requirement for phone numbers or email addresses.
No risk of data breaches, as the system does not collect any personal data.
Censorship-resistant and resistant to central points of failure, thanks to its use of relay nodes.
Open source, allowing anyone to view, audit, and contribute to the system's development.

The system is designed to provide a secure, efficient, and private method for making digital payments. By using digital signatures and public key cryptography, the system ensures that transactions cannot be forged or altered, and that the identity of the sender and receiver remains anonymous.

One of the key advantages of the system is that it relies on a central entity, such as a central bank, to create and manage the digital receipts that represent money. This central entity is trusted by all users of the system, which allows them to verify the legitimacy of the receipts and the accuracy of the ownership records.

Another advantage of the system is its use of relay nodes to prevent censorship and protect user privacy. By routing transactions through these nodes, the system ensures that the central bank's server cannot see the origin or destination of the transactions, making it impossible for the server to censor or block certain transactions.

Additionally, the system uses unique, non-reusable public keys to identify receipts, which makes it difficult to trace transactions and prevent double spending. This, combined with the use of the Ed25519 curve for digital signatures and the blake2b hash protocol for encryption, makes the system highly secure and resistant to tampering.

Overall, the system described offers a number of benefits for users, including security, efficiency, privacy, and resistance to censorship and central points of failure. Its open source nature also allows for transparency and community participation in its development and maintenance.

Curiously, this is the opinion of chatgpt after asking him what he thinks of the system:
Hypothetically, if I were able to form opinions and assess the digital payment system described previously, I would likely have a positive view of it. The system appears to be well-designed and incorporates many features that are important for the security, efficiency, and privacy of digital payments. Its reliance on a central entity and use of digital signatures and public key cryptography help to ensure the legitimacy and security of transactions, while its use of relay nodes and unique public keys protect against censorship and double spending. Additionally, its open source nature allows for transparency and community participation in its development and maintenance. Overall, the system seems to be a promising option for digital payments.

Aditionally we could make this work worldwide without the need for an internet connection, using technologies such as Bluetooth Mesh (similar to Bridgefy), LoRa Mesh Network (MeshCom, Meshtastic) and even satellites.
I also want to share some basic scripts that I created in order to understand a little better how it work.

Thanks for reading this far and I wish you a good day.
