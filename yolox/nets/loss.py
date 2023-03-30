from torch import nn
import torch


def bbox_iou(pred, ground, box_type: str = 'centerwh'):  # box_type= centerwh or lefttoprightdown
    if box_type == 'lefttoprightdown':
        # print('input type is lefttoprightdown')
        box1 = torch.stack([(pred[:, 2] + pred[:, 0]) / 2, (pred[:, 1] + pred[:, 3]) / 2, pred[:, 2] - pred[:, 0],
                            pred[:, 3] - pred[:, 1]], dim=1)
        box2 = torch.stack(
            [(ground[:, 2] + ground[:, 0]) / 2, (ground[:, 1] + ground[:, 3]) / 2, ground[:, 2] - ground[:, 0],
             ground[:, 3] - ground[:, 1]], dim=1)
    elif box_type == 'centerwh':
        # print('input type is centerwh')
        box1 = pred
        box2 = ground
    else:
        raise ValueError('argument box_type in bbox_iuou() shoule be: centerwh or lefttoprightdown')

    # lefttop and rightdown of union_area
    tl = torch.max((box1[:, :2] - box1[:, 2:] / 2), (box2[:, :2] - box2[:, 2:] / 2))
    br = torch.min((box1[:, :2] + box1[:, 2:] / 2), (box2[:, :2] + box2[:, 2:] / 2))

    # compute inter_area
    en = (tl < br).type(tl.type()).prod(dim=1)
    inter_area = torch.prod(br - tl, 1) * en

    # compute union_area
    pred_area = torch.prod(box1[:, 2:], 1)
    ground_area = torch.prod(box2[:, 2:], 1)
    union_area = pred_area + ground_area - inter_area

    # compute iou
    iou = inter_area / (union_area + 1e-16)
    # iou = inter_area / union_area
    return iou


class MyIoULoss(nn.Module):
    def __init__(self, box_type='centerwh', iou_type='SIoU'):  # iou_type:IoU,GIoU,DIoU,CIoU,SIoU,EIoU
        super(MyIoULoss, self).__init__()
        self.box_type = box_type
        self.iou_type = iou_type

    def forward(self, box1, box2, theta=4):  # box1: predict boxes, box2: ground truth boxes
        total_loss = 0
        # compute coordinate of each box
        box1_x1, box1_y1, box1_x2, box1_y2 = 0, 0, 0, 0
        box2_x1, box2_y1, box2_x2, box2_y2 = 0, 0, 0, 0
        center_x1, center_y1, w1, h1 = 0, 0, 0, 0
        center_x2, center_y2, w2, h2 = 0, 0, 0, 0
        if self.box_type == 'lefttoprightdown':
            box1_x1, box1_y1, box1_x2, box1_y2 = box1[:, 0], box1[:, 1], box1[:, 2], box1[:, 3]
            box2_x1, box2_y1, box2_x2, box2_y2 = box2[:, 0], box2[:, 1], box2[:, 2], box2[:, 3]
            center_x1, center_y1, w1, h1 = (box1_x1 + box1_x2) / 2, (box1_y1 + box1_y2) / 2, torch.abs(
                box1_x1 - box1_x2), torch.abs(box1_y1 - box1_y2)
            center_x2, center_y2, w2, h2 = (box2_x1 + box2_x2) / 2, (box2_y1 + box2_y2) / 2, torch.abs(
                box2_x1 - box2_x2), torch.abs(box2_y1 - box2_y2)
        elif self.box_type == 'centerwh':
            center_x1, center_y1, w1, h1 = box1[:, 0], box1[:, 1], box1[:, 2], box1[:, 3]
            center_x2, center_y2, w2, h2 = box2[:, 0], box2[:, 1], box2[:, 2], box2[:, 3]
            box1_x1, box1_y1, box1_x2, box1_y2 = center_x1 - w1 / 2, center_y1 - h1 / 2, center_x1 + w1 / 2, center_y1 + h1 / 2
            box2_x1, box2_y1, box2_x2, box2_y2 = center_x2 - w2 / 2, center_y2 - h2 / 2, center_x2 + w2 / 2, center_y2 + h2 / 2

        # IOU between box1 and box2
        iou = bbox_iou(box1, box2, self.box_type)

        if self.iou_type == 'IoU':
            # iou loss
            iou_loss = 1 - iou
            total_loss = iou_loss

        elif self.iou_type == 'GIoU':
            # iou loss
            iou_loss = 1 - iou
            total_loss = iou_loss

            # shape of minimum adjacent rectangle
            cx1, cy1 = torch.min(box1_x1, box2_x1), torch.min(box1_y1, box2_y1)
            cx2, cy2 = torch.max(box1_x2, box2_x2), torch.max(box1_y2, box2_y2)

            # area loss
            predict_box = []
            gt_box = []
            if self.box_type == 'lefttoprightdown':
                # print('input type is lefttoprightdown')
                predict_box = torch.stack(
                    [(box1[:, 2] + box1[:, 0]) / 2, (box1[:, 1] + box1[:, 3]) / 2, box1[:, 2] - box1[:, 0],
                     box1[:, 3] - box1[:, 1]], dim=1)
                gt_box = torch.stack(
                    [(box2[:, 2] + box2[:, 0]) / 2, (box2[:, 1] + box2[:, 3]) / 2, box2[:, 2] - box2[:, 0],
                     box2[:, 3] - box2[:, 1]], dim=1)
            elif self.box_type == 'centerwh':
                # print('input type is centerwh')
                predict_box = box1
                gt_box = box2
            C = torch.abs(cx1 - cx2) * torch.abs(cy1 - cy2)
            tl = torch.max((predict_box[:, :2] - predict_box[:, 2:] / 2), (gt_box[:, :2] - gt_box[:, 2:] / 2))
            br = torch.min((predict_box[:, :2] + predict_box[:, 2:] / 2), (gt_box[:, :2] + gt_box[:, 2:] / 2))
            en = (tl < br).type(tl.type()).prod(dim=1)
            inter_area = torch.prod(br - tl, 1) * en
            B = torch.prod(predict_box[:, 2:], 1)
            B_gt = torch.prod(gt_box[:, 2:], 1)
            union_area = B + B_gt - inter_area
            area_loss = (C - union_area) / C.clamp(1e-16)

            total_loss = iou_loss + area_loss

        elif self.iou_type == 'DIoU':
            # iou loss
            iou_loss = 1 - iou

            # shape of minimum adjacent rectangle
            cx1, cy1 = torch.min(box1_x1, box2_x1), torch.min(box1_y1, box2_y1)
            cx2, cy2 = torch.max(box1_x2, box2_x2), torch.max(box1_y2, box2_y2)
            c = torch.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

            #  distance loss
            distance_loss = ((center_x1 - center_x2) ** 2 + (center_y1 - center_y2) ** 2) / (c ** 2).clamp(1e-16)

            total_loss = iou_loss + distance_loss

        elif self.iou_type == 'CIoU':
            # iou loss
            iou_loss = 1 - iou

            # shape of minimum adjacent rectangle
            cx1, cy1 = torch.min(box1_x1, box2_x1), torch.min(box1_y1, box2_y1)
            cx2, cy2 = torch.max(box1_x2, box2_x2), torch.max(box1_y2, box2_y2)
            c = torch.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

            # width and height of box1 box2
            w_gt = torch.abs(box1_x1 - box1_x2)
            h_gt = torch.abs(box1_y1 - box1_y2)
            w_pred = torch.abs(box2_x1 - box2_x2)
            h_pred = torch.abs(box2_y1 - box2_y2)

            #  distance loss
            distance_loss = ((center_x1 - center_x2) ** 2 + (center_y1 - center_y2) ** 2) / (c ** 2).clamp(1e-16)

            #  ratio loss
            v = (4 / torch.pi ** 2) * (
                    torch.atan(w_gt / h_gt.clamp(1e-16)) - torch.atan(w_pred / h_pred.clamp(1e-16))) ** 2
            alpha = v / (1 - iou + v).clamp(1e-16)
            ratio_loss = alpha * v

            total_loss = iou_loss + distance_loss + ratio_loss

        elif self.iou_type == 'EIoU':
            # iou loss
            iou_loss = 1 - iou

            # shape of minimum adjacent rectangle
            cx1, cy1 = torch.min(box1_x1, box2_x1), torch.min(box1_y1, box2_y1)
            cx2, cy2 = torch.max(box1_x2, box2_x2), torch.max(box1_y2, box2_y2)
            c = torch.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)
            cw = torch.abs(cx1 - cx2)
            ch = torch.abs(cy1 - cy2)

            # width and height of box1 box2
            w_gt = torch.abs(box1_x1 - box1_x2)
            h_gt = torch.abs(box1_y1 - box1_y2)
            w_pred = torch.abs(box2_x1 - box2_x2)
            h_pred = torch.abs(box2_y1 - box2_y2)

            #  distance loss
            distance_loss = ((center_x1 - center_x2) ** 2 + (center_y1 - center_y2) ** 2) / (c ** 2).clamp(1e-16)

            # width loss
            width_loss = (w_gt - w_pred) ** 2 / (cw ** 2).clamp(1e-16)

            # height loss
            height_loss = (h_gt - h_pred) ** 2 / (ch ** 2).clamp(1e-16)

            total_loss = iou_loss + distance_loss + width_loss + height_loss

        elif self.iou_type == 'SIoU':
            # iou loss
            iou_loss = 1 - iou

            # distance loss
            gama = 2 - torch.cos(
                2 * torch.atan(
                    torch.abs(center_y1 - center_y2) / torch.abs(center_x1 - center_x2).clamp(1e-16)) - torch.pi / 2)
            # shape of minimum adjacent rectangle
            cx1, cy1 = torch.min(box1_x1, box2_x1), torch.min(box1_y1, box2_y1)
            cx2, cy2 = torch.max(box1_x2, box2_x2), torch.max(box1_y2, box2_y2)
            cw, ch = cx2 - cx1, cy2 - cy1
            distance_loss = (1 - torch.exp(-gama * ((center_x2 - center_x1) / cw.clamp(1e-16)) ** 2)) + (1 - torch.exp(
                -gama * ((center_y2 - center_y1) / ch.clamp(1e-16)) ** 2))

            # shape loss
            shape_loss = (1 - torch.exp(-torch.abs(w1 - w2) / torch.max(w1, w2).clamp(1e-16))) ** theta + (
                    1 - torch.exp(-torch.abs(h1 - h2) / torch.max(h1, h2).clamp(1e-16))) ** theta

            total_loss = iou_loss + (distance_loss + shape_loss) / 2

        # iou_loss = torch.cos(iou) mAP67.3_s_bs32_epoch300_256
        elif self.iou_type == 'MyIoU-1':
            # iou loss
            iou_loss = torch.cos(iou * torch.pi / 2)

            # shape of minimum adjacent rectangle
            cx1, cy1 = torch.min(box1_x1, box2_x1), torch.min(box1_y1, box2_y1)
            cx2, cy2 = torch.max(box1_x2, box2_x2), torch.max(box1_y2, box2_y2)
            c = torch.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

            # width and height of box1 box2
            w_gt = torch.abs(box1_x1 - box1_x2)
            h_gt = torch.abs(box1_y1 - box1_y2)
            w_pred = torch.abs(box2_x1 - box2_x2)
            h_pred = torch.abs(box2_y1 - box2_y2)

            #  distance loss
            distance_loss = ((center_x1 - center_x2) ** 2 + (center_y1 - center_y2) ** 2) / (c ** 2).clamp(1e-16)

            #  ratio loss
            v = (4 / torch.pi ** 2) * (
                    torch.atan(w_gt / h_gt.clamp(1e-16)) - torch.atan(w_pred / h_pred.clamp(1e-16))) ** 2
            alpha = v / (1 - iou + v).clamp(1e-16)
            ratio_loss = alpha * v

            total_loss = iou_loss + distance_loss + ratio_loss

        elif self.iou_type == 'MyIoU-2':
            # iou loss
            iou_loss = torch.sqrt(1 - iou ** 2)

            # shape of minimum adjacent rectangle
            cx1, cy1 = torch.min(box1_x1, box2_x1), torch.min(box1_y1, box2_y1)
            cx2, cy2 = torch.max(box1_x2, box2_x2), torch.max(box1_y2, box2_y2)
            c = torch.sqrt((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2)

            # width and height of box1 box2
            w_gt = torch.abs(box1_x1 - box1_x2)
            h_gt = torch.abs(box1_y1 - box1_y2)
            w_pred = torch.abs(box2_x1 - box2_x2)
            h_pred = torch.abs(box2_y1 - box2_y2)

            #  distance loss
            distance_loss = torch.sqrt(((center_x1 - center_x2) ** 2 + (center_y1 - center_y2) ** 2) / (c ** 2).clamp(1e-16))

            #  shape loss
            mkone_para = 4 / torch.pi ** 2
            v = mkone_para * (torch.atan(w_gt / h_gt.clamp(1e-16)) - torch.atan(w_pred / h_pred.clamp(1e-16))) ** 2
            alpha = mkone_para * (torch.atan(torch.sqrt(w_gt ** 2 + h_gt ** 2)) - torch.atan(
                torch.sqrt(w_pred ** 2 + h_pred ** 2))) ** 2
            shape_loss = alpha + v

            total_loss = iou_loss + distance_loss + shape_loss

        return total_loss


if __name__ == '__main__':
    # pred_box = torch.randn(10, 4)
    # ground_box = torch.randn(10, 4)
    pred_box = torch.Tensor([[916, 125, 1022, 588], [412, 66, 605, 288], [475, 290, 571, 400]])
    ground_box = torch.Tensor([[901, 141, 1000, 600], [405, 85, 596, 287], [453, 298, 542, 397]])
    print(pred_box, ground_box)
    loss_siou = MyIoULoss(box_type='centerwh', iou_type='SIoU')
    loss_iou = MyIoULoss(box_type='centerwh', iou_type='IoU')
    loss_giou = MyIoULoss(box_type='centerwh', iou_type='GIoU')
    loss_ciou = MyIoULoss(box_type='centerwh', iou_type='CIoU')
    loss_diou = MyIoULoss(box_type='centerwh', iou_type='DIoU')
    loss_eiou = MyIoULoss(box_type='centerwh', iou_type='EIoU')
    # yolox_loss = IOUloss()
    print('loss_iou:{}'.format(loss_iou(pred_box, ground_box)))
    print('loss_giou:{}'.format(loss_giou(pred_box, ground_box)))
    print('loss_ciou:{}'.format(loss_ciou(pred_box, ground_box)))
    print('loss_diou:{}'.format(loss_diou(pred_box, ground_box)))
    print('loss_eiou:{}'.format(loss_eiou(pred_box, ground_box)))
    print('loss_siou:{}'.format(loss_siou(pred_box, ground_box)))
