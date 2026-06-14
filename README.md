# Enterprise Random Password Generator 🔐

## Overview
This project is a secure, backend password generation tool built in Python. Developed as part of the DecodeLabs Industrial Training (Project 3), it moves beyond basic scripting to implement enterprise-level security protocols. The generator aligns with NIST 2024 password guidelines by prioritizing cryptographic unpredictability, optimal memory management, and mathematical strength validation.

## Key Features

* **Cryptographically Secure Randomness:** Utilizes Python's `secrets` module to tap into hardware-level OS noise, bypassing the deterministic vulnerabilities of the standard `random` (Mersenne Twister) module.
* **Linear Time Complexity $O(N)$:** Implements the `"".join()` accumulator pattern for highly efficient string manipulation, preventing the $O(N^2)$ memory overhead caused by standard string concatenation in loops.
* **Information Entropy Validation:** Mathematically proves the resistance of the generated password to modern cracking techniques by calculating its entropy in bits using the formula $E = L \times \log_2(R)$.
* **NIST 2024 Compliant:** Built to enforce length over forced complexity, while still guaranteeing the inclusion of necessary character types (letters, digits, punctuation).

## Architecture
This tool follows a strict Input-Process-Output scaffold:
1. **Input:** Captures and validates the target integer for password length.
2. **Process:** A transformation engine pools character sets using the standard `string` module and selects them securely.
3. **Output:** Delivers the randomized string alongside its calculated entropy score.

## Getting Started

### Prerequisites
* Python 3.6 or higher (required for the `secrets` module).

### Installation & Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/mohitkumarjha1257-pixel/Task-3-MohitKumarJha.git](https://github.com/mohitkumarjha1257-pixel/Task-3-MohitKumarJha.git)
