## Advance-Python

### Introduction

Actually `Python` is both interpreted and compiled language. The question is how `Python` run the code.

- 1. So, at first we write a `Python` code stored in a file with `.py` extension. Then a compiler compiled the source code into special `byte code` at that time the compiler also checks the `Python` syntax.

- 2. The `Python` compiler compiled the code behind the scene so we don't have to compile it manually.

- 3. The `byte code` is not understand by `cpu`.

- 4. Now, there is an `Interpreter` which is also called `Python Virtual Environment(PVM)` which takes that byte code and read the byte code line by line (one line at a time) and convert that byte code into `Machine Code`.

- 5. Here we use byte code for portability.So every computer should have virtual machine (PVM) to interpreted that byte code.

- 6. The python code we write is actually CPython.

- 7. All language have one compiling phase. So, no language is only interpreted that language is also compiled.
