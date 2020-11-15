TOP_LEFT =      (0, 0)
TOP_CENTER =    (0.5, 0)
TOP_RIGHT =     (1, 0)
CENTER_LEFT =   (0, 0.5)
CENTER =        (0.5, 0.5)
CENTER_RIGHT =  (1, 0.5)
BOTTOM_LEFT =   (0, 1)
BOTTOM_CENTER = (0.5, 1)
BOTTOM_RIGHT =  (1, 1)


def _compute_src_top_left(dst, src, dst_anchor, src_anchor, left_offset=0,
                          top_offset=0):
    dstw, dsth = dst.size
    srcw, srch = src.size

    x = dstw * dst_anchor[0] - srcw * src_anchor[0] + left_offset
    y = dsth * dst_anchor[1] - srch * src_anchor[1] + top_offset
    return x, y


def paste(dst, src, dst_anchor=CENTER, src_anchor=CENTER, left_offset=0,
          top_offset=0):
    """Paste src into dst, aligned according to src_anchor and dst_anchor.
    Position can be adjusted by specifying left_offset and top_offset. Offsets
    always apply from left-to-right and top-to-bottom, regardless of the
    anchors."""
    x, y = _compute_src_top_left(dst, src, dst_anchor, src_anchor,
                                 left_offset, top_offset)
    dst.paste(src, (int(x), int(y)))


def cut_hole(dst, mask, dst_anchor=CENTER, mask_anchor=CENTER, left_offset=0,
             top_offset=0):
    """Cut a hole in dst according to mask, which must have mode "1".
    Position can be adjusted by specifying left_offset and top_offset. Offsets
    always apply from left-to-right and top-to-bottom, regardless of the
    anchors."""
    x, y = _compute_src_top_left(dst, mask, dst_anchor, mask_anchor,
                                 left_offset, top_offset)
    dst.paste(0, (int(x), int(y)), mask)
