import numpy as np
import matplotlib.pyplot as plt
import phantominator as ph


def main(real_scaler, im_scaler, size):
    img = ph.shepp_logan(size)

    k = np.fft.fftshift(np.fft.fft2(img))

    real_part = np.real(k)
    imag_part = np.imag(k)
    k_modified = real_scaler * real_part + im_scaler * imag_part

    img_mod_cplx = np.fft.ifft2(np.fft.ifftshift(k_modified))
    img_mod_mag = np.abs(img_mod_cplx)

    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

    axs[0].imshow(img, cmap="gray")
    axs[0].set_title("Original")
    axs[0].axis("off")

    axs[1].imshow(img_mod_mag, cmap="gray")
    axs[1].set_title("Modified Magnitude")
    axs[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    real_scaler = 1.0
    im_scaler = 0
    main(real_scaler, im_scaler, size=256)
