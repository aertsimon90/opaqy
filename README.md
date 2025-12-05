# OPAQY: Advanced Polymorphic Python Obfuscator

**OPAQY** is an advanced Python script obfuscation tool designed to protect your intellectual property (IP) and research against static analysis, reverse engineering, and automated deobfuscation. It leverages a multi-layered, polymorphic encryption scheme using the custom **LeCatchu v9 (LehnCATH4)** cryptographic engine.

> **Disclaimer:** This tool is intended *strictly* for legitimate uses: protecting your own intellectual property, educational purposes, security research, and authorized red team/penetration testing exercises. **Any malicious use is strictly prohibited and is the sole responsibility of the user.**

## 🌟 Key Features

  * **Multi-Layered Encryption:** Implements "indent" layers for recursive encryption, significantly increasing resistance to linear deobfuscation.
  * **Polymorphic Decoys:** Generates multiple fake encrypted code blobs that confuse analysts and automated tools, as only one is the true payload.
  * **Custom Cryptography:** Powered by the **LeCatchu v9 (LehnCATH4)** engine, a custom high-entropy stream cipher built on the **BLAKE2b** hash function.
  * **Dynamic S-Box Generation:** The core cryptographic substitution box (S-Box) is dynamically generated and shuffled on every run, ensuring a unique cipher mapping each time.
  * **Integrity Verification:** Uses a built-in **TAC (Tag Authentication Code)** mechanism for simple integrity checking of the encrypted data.
  * **Pure Python Output:** The resulting obfuscated file is 100% pure Python, requiring no external dependencies or compiled binaries to run.

## 🚀 Installation

OPAQY is a standalone Python script. No special installation is required beyond a standard Python 3 environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/aertsimon90/OPAQY
    cd OPAQY
    ```
2.  **Ensure Python 3 is installed:**
    ```bash
    python --version
    # Expected output: Python 3.x.x
    ```

## 🛠️ Usage

OPAQY can be run in two modes: **Command Line** (for batch/scripting) or **Interactive Menu** (for quick use).

### 1\. Command Line Mode (Recommended)

Use command-line arguments to specify input, output, and all obfuscation parameters.

```bash
python opaqy.py <input_file> <output_file> [options]
```

#### Example

This example uses recommended settings: 12 decoy copies, 1 depth layer, a 128-digit key, and only the final Base64 wrapper.

```bash
python opaqy.py my_script.py obfuscated_script.py -c 32 -d 1 -k 128 --no-per-b64 --final-b64
```

| Argument | Description | Default | Recommended |
| :--- | :--- | :--- | :--- |
| `-c`, `--count` | Number of fake/decoy code chunks. | 4 | 8 - 64 |
| `-d`, `--depth` | Obfuscation depth/layers (recursive encryption). | 1 | 1 - 2 (Avoid \> 2) |
| `-k`, `--keylength` | Cryptographic key digit length. | 64 | 64 - 256 |
| `--per-b64` | Enable Base64 wrapping on intermediate layers. | True | **False** |
| `--no-per-b64` | Disable Base64 on intermediate layers. | - | - |
| `--final-b64` | Enable final Base64 wrapper. | True | **True** |
| `-q`, `--quiet` | Suppress detailed output. | False | - |

-----

### 2\. Interactive Menu Mode

Run the script without arguments to start the interactive console menu.

```bash
python opaqy.py
```

Follow the on-screen prompts to select options and input file paths.

## ⚠️ Performance and Size Warning

Please be mindful of the settings, as they have a significant impact on the output file size and runtime performance:

  * **Depth (Layers):** Depth greater than 1 will **significantly slow down execution startup time**, as each layer requires full decryption at runtime.
  * **Size Growth:** Every additional layer causes **exponential size growth**. For example, 1-2 layers can turn a 1 KB script into 500 KB to 3 MB+.

## The LeCatchu v9 Engine

OPAQY relies on the custom, in-house developed **LeCatchu v9** cryptographic engine (also known as **LehnCATH4**).

LeCatchu v9 is a proprietary, non-standard stream cipher utilizing **BLAKE2b** as its core hash function to generate high-entropy, unpredictable key streams.

  * **Custom Key Scheduling:** Keys are processed using iterative BLAKE2b hashing (`process_hash` and `hash_stream`).
  * **Substitution:** The custom `encode`/`decode` functions implement a substitution cipher where the S-Box (`self.sbox`) is unique per run.
  * **Integrity:** The `add_tactag` and `check_tactag` methods provide a simple integrity check using a Tag Authentication Code (TAC).

For more details on the LeCatchu engine, please refer to its dedicated repository:

  * **LeCatchu Repository:** [https://github.com/aertsimon90/LeCatchu](https://github.com/aertsimon90/LeCatchu)

-----

## 👨‍💻 Developer

  * **OPAQY Developer:** Simon Scap
  * **Cryptographic Engine:** LeCatchu v9 - LehnCATH4 (2025)
