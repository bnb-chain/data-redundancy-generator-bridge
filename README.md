# Data Redundancy Generator Bridge

This repository contains the file that produce the bridge between the [`greenfield-python-sdk`](https://github.com/bnb-chain/greenfield-python-sdk) and the greenfield data redundancy go library.

## Generate files

To be able to generate the `generated shared library`, use the following command:
- For windows:
```
go build -buildmode=c-shared -o build/main.dll src/main.go
```

- For Mac or Linux:
```
go build -buildmode=c-shared -o build/main.so src/main.go
```

The `generated shared library` will be stored in the `build` folder. You will have to move the file to the `greenfield_python_sdk/go_library` folder from the `greenfield-python-sdk`.

## Test the function

To test the function, you can choose one of these different commands to compile the test function:

```
python3 tests/test_main.py
```

or
```
python3 -m unittest tests/test_main.py
```

or
```
python -m unittest discover
```