# GPU Rendering: Rendering Technologies, CUDA – NVIDIA, OptiX – NVIDIA, HIP – AMD, oneAPI – Intel

## GPU Rendering

### GPU Rendering 

GPU rendering hands the work to your graphics card in place of the CPU . It often comes out faster, since modern GPUs are made to chew through huge amounts of arithmetic.
The catch: limited memory leaves them weaker on complex scenes, and sharing one card between display and rendering hurts interactivity.

To enable GPU rendering:

- Select either CUDA , OptiX , HIP , oneAPI , or Metal
in the Cycles Render Devices user preference.

- Enable the available devices for the chosen backend.

- Configure each scene to use the GPU Compute Device.

### Rendering Technologies 

Which GPU technology Blender can use turns on the particular GPU maker and the operating system.

### CUDA – NVIDIA 

CUDA runs on Windows and Linux and wants an NVIDIA graphics card of compute capability 5.0 or higher. To check yours makes the cut, see the list of NVIDIA graphics cards with their compute capabilities and supported cards.

### OptiX – NVIDIA 

OptiX runs on Windows and Linux, asking for an NVIDIA graphics card of compute capability 5.0 or higher plus a driver no older than 535. To check yours makes the cut, see the list of NVIDIA graphics cards.

OptiX taps the hardware ray-tracing acceleration in RTX cards for a performance lift.

OpenImageDenoise picks up GPU acceleration from compute capability 7.0 upward, which takes in every NVIDIA RTX card.

### HIP – AMD 

HIP runs on Windows and Linux and wants an AMD graphics card of the RDNA1 architecture or newer. It works on discrete GPUs and APUs both.

Supported GPUs include:

- Radeon RX 5000 Series

- Radeon RX 6000 Series and Radeon Pro W6000 Series

- Radeon RX 7000 Series and Radeon Pro W7000 Series

- Radeon RX 9000 Series

Minimum driver versions:

- Windows: Radeon Software 24.9.1 or Radeon PRO Software 24.Q4

- Linux: Radeon Software 23.40 or ROCm HIP Runtime 6.0

For more on AMD graphics cards and their architectures, check AMD's website.

The latest drivers carry hardware ray-tracing support. Switch it on in the preferences; Radeon RX 6000 and newer back it.

GPU accelerated denoising lands on discrete Radeon RX 6000 and newer.

### oneAPI – Intel 

oneAPI is a compute library running on Windows and Linux that wants an Intel® Arc™ graphics card on the Xe HPG architecture. Hardware acceleration spans both ray-tracing and denoising.

Supported GPUs include:

- Intel® Arc™ A-Series

- Intel® Arc™ B-Series

Minimum driver versions:

- Windows: Intel Graphics Driver XX.X.101.5518

- Linux: intel-level-zero-gpu package 1.3.27642,
typically available through the intel-compute-runtime package XX.XX.34666.3

For more on Intel graphics cards and their architectures, check Intel's website.

GPU accelerated denoising reaches every supported GPU.

[Related references](INDEX.md).
