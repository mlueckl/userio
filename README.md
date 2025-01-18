# ![icon-name](assets/icon.png) User IO

A simple library to handle user input and output.

<sub><sub><suv>Icon by [Three musketeers](https://www.flaticon.com/authors/three-musketeers) - Flaticon</sub></sub></sub>

### Usage

#### Output

```python
from userio import Output

output = Output("Welcome to UserIO", "This is a simple library for user input and output")

print(output.clear().headline().description("This is the output part").display())
```

```
Welcome to UserIO
This is the output part
```

#### Input

```python
from userio import Input

i = Input(description="Please enter your name")
i.clear().headline("User Info").description().prompt()
```

```
User Info
Please enter your name:
```
