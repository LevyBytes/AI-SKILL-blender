# gpu.platform

## GPU Platform Utilities (gpu.platform)

### GPU Platform Utilities (gpu.platform)

This module exposes the GPU Platform definitions.
gpu.platform. backend_type_get ( )

Fetch the GPU backend that is currently active.

Returns :

Backend type (‘OPENGL’, ‘VULKAN’, ‘METAL’, ‘NONE’, ‘UNKNOWN’).

Return type :

str
gpu.platform. device_type_get ( )

Fetch the category of GPU device in use.

Returns :

Device type (‘APPLE’, ‘NVIDIA’, ‘AMD’, ‘INTEL’, ‘SOFTWARE’, ‘QUALCOMM’, ‘UNKNOWN’).

Return type :

str
gpu.platform. renderer_get ( )

Fetch the GPU that will handle rendering.

Returns :

GPU name.

Return type :

str
gpu.platform. vendor_get ( )

Fetch the GPU vendor.

Returns :

Vendor name.

Return type :

str
gpu.platform. version_get ( )

Fetch the GPU driver version.

Returns :

Driver version.

Return type :

str

[Related references](INDEX.md).
