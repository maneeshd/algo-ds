"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@date: 24/6/17

Stack
"""
_STACK_SIZE_LIMIT = 50


class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []

    def __str__(self):
        if self.is_empty():
            return str([])
        i = len(self.stack) - 1
        ret_str = ""
        while i > -1:
            ret_str += "\t{}\n".format(self.stack[i])
            i -= 1
        return ret_str

    def is_empty(self):
        if self.top < 0 or len(self.stack) == 0:
            return True
        return False

    def is_full(self):
        if self.top >= _STACK_SIZE_LIMIT or len(self.stack) >= _STACK_SIZE_LIMIT:
            return True
        return False

    @staticmethod
    def type_checker(data: str):
        try:
            if data.isdigit():
                return int(data)
            elif data.lower() == "true":
                return True
            elif data.lower() == "false":
                return False
            elif data.lower() in ["none", "null", "nan"]:
                return None
            elif data.replace(".", "").isdigit():
                return float(data)
            else:
                return data
        except:
            return data

    def push(self, item):
        if self.is_full():
            print("!!! Stack Overflow !!!\n")
            return
        self.stack.append(Stack.type_checker(item))
        self.top += 1
        print(item, "pushed into stack...")

    def pop(self):
        if self.is_empty():
            print("!!! Stack Underflow !!!\n")
            return
        data = self.stack[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.is_empty():
            print("!!! Stack Underflow !!!")
            return
        return self.stack[self.top]


if __name__ == '__main__':
    print("Stack Operations")
    print("-" * len("Stack Operations"))
    my_stack = Stack()

    while True:
        try:

            print("[1] Push\n"
                  "[2] Pop\n"
                  "[3] Peek\n"
                  "[4] Display\n"
                  "[5] Exit\n")

            choice = input("Enter your choice: ")

            if choice == "1":
                dat = input("Enter the item to push: ")
                my_stack.push(dat)
                print()

            elif choice == "2":
                dat = my_stack.pop()
                if dat:
                    print("Popped item:", dat, "\n")
                else:
                    print()

            elif choice == "3":
                peek_item = my_stack.peek()
                if peek_item:
                    print("Top most item in stack:", peek_item, "\n")
                else:
                    print()

            elif choice == "4":
                print("Stack:")
                print(my_stack, "\n")

            elif choice == "5":
                print("Exiting...\nThank You..\n")
                exit(0)

            else:
                print("!!! Enter a valid choice !!!\n")

        except ValueError:
            print("!!! Enter a valid choice !!!\n")
        except TypeError:
            print("!!! Enter a valid choice !!!\n")
        except KeyboardInterrupt:
            print("Got Ctrl+C...\nExiting...\n")
            exit(1)
        except Exception as exp:
            print(exp, "\n")
