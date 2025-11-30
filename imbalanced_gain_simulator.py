import numpy as np
import matplotlib.pyplot as plt
import phantominator as ph
import argparse


def main(real_scaler, im_scaler, size):
    img = ph.shepp_logan(size)

    k = np.fft.fftshift(np.fft.fft2(img))

    real_part = np.real(k)
    imag_part = np.imag(k)
    k_modified = real_scaler * real_part + im_scaler * 1j* imag_part

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
    parser = argparse.ArgumentParser(
        description="Modify real/imaginary parts of k-space and compare images."
    )
    parser.add_argument(
        "--real_scaler",
        type=float,
        default=1.0,
        help="Scaling factor for real part of k-space (default: 1.0)",
    )
    parser.add_argument(
        "--im_scaler",
        type=float,
        default=1.0,
        help="Scaling factor for imaginary part of k-space (default: 1.0)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=256,
        help="Image size for Shepp-Logan phantom (default: 256)",
    )

    args = parser.parse_args()

    main(args.real_scaler, args.im_scaler, size=args.size)
