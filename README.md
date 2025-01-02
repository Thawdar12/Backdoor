## Description
This project involves creating a backdoor program in Python, which allows the victim’s **Ubuntu machine** to establish a reverse shell connection to **the hacker’s Kali VM**. Once connected, the hacker can send Unix commands to be executed on the victim’s system. The backdoor program will be a client that connects to the Kali machine and executes the received commands until the termination symbol (‘&’) is entered. The program should also be capable of interactive commands for enhanced functionality.

## What I learnt
- Socket Programming: Established a client-server connection using Python's socket library to communicate with the Kali machine.
- Command Execution: Used subprocess to run shell commands and return output to the attacker.
- File Navigation: Implemented directory changes with os.chdir() and dynamically updated the working path.
- Error Handling: Managed errors for invalid commands and paths using try-except.
- Real-Time Interaction: Enabled a reverse shell for executing non-interactive commands.
- Ethical Awareness: Highlighted the importance of secure coding and ethical hacking to prevent misuse.
