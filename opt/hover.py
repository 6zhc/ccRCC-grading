import tensorflow as tf

#### Training parameters
###
# np+hv : double branches nework, 
#     1 branch nuclei pixel classification (segmentation)
#     1 branch regressing horizontal/vertical coordinate w.r.t the (supposed) 
#     nearest nuclei centroids, coordinate is normalized to 0-1 range
#
# np+dst: double branches nework
#     1 branch nuclei pixel classification (segmentation)
#     1 branch regressing nuclei instance distance map (chessboard in this case),
#     the distance map is normalized to 0-1 range

np_hv = {
    'train_input_shape': [350, 350],
    'train_mask_shape': [160, 160],
    'infer_input_shape': [350, 350],
    'infer_mask_shape': [160, 160],
    'infer_avalible_shape': [160, 160],

    'training_phase': [
        {
            'nr_epochs': 40,
            'manual_parameters': {
                # tuple(initial value, schedule)
                'learning_rate': (1.0e-4, [('20', 1.0e-5)]),
            },
            'pretrained_path': 'pretrained_model/ImageNet-ResNet50-Preact.npz',
            'train_batch_size': 4,
            'infer_batch_size': 8,

            'model_flags': {
                'freeze': True
            }
        },

        {
            'nr_epochs': 40,
            'manual_parameters': {
                # tuple(initial value, schedule)
                'learning_rate': (1.0e-4, [('20', 1.0e-5)]),
            },
            # path to load, -1 to auto load checkpoint from previous phase, 
            # None to start from scratch
            'pretrained_path': -1,
            'train_batch_size': 2,  # unfreezing everything will
            'infer_batch_size': 4,

            'model_flags': {
                'freeze': False
            }
        }
    ],

    'loss_term': {'bce': 1, 'dice': 1, 'mse': 2, 'msge': 1},

    'optimizer': tf.train.AdamOptimizer,

    'inf_auto_metric': 'valid_mean_dice',
    'inf_auto_comparator': '>',
    'inf_batch_size': 16,
}

np_dg = {
    'train_input_shape': [350, 350],
    'train_mask_shape': [160, 160],
    'infer_input_shape': [350, 350],
    'infer_mask_shape': [160, 160],
    'infer_avalible_shape': [100, 100],

    'training_phase': [
        {
            'nr_epochs': 40,
            'manual_parameters': {
                # tuple(initial value, schedule)
                'learning_rate': (1.0e-4, [('20', 1.0e-5)]),
            },
            'pretrained_path': 'pretrained_model/ImageNet-ResNet50-Preact.npz',
            'train_batch_size': 4,
            'infer_batch_size': 8,

            'model_flags': {
                'freeze': True
            }
        },

        {
            'nr_epochs': 50,
            'manual_parameters': {
                # tuple(initial value, schedule)
                'learning_rate': (1.0e-4, [('25', 1.0e-5)]),
            },
            # path to load, -1 to auto load checkpoint from previous phase, 
            # None to start from scratch
            'pretrained_path': -1,
            'train_batch_size': 2,  # unfreezing everything will
            'infer_batch_size': 8,

            'model_flags': {
                'freeze': False
            }
        },

    ],

    'loss_term': {'bce': 1, 'dice': 1, 'mae': 2, 'ssim': 1},

    'optimizer': tf.train.AdamOptimizer,

    'inf_auto_metric': 'valid_ssim',
    'inf_auto_comparator': '>',
    'inf_batch_size': 16,
}

np_dist = {
    'train_input_shape': [270, 270],
    'train_mask_shape': [80, 80],
    'infer_input_shape': [270, 270],
    'infer_mask_shape': [80, 80],

    'training_phase': [
        {
            'nr_epochs': 50,
            'manual_parameters': {
                # tuple(initial value, schedule)
                'learning_rate': (1.0e-4, [('25', 1.0e-5)]),
            },
            'pretrained_path': 'pretrained_model/ImageNet-ResNet50-Preact.npz',
            'train_batch_size': 8,
            'infer_batch_size': 16,

            'model_flags': {
                'freeze': True
            }
        },

        {
            'nr_epochs': 50,
            'manual_parameters': {
                # tuple(initial value, schedule)
                'learning_rate': (1.0e-4, [('25', 1.0e-5)]),
            },
            # path to load, -1 to auto load checkpoint from previous phase, 
            # None to start from scratch
            'pretrained_path': -1,
            'train_batch_size': 4,  # unfreezing everything will
            'infer_batch_size': 16,

            'model_flags': {
                'freeze': False
            }
        }
    ],

    'optimizer': tf.train.AdamOptimizer,

    'inf_auto_metric': 'valid_dice',
    'inf_auto_comparator': '>',
    'inf_batch_size': 16,
}
