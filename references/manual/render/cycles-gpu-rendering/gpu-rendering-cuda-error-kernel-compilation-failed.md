# GPU Rendering: CUDA Error: Kernel compilation failed

(Substitute the name or path of the compatible GCC compiler).

Remove compatibility checks
If that gets nowhere, strike this line out of
/usr/local/cuda/include/host_config.h :

```text
#error -- unsupported GNU version! gcc x.x and up are not supported!
```

Doing so opens the way for Cycles to build the CUDA rendering kernel on its first run against your GPU. With the kernel built, launch Blender as usual and it keeps using that CUDA kernel to render.

### CUDA Error: Kernel compilation failed 

This one can crop up with a new NVIDIA graphics card the installed Blender version and CUDA toolkit do not yet know.
Blender may then try to build a kernel for your card on the fly and fall short.

In this case you can:

- Check if the latest Blender version
(official or experimental builds)
supports your graphics card.

- If you build Blender yourself, try to download and install a newer CUDA developer toolkit.

As a rule there is no need to install the CUDA toolkit, since Blender arrives with precompiled kernels.

[Related references](INDEX.md).
