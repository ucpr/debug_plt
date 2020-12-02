from logging import getLogger, DEBUG, ERROR

import numpy as np
import matplotlib.pyplot as plt

import skimage.measure as measure
from skimage.draw import ellipse
from skimage.transform import rotate

from tedasuke import tedasuke

logger = getLogger(__name__)
logger.setLevel(ERROR)


def create_test_image():
    image = np.zeros((600, 600))

    rr, cc = ellipse(300, 350, 100, 220)
    image[rr, cc] = 1
    image = rotate(image, angle=15, order=0)

    rr, cc = ellipse(100, 110, 60, 50)
    image[rr, cc] = 1
    return image


def main():
    img = create_test_image()
    _, ax = plt.subplots()
    dax = tedasuke(ax, logger, level=DEBUG)

    ax.imshow(img, cmap=plt.cm.gray)

    labels = measure.label(img)
    regions = measure.regionprops(labels, img)

    for i in range(labels.max()):
        props = regions[i]
        label = props.label

        contour = measure.find_contours(labels == label, 0.8)[0]
        dax.plot(contour[:, 1], contour[:, 0], linewidth=2)

    plt.show()


if __name__ == "__main__":
    main()
