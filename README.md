# keylogger
🔐 Description: Local Keystroke Logger (Authorized)
This keylogger is a Python-based monitoring tool designed to capture and log keystrokes from the local keyboard input on a target system. It utilizes the pynput library to hook into keyboard events and record user input in real time. The tool is configured to:

Capture alphanumeric input and interpret special keys (e.g., Space, Enter, Backspace).
Combine individual keystrokes into coherent words to improve readability and reduce log fragmentation.
Handle line breaks and spacing accurately by detecting Enter and Space for natural text formatting.
Log data locally to a plain-text file (log.txt) in an append mode, preserving historical input across sessions.
Support clean logging: No raw object output; special keys are handled intelligently (e.g., backspace deletes the last character, enter creates a new line).
🛡️ This tool was deployed only on systems for which written authorization was granted, as part of a controlled penetration test to assess endpoint security, detect logging vulnerabilities, or evaluate response to local reconnaissance tools.

It does not:

Transmit data over the network
Hook screenshots or clipboard content (unless explicitly added)
Use rootkits or stealth techniques (unless extended for red team operations)
This serves as a proof-of-concept for local input capture and highlights the risk posed by unattended or improperly hardened systems where physical or remote code execution access is achieved.

📝 Purpose in Pentest:

Validate detection capabilities of EDR/XDR solutions
Assess risk of credential or command capture post-exploitation
Simulate post-breaching behavior of real-world malware
Logs generated are handled under strict confidentiality and securely deleted after analysis.


