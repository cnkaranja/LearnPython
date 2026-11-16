name = "Ada"
age = 36
height_m = 1.68
is_learning = True
nickname = None

print(type(name), type(age), type(height_m), type(is_learning), type(nickname))

x, y = 10, 20

print(x, y)

x, y = y, x

print(x, y)

population = 8_100_000_000

print(population * 2)

MAX_RETRIES = 3

# Strings

greeting = f"Hello, {name}! Next year you'll be {age + 1}."
print(greeting)

print(name.upper(), name.lower(), len(name))  # ADA ada 3
print("  padded  ".strip())  # 'padded'
print(["a", "b", "c"])  # ['a', 'b', 'c']
print("-".join(["2026", "11", "10"]))  # 2026-11-10
print("python".replace("py", "Py"))  # Python
print("data.csv".endswith(".csv"))  # True
print(name[0], name[-1])  # A a  (indexing)
print("ha" * 3)  # hahaha

poem = """Triple quotes
let a string span
several lines."""
path = r"C:\new\folder"  # raw string: backslashes are literal
print(f"{3.14159:.2f} | {1234567:,} | {'right':>10} | {42:05d}")

# type conversion or casting

print(int("42") + 1)  # 43
print(float("3.5") * 2)  # 7.0
print(str(99) + " bottles")  # '99 bottles'
print(int(7.9), round(7.9))  # 7 8   (int() truncates toward zero)
print(int("ff", 16))  # 255   (parse hexadecimal)

# Truthiness: empty / zero values are False
print(bool(0), bool(""), bool([]), bool(None))  # False False False False
print(bool("False"), bool(-1), bool([0]))  # True True True

# int("3.5")  -> ValueError!  Convert in two steps:
print(int(float("3.5")))  # 3
