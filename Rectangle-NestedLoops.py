def main():
    print_rectangle(3, 5)

def print_rectangle(height, width):

    # for each row in square
    for i in range(height):

        # for each brick in row
        for j in range(width):
            
            # print brick
            print("# ", end="")
        
        # jumps to next row
        print()    


main()
