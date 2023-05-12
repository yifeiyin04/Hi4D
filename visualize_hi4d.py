from aitviewer.viewer import Viewer
from aitviewer.models.smpl import SMPLLayer
from aitviewer.renderables.smpl import SMPLSequence
from aitviewer.renderables.multi_view_system import MultiViewSystem
from aitviewer.renderables.meshes import VariableTopologyMeshes

from aitviewer.configuration import CONFIG as C
C.update_conf({"playback_fps": 30})
C.update_conf({"flat_rendering": True})
C.update_conf({"shadows_enabled": False})
C.update_conf({"smplx_models": "smplx/models"})


import numpy as np
import os
import glob
import tqdm
from pathlib import Path

COLORS = [[0.412,0.663,1.0,1.0], [1.0,0.749,0.412,1.0]]
CONTACT_COLORS = [[[0.412,0.663,1.0,1.0], [1.0, 0.412, 0.514, 1.0]], [[1.0,0.749,0.412,1.0], [1.0, 0.412, 0.514, 1.0]]] 

HI4D_PATH = "Dataset/Hi4D/"

def main(args):
    v = Viewer()
    v.scene.camera.dolly_zoom(-25)
    v.scene.camera.position[1] += 2
    v.scene.camera.target[1] += 1
    v.scene.origin.enabled = False
    v.run_animations = False
    v.playback_fps = 30

    

    root = Path(HI4D_PATH) / args.pair / args.action
    print("Visualization:", args.vis)

    # render raw meshes
    if "org" in args.vis:
        org_meshes = VariableTopologyMeshes.from_directory(root / "frames_vis", name='org_meshes')
        v.scene.add(org_meshes)

    # render segmented raw meshes
    if "seg" in args.vis:
        
        seg_meshes = VariableTopologyMeshes.from_directory(root / "frames_vis", name='seg_meshes')
        seg_mask_paths = sorted(glob.glob(f"{root}/seg/mesh_seg_mask/*.npz"))
        seg_meshes.vertex_colors = [np.array(COLORS)[np.load(seg_mask_path)["vertices_mask"]] for seg_mask_path in seg_mask_paths]
        seg_meshes.show_texture = False
        seg_meshes.material.diffuse = 1.0
        seg_meshes.material.ambient = 0.0
        v.scene.add(seg_meshes)

    # render instance meshes
    if "instance" in args.vis:
        for p in range(2):
            instance_paths = sorted(glob.glob(f"{root}/seg/instance/{p}/*.npz"))
            vertices, faces = [], []
            for instance_path in tqdm.tqdm(instance_paths):
                instance_params = np.load(instance_path)
                vertices.append(instance_params["vertices"])
                faces.append(instance_params["faces"])
            instance_meshes = VariableTopologyMeshes(vertices=np.array(vertices), faces=np.array(faces), color=tuple(COLORS[p]), name='instance'+ str(p), preload=False)
            instance_meshes.material.diffuse = 1.0
            instance_meshes.material.ambient = 0.0
            v.scene.add(instance_meshes)

    # render SMPL
    if "smpl" in args.vis:
        gender = dict(np.load(os.path.join(root, "meta.npz")))["genders"]
        for p in range(2):
            smpl_layer = SMPLLayer(model_type="smpl", gender=gender[p])
            smpl_paths = sorted(glob.glob(f"{root}/smpl/*.npz"))

            poses_body, poses_root, betas, trans, colors = [], [], [], [], []
            for smpl_path in tqdm.tqdm(smpl_paths):
                smpl_params = np.load(smpl_path)
                poses_body.append(smpl_params["body_pose"][p])
                poses_root.append(smpl_params["global_orient"][p])
                betas.append(smpl_params["betas"][p])
                trans.append(smpl_params["transl"][p])
                colors.append(np.array(CONTACT_COLORS[p])[np.array(smpl_params["contact"][p] > 0, dtype=int)])

            smpl_seq = SMPLSequence(poses_body = np.array(poses_body), 
                                    smpl_layer = smpl_layer,
                                    poses_root = np.array(poses_root),
                                    betas = np.array(betas),
                                    trans = np.array(trans))
            smpl_seq.mesh_seq.vertex_colors = np.array(colors)
            smpl_seq.name = "smpl" + str(p)
            smpl_seq.mesh_seq.material.diffuse = 1.0
            smpl_seq.mesh_seq.material.ambient = 0.1
            v.scene.add(smpl_seq)

    # render cameras systems
    if "rgb" in args.vis:
        cols = 940
        rows = 1280
        camera_system = MultiViewSystem(os.path.join(root, 'cameras/rgb_cameras.npz'),
                                        os.path.join(root, 'images'), cols, rows, v)
        camera_system._billboards_enabled = True
        # camera_system.view_from_camera(0)

        v.scene.add(camera_system)

    v.run()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--pair', type=str, required=True, help='pair id')
    parser.add_argument('--action', type=str, required=True, help='action id')

    # Warining: Visualizing instance meshes (instance) can take a lot of memory!
    parser.add_argument('--vis', nargs='+', type=str, default=['org', 'seg', 'smpl', 'rgb'], help='visualize type: org, seg, instance, smpl, rgb')
    

    main(parser.parse_args())
