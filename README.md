# Hi4D: 4D Instance Segmentation of Close Human Interaction


## [Project Page](https://yifeiyin04.github.io/Hi4D/) | [Paper](https://arxiv.org/abs/2303.15380) | [Video](https://youtu.be/DrvL2XkW7rw) | [Data](https://forms.gle/dR6FUpMTCjp97xMx5) 
<img src="assets/teaser.png"/> 
Hi4D (Humans interacting in 4D), a dataset of humans in close physical interaction that contains (A) 4D textured scans, (B) instance meshes with vertex-level contact annotations, (C) instance segmentation masks in 2D and 3D, (D) registered parametric body models with contact annotations. 

## Contents
1. [Dataset](#hi4d-dataset)
2. [Visualization](#visualization)
2. [Citation](#citation)
3. [Contact](#contact)

## Hi4D Dataset
Please fill out the [Hi4D Application Form](https://forms.gle/dR6FUpMTCjp97xMx5) to access Hi4D. We will send you an email with more information after approval of your application.\
\
Hi4D dataset structure can be found in [Dataset Structure](dataset.md).

## Visualization
We use [AITViewer](https://github.com/eth-ait/aitviewer) to visualize the dataset. 
### Installation
```bash
      pip install aitviewer
```
### Usage
1. Change the `smplx_models` parameter in `visualize_hi4d.py` to the path of SMPL-X models. More information please refer to [AITViewer Documentation](https://eth-ait.github.io/aitviewer/parametric_human_models/supported_models.html).
2. Change the `HI4D_PATH` parameter in `visualize_hi4d.py` to the path of Hi4D dataset.
3. Run the following command to visualize the dataset.
```bash
      python visualize_hi4d.py --pair {PAIRXX} --action {ACTIONXX} --vis {VIS_TYPE}
```

## Citation
If you find this work useful for your research, please cite our paper:
``` bibtex
@inproceedings{yin2023hi4d,
      author = {Yin, Yifei and Guo, Chen and Kaufmann, Manuel and Zarate, Juan and Song, Jie and Hilliges, Otmar}, 
      title = {Hi4D: 4D Instance Segmentation of Close Human Interaction}, 
      booktitle = {Computer Vision and Pattern Recognition (CVPR)},
      year = {2023}
      }
```

## Contact
If you have any questions, please contact [Yifei Yin](mailto:yifyin@ethz.ch) or [Chen Guo](mailto:chen.guo@inf.ethz.ch).
