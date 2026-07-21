import sys

sys.path.insert(0, str(__file__).rsplit("\\", 1)[0] if "\\" in __file__ else str(__file__).rsplit("/", 1)[0])

from portfolio_app.app import main

if __name__ == "__main__":
    main()
