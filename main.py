from battle import simulate_battle

def main():
    try:
        simulate_battle()
    except KeyboardInterrupt:
        print("\nThe player interrupt the program by the keyboard!")

if __name__ == "__main__":
    main()
