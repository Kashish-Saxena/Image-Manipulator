"""Image_Manipulator.

2018, Kashish Saxena,

Image_Manipulator provides a collection of functions that can be applied to digital images.

Uses Cimpl, a library that provides a collection of functions for manipulating digital images.

"""

from Cimpl import *


def grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = (r + g + b) // 3

        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int

        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)

    return new_image


# The negative filter inverts every component of every pixel.
# The solarizing filter invert only those components that have intensities
# below a specified value.

def negative(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return an inverted copy of image; that is, an image that is a colour 
    negative of the original image.
    
    >>> image = load_image(choose_file())
    >>> filtered = negative(image)
    >>> show(filtered)
    """
    new_image = copy(image)

    # Invert the intensities of every component in every pixel.
    for x, y, (r, g, b) in image:
        inverted = create_color(255 - r, 255 - g, 255 - b)
        set_color(new_image, x, y, inverted)

    return new_image


def solarize(image, threshold):
    """ (Cimpl.Image, int) -> Cimpl.Image
    
    Return a "solarized" copy of image. RGB components that have
    intensities less than threshold are modified.
    
    Parameter threshold is in the range 0 to 256, inclusive.
    
    >>> image = load_image(choose_file()) 
    >>> filtered = solarize(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for x, y, (red, green, blue) in image:

        # Invert the intensities of all RGB components that are less than 
        # threshold.

        if red < threshold:
            red = 255 - red

        if green < threshold:
            green = 255 - green

        if blue < threshold:
            blue = 255 - blue

        col = create_color(red, green, blue)
        set_color(new_image, x, y, col)

    return new_image


def black_and_white(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a black-and-white (two-tone) copy of image.
    
    >>> image = load_image(choose_file()) 
    >>> filtered = black_and_white(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on
    # whether its brightness is in the lower or upper half of this range.

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3

        if brightness < 128:  # brightness is between 0 and 127, inclusive
            set_color(new_image, x, y, black)
        else:  # brightness is between 128 and 255, inclusive
            set_color(new_image, x, y, white)

    return new_image


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a black-and-white-and gray (three-tone) copy of image.

    >>> image = load_image(choose_file()) 
    >>> filtered = black_and_white_and_gray(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of every
    # pixel whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3

        if brightness < 85:  # brightness is between 0 and 84, inclusive
            set_color(new_image, x, y, black)
        elif brightness < 171:  # brightness is between 85 and 170, inclusive
            set_color(new_image, x, y, gray)
        else:  # brightness is between 171 and 255, inclusive
            set_color(new_image, x, y, white)

    return new_image


def weighted_grayscale(image):
    """ (Cimpl.Image) -> Cimpl.Image

    Return a grayscale copy of image.

    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        # Use the pixel's brightness as the value of RGB components for the
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.

        brightness = r * 0.299 + g * 0.587 + b * 0.114

        # create_color will convert an argument of type float to an int

        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)

    return new_image


def extreme_contrast(image):
    """ (Cimpl.Image) -> Cimpl.Image

    Return a copy of image, maximizing the contrast between
    the light and dark pixels.

    >>> image = load_image(choose_file())
    >>> new_image = extreme_contrast(image)
    >>> show(new_image)

    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        if r < 128:
            r = 0;
        else:
            r = 255;
        if g < 128:
            g = 0;
        else:
            g = 255;
        if b < 128:
            b = 0;
        else:
            b = 255;

        new_col = create_color(r, g, b)
        set_color(new_image, x, y, new_col)

    return new_image


def sepia_tint(image):
    """ (Cimpl.Image) -> Cimpl.Image

    Return a copy of image in which the colours have been
    converted to sepia tones.

    >>> image = load_image(choose_file())
    >>> new_image = sepia_tint(image)
    >>> show(new_image)
    """

    new_image = copy(weighted_grayscale(image))
    for x, y, (r, g, b) in new_image:

        if r < 63:
            b = b * 0.9
            r = r * 1.1
        elif r < 191:
            b = b * 0.85
            r = r * 1.15
        else:
            b = b * 0.93
            r = r * 1.08
        new_col = create_color(r, g, b)
        set_color(new_image, x, y, new_col)
    return new_image


def _adjust_component(amount):
    """ (int) -> int

    Divide the range 0..255 into 4 equal-size quadrants,
    and return the midpoint of the quadrant in which the
    specified amount lies.

    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """

    if amount < 64:
        value = 31
    elif amount < 128:
        value = 95
    elif amount < 192:
        value = 159
    else:
        value = 223

    return value


def posterize(image):
    """ (Cimpl.Image) -> Cimpl.Image

    Return a "posterized" copy of image.

    >>> image = load_image(choose_file())
    >>> new_image = posterize(image)
    >>> show(new_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        new_col = create_color(r, g, b)
        set_color(new_image, x, y, new_col)
    return new_image


def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image

    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):

            pixel_red, pixel_green, pixel_blue = get_color(image, x, y)
            pixelbelow_red, pixelbelow_green, pixelbelow_blue = get_color(image, x, y + 1)

            contrast_check = ((pixel_red + pixel_green + pixel_blue) // 3) - (
                    (pixelbelow_red + pixelbelow_green + pixelbelow_blue) // 3)
            if contrast_check < threshold:
                set_color(new_image, x, y, create_color(255, 255, 255))
            else:
                set_color(new_image, x, y, create_color(0, 0, 0))

    return new_image


def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> Cimpl.Image

    Return a new image that contains a copy of the original image
    that has been modified using edge detection.
    >>> image = load_image(choose_file())
    >>> filtered = detect_edges(image, 10.0)
    >>> show(filtered)

    """
    new_image = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            # top_red, top_green, top_blue = get_color(image, x, y - 1)
            # left_red, left_green, left_blue = get_color(image, x - 1, y)
            # bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            # right_red, right_green, right_blue = get_color(image, x + 1, y)
            # center_red, center_green, center_blue = get_color(image, x, y)

            pixel_red, pixel_green, pixel_blue = get_color(image, x, y)
            pixelbelow_red, pixelbelow_green, pixelbelow_blue = get_color(image, x, y + 1)
            pixelright_red, pixelright_green, pixelright_blue = get_color(image, x + 1, y)

            contrast_check_below = ((pixel_red + pixel_green + pixel_blue) // 3) - (
                    (pixelbelow_red + pixelbelow_green + pixelbelow_blue) // 3)
            contrast_check_right = ((pixel_red + pixel_green + pixel_blue) // 3) - (
                    (pixelright_red + pixelright_green + pixelright_blue) // 3)

            if contrast_check_below > threshold or contrast_check_right > threshold:
                set_color(new_image, x, y, create_color(0, 0, 0))
            else:
                set_color(new_image, x, y, create_color(255, 255, 255))

    return new_image


def blur_better(image):
    """ (Cimpl.Image) -> Cimpl.Image

    Return a new image that is a blurred copy of image.

    >>> original = load_image(choose_file())
    >>> blurred = blur_better(original)
    >>> show(blurred)
    """
    target = copy(image)

    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(image, x, y - 1)
            left_red, left_green, left_blue = get_color(image, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(image, x, y + 1)
            right_red, right_green, right_blue = get_color(image, x + 1, y)
            center_red, center_green, center_blue = get_color(image, x, y)
            diagonaltopright_red, diagonaltopright_green, diagonaltopright_blue = get_color(image, x + 1, y - 1)
            diagonaltopleft_red, diagonaltopleft_green, diagonaltopleft_blue = get_color(image, x - 1, y - 1)
            diagonalbottomright_red, diagonalbottomright_green, diagonalbottomright_blue = get_color(image, x + 1,
                                                                                                     y + 1)
            diagonalbottomleft_red, diagonalbottomleft_green, diagonalbottomleft_blue = get_color(image, x - 1, y + 1)

            # Average the red components of the nine pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + diagonaltopright_red + diagonaltopleft_red + diagonalbottomright_red + diagonalbottomleft_red) // 9

            # Average the green components of the nine pixels
            new_green = (top_green + left_green + bottom_green +
                         right_green + center_green + diagonaltopright_green + diagonaltopleft_green + diagonalbottomright_green + diagonalbottomleft_green) // 9

            # Average the blue components of the nine pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                        right_blue + center_blue + diagonaltopright_blue + diagonaltopleft_blue + diagonalbottomright_blue + diagonalbottomleft_blue) // 9

            new_color = create_color(new_red, new_green, new_blue)

            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target


def flip_vertical(image):
    """ (Cimpl.Image) -> Cimpl.Image
    Return an image that contains a copy of the original image
    after it has been flipped around an imaginary vertical line
    drawn through its midpoint.

    >>> image = load_image(choose_file())
    >>> filtered = flip_vertical(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            col = get_color(image, x, y)
            set_color(new_image, (get_width(image) - (x + 1)), y, col)
    return new_image


def flip_horizontal(image):
    """ (Cimpl.Image) -> Cimpl.Image
    Return an image that contains a copy of the original image
    after it has been flipped around an imaginary vertical line
    drawn through its midpoint.

    >>> image = load_image(choose_file())
    >>> filtered = flip_vertical(image)
    >>> show(filtered)
    """
    new_image = copy(image)
    for y in range(1, get_height(image) - 1):
        for x in range(1, get_width(image) - 1):
            col = get_color(image, x, y)
            set_color(new_image, x, get_height(image) - (y + 1), col)
    return new_image


# -------------------------------------
# A few functions to test the filters.

def test_grayscale(image):
    """ (image)
        tests the called function
        gray_image = test (image)

        """
    gray_image = grayscale(image)
    show(gray_image)


def test_negative(image):
    """ (image)
        tests the called function
        inverted_image = test (image)

        """
    inverted_image = negative(image)
    show(inverted_image)


def test_solarize(image):
    """ (image)
        tests the called function
        solarized_image = test (image)

        """
    solarized_image = solarize(image, 128)
    show(solarized_image)


def test_black_and_white(image):
    """ (image)
        tests the called function
        b_w_image = test (image)

        """
    b_w_image = black_and_white(image)
    show(b_w_image)


def test_black_and_white_and_gray(image):
    """ (image)
        tests the called function
        b_w_g_image = test (image)

        """
    b_w_g_image = black_and_white_and_gray(image)
    show(b_w_g_image)


def test_weighted_grayscale(image):
    """ (image)
        tests the called function
        gray_image = test (image)

        """
    gray_image = weighted_grayscale(image)
    show(gray_image)


def test_sepia_tint(image):
    """ (image)
        tests the called function
        sepia_image = test (image)

        """
    sepia_image = sepia_tint(image)
    show(sepia_image)


def test_extreme_contrast(image):
    """ (image)
        tests the called function
        contrast_image = test (image)

        """
    contrast_image = extreme_contrast(image)
    show(contrast_image)


def test_detect_edges(image):
    """ (image)
        tests the called function
        edge_image = test (image)

        """
    edge_image = detect_edges(image, 50)
    show(edge_image)


def test_detect_edges_better(image):
    """ (image)
        tests the called function
        edge_image = test (image)

        """
    edge_image = detect_edges_better(image, 50)
    show(edge_image)


def test_blur_better(image):
    """ (image)
        tests the called function
        blur_image = test (image)

        """
    blur_image = blur_better(image)
    show(blur_image)


def test_flip_vertical(image):
    """ (image)
        tests the called function
        fv_image = test (image)

        """
    fv_image = flip_vertical(image)
    show(fv_image)


def test_flip_horizontal(image):
    """ (image)
        tests the called function
        fh_image = test (image)

        """
    fh_image = flip_horizontal(image)
    show(fh_image)


# print(__name__)
if __name__ == "__main__":
    original = load_image(choose_file())
    show(original)

    test_grayscale(original)
    test_negative(original)
    test_solarize(original)
    test_black_and_white(original)
    test_black_and_white_and_gray(original)
