# JXC Syntax

JXC syntax is a **very flexible and powerful** syntax designed to integrate multiple languages inside one file.

---

## Language Blocks

Use these keywords at the start of a code block `{ ... }` to specify which language the block contains:

- `PythonUSE` — Use Python for all code inside the block  
- `jUseS` — Use JavaScript for all code inside the block  
- `USEjava` — Use Java for all code inside the block  
- `Cplusplus` — Use C++ for all code inside the block  

Example:

    ```jxc
    {
        PythonUSE
        # Python code here
    }
    ```

## Other Notes

- Blocks are enclosed in curly braces `{ ... }`  
- Each block’s language affects how the code is interpreted and executed  
- JXC enables multi-language interoperability in one file  

# Made with ❤️ by [Stetup](https://www.github.com/stetupdev)
