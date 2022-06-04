# Exercise 006-03 Glossary: I will add another key-values when
# reading "Clean Code".

principles = {'kiss': 'Keep It Simple, Stupid - this principle tell you, that '
                      'you should keep you code as simple as possible. If you '
                      'can write something in on line, do it! ALos use clear '
                      'variables names, take advantage of coding libraries, '
                      'and use existing tools. It make it easy to read, and '
                      'come back to work on it after six months, saving you '
                      'ton of time and suffering. Do not reinvent the wheel!',
              'yagni': "You Ain't Gonna Need It - it means, that you should "
                       "not code for functionality on the off chance that you "
                       "may need it in the future. Don't try to solve problems "
                       "that doesn't exist.",
              'dry': "DRY stands for Don't Repeat Yourself. Avoid duplication "
                     "of data or logic. E.g. try finding the loop, than "
                     "duplicate the lines of code. It's easier to debug one "
                     "loop that handles 50 repetitions, than 50 blocks of "
                     "code, that handle one repetition each.",
              'solid': "",
              'open/closed': "Aim to make your code open for extensions, but "
                             "closed to modification. This is important if "
                             "you're realising a library of framework, that "
                             "others will use.",
              'single responsibility': "'A class should have only one reason "
                                       "to change.' Robert C. Martin. This "
                                       "principle mean, that every class or "
                                       "module should provide one specific "
                                       "functionality. This will make easier "
                                       "for debugging, and creating additional "
                                       "functionality for a specific module.",
              'document your code': "Use comments explaining objects, "
                                    "enhancing variable definitions, and make "
                                    "functions easier to understand.",
              'refactor': "Review your code to find ways to optimize it, make "
                          "it more efficient and possibly cleaner/shorter, "
                          "while keeping the same results.",
              'clean code': "",
              'separation of concerns': "",
              'composition over inheritance': "",
              }
print('KISS:\n')
print(f"\t{principles['kiss']}\n")
print('YAGNI:\n')
print(f"\t{principles['yagni']}\n")
print('DRY:\n')
print(f"\t{principles['dry']}\n")
print("\nSOLID\n")
print(f"\t{principles['single responsibility']}")
print(f"\t{principles['open/closed']}")
# to be continued...
