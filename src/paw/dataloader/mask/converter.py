import cv2
from numpy.typing import ArrayLike


def mask2segmentation(filepath: str) -> ArrayLike:
    # Load the mask image
    mask_image = cv2.imread(filepath, 0)  # Read as grayscale

    # Threshold the image to create a binary mask
    _, binary_mask = cv2.threshold(mask_image, 1, 255, cv2.THRESH_BINARY)

    # Perform morphological opening to remove outliers
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)

    # Find contours in the binary image
    contours, _ = cv2.findContours(
        binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # assert len(contours) == 1

    return contours
