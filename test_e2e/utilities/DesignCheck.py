import cv2
import numpy as np


class DesignCheck:
    # This will compare website design to saved version to see if its properly displayed (visual check)

    @staticmethod
    def verify(screen1, screen2, mask=255):
        if screen1 is None or screen2 is None:
            return 0
        template = cv2.imread(screen1)
        captured = cv2.imdecode(np.asarray(bytearray(screen2), dtype=np.uint8), 1)

        pix_diff = 0
        pix_count = template.shape[0] * template.shape[1]

        for i in range(0, template.shape[0], 1):
            for j in range(0, template.shape[1], 1):
                pix_template = template[i, j]
                pix_captured = captured[i, j]
                if pix_template[0] != pix_captured[0] and pix_template[0] != mask:
                    pix_diff = pix_diff + 1

        return round(((pix_count - pix_diff) / pix_count) * 100, 2)
