You will first have to create a public and private key for Bob with create_keys.
Second you will have to execute the send_pubkey script that will create a file called pub.key, this file is the one that you will send to Alice, the send_pubkey script will also send 
the public key as well as the private key to a file called used.key where all the public keys that you have sent will be so that in the future you can use the private key to send 
them to another
Third, in Alice you can create a solicitation transfer ownership with the receipt you already have and sign it with the create_solicitation script.
Fourth and finally, Alice will send that file to the server, and the server with the validate_server script, verifies that Alice has a receipt and if so, verify that the signature
is hers, if everything is correct create a new receipt with the new owner (Bob)