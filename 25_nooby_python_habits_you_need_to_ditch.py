import socket
# From mCoding James Murphy on YouTube
# https://www.youtube.com/c/mCodingWithJamesMurphy


# # # 1
# Instead of manual string formatting, using plus signs, like below:
def manual_str_formatting(name, subscribers):

    if subscribers > 100_000:
        print("Wow" + name + "! you have" + str(subscribers) + " subscribers!")
    else:
        print("Lol" + name + " that's not many subscribers...")


# Use f-strings!
def fstr_formatting(name, subscribers):
    if subscribers > 100_000:
        print(f"Wow {name}! You have {subscribers} subscribers!")
    else:
        print(f"Lol {name} that's not many subscribers...")
# f-strings are more readable, easier to write and less prone to error.


# # # 2
# Manually closing a file (like below), if calling close when f.write() call
# throws an exception, the file never be closed.
def manually_calling_close_on_a_file(filename):
    f = open(filename, 'w')
    f.write("hello\n")
    f.close()


# Instead of f.close(), use 'with' statement, which will ensure the file
# is closed, even if exception is thrown:
def closing_on_a_file_with_as_statement(filename):
    with open(filename, 'w') as f:
        f.write("hello\n")


# # # 3
# Using "try-finally" instead of a context manager.
def try_finally(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.sendall(b'Hello, world')
    finally:
        s.close()


# "Try-finally" comes from a different language, in Python most resources that
# need to be close have their own context manager, that will goe as follows:
def python_context_manager(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, world')
