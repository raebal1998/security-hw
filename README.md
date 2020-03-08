# Security
In this assignment code you can find the way to implement tow cryptosystems (RSA,Keyword columnar) Using python languages so you will be able to enc/decrypt your messages. 
we worked as a team with @AlherbishLama and @HaneenKhaled1

##  RSA
Asymmetric encryption algorithm so there is private and public key .
we implemented tis algorithm by following these steps:-
- ask the user to enter tow prime numbers and validate that the input is prime and int.
- compute n and phi 
- compute the list that contain all possiple e and ask the user to choose from it
- compute the d
- now we are be able to generate the private and the public key the public key is a pair from (e,n)while the private key is a pair of numbers(d,n)
- the user can choose either encrypt or decrypt and passing the plain text to encrypt or decrypt messages 
-  encrypt or decrypt methods will convert the letters into numbers and also will encrypt/decrypt. 
## Keyword columnar
The key for the columnar transposition cipher is a keyword e.g. GERMAN. The row length that is used is the same as the length of the keyword.
-  the user will choose keyword we will assign numbers to each letter accoarding th the alphapatic order
- build the grid and order the letters inside it
- we will take number 1 as a start each letter in the colomn will write it next to each other then we will move to colomn num 2 and so on this is the encryption process 
- to decrypt we determined the size of the grid and basing the location of the letters . 

