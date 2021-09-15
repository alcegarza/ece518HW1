# ece518HW1

# ECE 443/518 Fall 2021 - Project 1
# Cryptographic Hash Functions and Ciphers

Report Due: 10/10 (Sun.), by the end of the day (Chicago time)
Late submissions will NOT be graded
# I. Objective
In this project, you will explore APIs to cryptographic hash functions and ciphers from your favorite programming languages. For your convenience, a Java program is provided as the starting point if you prefer to work with Java. For other languages including but not limited to C, C++, Python, and Matlab, please use a search engine to find tutorials on how to use their cryptographic APIs. Please use a cryptographic library and don't implement those hash functions and ciphers by yourself.

# II. Cryptographic Hash Functions
For cryptographic hash functions, we experiment with SHA-256 and SHA-512. Two tasks need to be completed for each of SHA-256 and SHA-512.

Validation: Compute the hash of the string "Hello world!" (12 bytes, ignore trailing '\0' in C and C++). Print at least the first 4 bytes and the last 4 bytes in hexadecimal format. Make sure it matches with 'C0535E4B...1AD9E51A' for SHA-256 and 'F6CDE2A0...85FFB5B6' for SHA-512.
Performance evaluation: Create a message of 256M (256*1024*1024) bytes that are all 0's. Time the process to compute its hash. Calculate the performance in MB/s. You may need to run the experiment for multiple times in order to calculate the average performance.
# III. Ciphers
For ciphers, we will experiment with AES in GCM mode without padding. The AES key size is 128 bits. The GCM mode uses an IV of 96 bits and generates a MAC of 128 bits.

Validation: Setup key and IV. Encrypt the string "Hello world!" into the ciphertext and the MAC. Decrypt the ciphertext while verifying the MAC. Make sure you get "Hello world!" back. (This step is already provided in the Java program but if you use a different language then you will need to complete it.)
Attack: Modify the code used for validation to change either the ciphertext or the MAC before sending them for decryption. Show how to use the cipher API to detect such attack.
Performance evaluation: Create a message of 64M (64*1024*1024) bytes that are all 0's. Time the process to encrypt and time the process to decrypt. Calculate the performance in MB/s for encryption and decryption separately. You may need to run the experiment for multiple times in order to calculate the average performance.
For a 20% bonus, please experiment with AES in CBC mode with padding. The AES key size is 128 bits. The CBC mode should use an IV of 128 bits. Repeat validation and performance evaluation.

# IV. Deliverables
Submit the following to Blackboard for this project.

Your source code. If third party libraries are used, please write instructions on how to install them.
A project report, which should include a summary of your experimental setup and a discussion of your findings. In particular, please address the items below (you may need to perform additional research online).
Details of the processor and the OS (if you use a VM, both the host OS and the VM OS).
How can you be sure that you are using those APIs in correct ways?
Do the performance measurements meet your expectations? In case of AES with GCM, is it accelerated by hardware, e.g. via AES-NI and other special instructions?
The project should be done individually. You can discuss the project with other students but all the source code and writings should be your OWN. PLAGIARISM and called for DISCIPLINARY ACTION. NEVER share your source code and reports with others.

# V. The Java Program
For Java development, you need to first install JDK 8 and Gradle. Popular IDEs include VS Code, Eclipse, and IntelliJ IDEA.

Download the Java program here. Unzip the file and you'll find a Java project in the standard directory layout with the Gradle project file 'build.gradle' and the Java source file in 'src/main/java'. For the command line, you may use 'gradle eclipse' to generate project files for Eclipse and use 'gradle idea' to generate project files for IntelliJ IDEA.

You can either run the Java program from with the IDE or via 'gradle run'. Moreover, you may directly download the Java program onto our VM and run it from there.

First, use 'wget' to download the zip file and 'unzip' to extract it.

ubuntu@ece443:~$ wget http://www.ece.iit.edu/~jwang/ece443-2021f/prj01-src.zip
--2019-09-09 13:10:26--  http://www.ece.iit.edu/~jwang/ece443-2021f/prj01-src.zip
......
2018-09-11 13:10:26 (479 MB/s) - 'prj01-src.zip' saved [4572/4572]

ubuntu@ece443:~$ unzip prj01-src.zip
Archive:  prj01-src.zip
   creating: prj01-src/
......
   creating: prj01-src/src/tests-unit/
Then, use 'cd' to change into 'prj01-src' and 'ls' to check the files.

ubuntu@ece443:~$ ls
prj01-src  prj01-src.zip
ubuntu@ece443:~$ cd prj01-src/
ubuntu@ece443:~/prj01-src$ ls
build.gradle  src
Finally, run the program with 'gradle run'. It will take some time for the first time as Gradle downloads other Java packages from online.

ubuntu@ece443:~/prj01-src$ gradle run
Download https://plugins.gradle.org/m2/com/github/jengelman/gradle/plugins/shadow/1.2.3/shadow-1.2.3.pom
......
:run
MD5 of [Hello world!]
Computed: 86FB269D190D2C85F6E0468CECA42A20
Expected: 86FB269D190D2C85F6E0468CECA42A20

MD5 of 256MB 0x00
Computed: 1F5039E50BD66B290C56684D8550C6C2
Time used: 578 ms
Performance: 442.91 MB/s

AES/GCM of [Hello world!]
Plaintext:  48656C6C6F20776F726C6421
Ciphertext: BB513E1F49B57446EA599AD2
MAC:        63B7C2C15D8D5AFEBBD9E6D42F7EF717
Decrypted:  48656C6C6F20776F726C6421

AES/GCM of 64MB 0x00
Plaintext:  7F614DA9329CD3AEBF59B91AADC30BF0[MD5]
MAC:        7CCC42CA2C2B7A415938CFBA603292FD
Decrypted:  7F614DA9329CD3AEBF59B91AADC30BF0[MD5]
Time used: encryption 874 ms, decryption 999 ms
Performance: encryption 73.23 MB/s, decryption 64.06 MB/s

BUILD SUCCESSFUL
......
