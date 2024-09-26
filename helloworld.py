class HelloWorld:
    def __init__(self, message):
        self.message = message

    def display_message(self):
        print(self.message)

def main():
    hello_world = HelloWorld("Hello, World!")
    hello_world.display_message()

if __name__ == "__main__":
    main()