# Write a function produce a Star triangle
def star_triangle(r: int):
    """ 
    pass any integer to the function to generate a triangle of stars
    for eg: star_triangle(3) 
        *
       *  *
     *   *  *
    """
    for index in range(1, r):
        print(" " * (r-index), "* " * index, " " * (r-index))


star_triangle(7)          # pass any integer
print(f'\n{"=" * 10}\n')
