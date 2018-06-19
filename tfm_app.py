import r1.mongo_setup as mongo_setup

def main():

    mongo_setup.init()
    print("Connected to db")

if __name__ == '__main__':
    main()
