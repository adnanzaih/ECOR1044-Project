from Cimpl import choose_file, load_image, copy, create_color, set_color, \
    show, Image, get_color


def red_channel(image: Image) -> Image:
    """Return a red filtered copy of image; that is, an image that is showing only the red color of the original image.

    >>> image = load_image(choose_file())
    >>> inverted = invert(image)
    >>> show(inverted)
    """
    new_image = copy(image)
    # filter the intensities of every component in every pixel.
    for x, y, (r, g, b) in image:
        red = create_color(r,0,0)
        set_color(new_image, x, y, red)
    return new_image


if __name__ == "__main__":
    image = load_image(choose_file())
    new_image = red_channel(image)
    show(new_image)