
# Statistical Measurements for Instance Segmentation and Classification

## Description

In this directory, the script `stats_utils.py` contains the statistical measurements code for instance segmentation. In order of appearance, the available measurements are AJI+, AJI, DICE2, Panoptic Quality (PQ), DICE which can be access through following functions:

`get_fast_aji()`: aji ported from the matlab code but is optimised for speed **[1]**. <br/>
`get_fast_aji_plus()`: extension of aggregated jaccard index that doesn't suffer from over-penalisation. <br/>
`get_dice_1()` and `get_dice_2()`: standard dice and ensemble dice (DICE2) **[2]** measures respectively. <br/> 
`get_fast_dice_2()`: ensemble dice optimised for speed. <br/>
`get_fast_panoptic_quality()`: panoptic quality as used in **[3]**.

## Processing

### Instance Segmentation

To get the instance segmentation measurements, run: <br/>
`python compute_stats.py --mode=instance --pred_dir='pred_dir' --true_dir='true_dir'` 

Toggle `print_img_stats` to determine whether to show the stats for each image.

### Classification

To get the classification measurements, run: <br/>
`python compute_stats.py --mode=type --pred_dir='pred_dir' --true_dir='true_dir'`

The above calculates the classification metrics, as discussed in the evaluation metrics section of our paper. 


## References
**[1]** Kumar, Neeraj, Ruchika Verma, Sanuj Sharma, Surabhi Bhargava, Abhishek Vahadane, and Amit Sethi. "A dataset and a technique for generalized nuclear segmentation for computational pathology." IEEE transactions on medical imaging 36, no. 7 (2017): 1550-1560. <br/>
**[2]** Vu, Quoc Dang, Simon Graham, Minh Nguyen Nhat To, Muhammad Shaban, Talha Qaiser, Navid Alemi Koohbanani, Syed Ali Khurram et al. "Methods for Segmentation and Classification of Digital Microscopy Tissue Images." arXiv preprint arXiv:1810.13230 (2018).  <br/>
**[3]** Kirillov, Alexander, Kaiming He, Ross Girshick, Carsten Rother, and Piotr Dollár. "Panoptic Segmentation." arXiv preprint arXiv:1801.00868 (2018).







