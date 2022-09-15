## Laniatus Games Studio Inc. | NOTE: The following #define macro was replaced in-line:
#ORIGINAL METINII C CODE: #define DO_ALL_BLEND_INFO(iter) for (iter=s_blend_info.begin(); iter!=s_blend_info.end(); ++iter)


class BLEND_ITEM_INFO:

    def __init__(self):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self.item_vnum = 0
        self.apply_type = 0
        self.apply_value = [0 for _ in range((int)LGEMiscellaneous.DEFINECONSTANTS.MAX_BLEND_ITEM_VALUE)]
        self.apply_duration = [0 for _ in range((int)LGEMiscellaneous.DEFINECONSTANTS.MAX_BLEND_ITEM_VALUE)]
