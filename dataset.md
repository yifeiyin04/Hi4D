# Hi4D Dataset Structure

After unzip the downloaded files, please rearrange the dataset structure as follows:
```
DATASET_PATH
├──pair00
├──pair01
├──...
├──pairXX
```

For each sequence, you will find a `meta.npz` file and six folders: `cameras`, `frames`, `frames_vis`, `images`, `seg`, `smpl`. 
```
DATASET_PATH
├──pairXX
│   ├── actionXX
│       ├── meta.npz
│       ├── cameras
│       ├── frames
│       ├── frames_vis
│       ├── images
│       ├── seg
│       ├── smpl
```
The detailed information to each folder is summarized below.

## meta.npz
This file contains the basic information of the sequence. It contains the following keys:
| Key | Description |
| --- | --- |
| `start` | the start frame id of the sequence|
| `end` | the end frame id of the sequence|
| `num_persons` | number of subjects in the sequence (2)|
| `genders` | genders of the subjects|
| `betas` | SMPL body shape parameters of the subjects|
| `contact_ids` | list of frame ids with phsical contact|
| `mono_cam` | the selected camera view for vision tasks in monocular setting|

## cameras
This folder contains the file `rgb_cameras.npz`, which contains the calibration parameters of the released 8 cameras. `rgb_cameras.npz` contains the following keys:

| Key | Description |
| --- | --- |
| `ids` | ids of the selected 8 cameras|
| `intirnsics` | 8x3x3 camera intrinsic matrix|
| `extrinsics` | 8x3x4 camera extrinsic matrix|
| `dist_coeffs` | 8x5 camera distortion parameters|

## frames
 This folder contains the textured raw scans of the sequence.
```
DATASET_PATH
├──pairXX
│   ├──actionXX
│       ├──frames
|           ├──Atlas-F00XXX.png         # mesh texture
|           ├──MatLib-F00XXX.mtl        # mesh material property
|           ├──mesh-f00XXX.obj          # reconstructed 3D scan of the object
```

## frames_vis
This folder contains the textured raw scans of the sequence with low-resolution texture for visualization efficiency.
```
DATASET_PATH
├──pairXX
│   ├──actionXX
│       ├──frames
|           ├──atlas-f00XXX.pkl         # low-res mesh texture (1024, 1024, 3)
|           ├──mesh-f00XXX.pkl          # mesh vertices, faces, normals and uvs
```

## images
This folder contains the RGB images of the sequence.
```
DATASET_PATH
├──pairXX
│   ├──actionXX
│       ├──images
|           ├──XX                       # camera id [4, 16, 28, 40, 52, 64, 76, 88]
|               ├──000XXX.jpg           # RGB image
```

## seg
This folder contains instance meshes and the segmentation masks in 2D and 3D of the sequence.
```
DATASET_PATH
├──pairXX
│   ├──actionXX
│       ├──seg
|           ├──img_seg_mask             # 2D segmentation masks
|               ├──XX                   # camera id [4, 16, 28, 40, 52, 64, 76, 88]
|                   ├──0                # subject id 0
|                       ├──000XXX.png 
|                   ├──1                # subject id 1
|                       ├──000XXX.png
|                   ├──all              # combined segmentation mask of all subjects
|                       ├──000XXX.png
|           ├──mesh_seg_mask            # 3D segmentation masks
|               ├──mesh-f00XXX.npz      # vertices mask, faces mask, and the source of the instance mesh of each subject
|           ├──instance                 # instance mesh of each subject
|               ├──0                    # subject id 0
|                   ├──mesh-f00XXX.npz  # instance mesh vertices and faces
|               ├──1                    # subject id 1
|                   ├──mesh-f00XXX.npz
```

## smpl
This folder contains the SMPL parameters of the sequence.
```
DATASET_PATH
├──pairXX
│   ├──actionXX
│       ├──smpl
|           ├──000XXX.npz               # SMPL parameters
```
SMPL parameters `000XXX.npz` file contains the following keys:
| Key | Description |
| --- | --- |
| `betas` | 2x10 SMPL body shape parameters|
| `body_pose` | 2x69 SMPL body pose parameters|
| `global_orient` | 2x3 SMPL global orientation parameters|
| `transl` | 2x3 translation parameters|
| `joints_3d` | 2x24x3 SMPL 3D joint locations|
| `verts` | 2x6890X3 SMPL vertices|
| `contact` | 2x6890 contact correspondences|







