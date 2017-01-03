from .module_y import spam as ham

def main():
    ham()

# This won't work!
if __name__ == '__main__':
    main()
