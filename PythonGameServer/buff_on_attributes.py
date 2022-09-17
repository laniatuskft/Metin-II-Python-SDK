import math

## Laniatus Games Studio Inc. | NOTE: Python has no need of forward class declarations:
#class CHARACTER

class CBuffOnAttributes:
    def __init__(self, pOwner, LG_POINT_type, p_vec_buff_wear_targets):
        #instance fields found by # Laniatus Games Studio Inc. |:
        self._m_pBuffOwner = None
        self._m_bPointType = 0
        self._m_bBuffValue = 0
        self._m_p_vec_buff_wear_targets = None
        self._m_map_additional_attrs = {}

        self._m_pBuffOwner = pOwner
        self._m_bPointType = LG_POINT_type
        self._m_p_vec_buff_wear_targets = p_vec_buff_wear_targets
        self.Initialize()

    def close(self):
        self.Off()

    def RemoveBuffFromItem(self, pItem):
        if 0 == self._m_bBuffValue:
            return
        if None is not pItem:
            if pItem.GetCell() < LGEMiscellaneous.INVENTORY_MAX_NUM:
                return
            it = find(self._m_p_vec_buff_wear_targets.begin(), self._m_p_vec_buff_wear_targets.end(), pItem.GetCell() - ushort(LGEMiscellaneous.INVENTORY_MAX_NUM))
            if self._m_p_vec_buff_wear_targets.end() is it:
                return

            m = pItem.GetAttributeCount()
            for j in range(0, m):
                attr = pItem.GetAttribute(j)
                it = self._m_map_additional_attrs.find(attr.bType)

                if it is not self._m_map_additional_attrs.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to value types:
#ORIGINAL METINII C CODE: int& sum_of_attr_value = it->second;
                    sum_of_attr_value = it.second
                    old_value = math.trunc(sum_of_attr_value * self._m_bBuffValue / float(100))
                    new_value = math.trunc((sum_of_attr_value - attr.sValue) * self._m_bBuffValue / float(100))
                    self._m_pBuffOwner.ApplyPoint(attr.bType, new_value - old_value)
                    sum_of_attr_value -= attr.sValue
                else:
                    #lani_err("Buff ERROR(type %d). This item(%d) attr_type(%d) was not in buff pool", self._m_bPointType, pItem.GetVnum(), attr.bType)
                    return

    def AddBuffFromItem(self, pItem):
        if 0 == self._m_bBuffValue:
            return
        if None is not pItem:
            if pItem.GetCell() < LGEMiscellaneous.INVENTORY_MAX_NUM:
                return
            it = find(self._m_p_vec_buff_wear_targets.begin(), self._m_p_vec_buff_wear_targets.end(), pItem.GetCell() - ushort(LGEMiscellaneous.INVENTORY_MAX_NUM))
            if self._m_p_vec_buff_wear_targets.end() is it:
                return

            m = pItem.GetAttributeCount()
            for j in range(0, m):
                attr = pItem.GetAttribute(j)
                it = self._m_map_additional_attrs.find(attr.bType)

                if it is self._m_map_additional_attrs.end():
                    self._m_pBuffOwner.ApplyPoint(attr.bType, math.trunc(attr.sValue * self._m_bBuffValue / float(100)))
                    self._m_map_additional_attrs.insert(TMapAttr.value_type(attr.bType, attr.sValue))
                else:
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to value types:
#ORIGINAL METINII C CODE: int& sum_of_attr_value = it->second;
                    sum_of_attr_value = it.second
                    old_value = math.trunc(sum_of_attr_value * self._m_bBuffValue / float(100))
                    new_value = math.trunc((sum_of_attr_value + attr.sValue) * self._m_bBuffValue / float(100))
                    self._m_pBuffOwner.ApplyPoint(attr.bType, new_value - old_value)
                    sum_of_attr_value += attr.sValue

    def ChangeBuffValue(self, bNewValue):
        if 0 == self._m_bBuffValue:
            self.On(bNewValue)
        elif 0 == bNewValue:
            self.Off()
        else:
            it = m_map_additional_attrs.begin()
            while it is not self._m_map_additional_attrs.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: Python does not have an equivalent to references to value types:
#ORIGINAL METINII C CODE: int& sum_of_attr_value = it->second;
                sum_of_attr_value = it.second
                old_value = math.trunc(sum_of_attr_value * self._m_bBuffValue / float(100))
                new_value = math.trunc(sum_of_attr_value * bNewValue / float(100))

                self._m_pBuffOwner.ApplyPoint(it.first, -math.trunc(sum_of_attr_value * self._m_bBuffValue / float(100)))
                it += 1
            self._m_bBuffValue = bNewValue

    def GiveAllAttributes(self):
        if 0 == self._m_bBuffValue:
            return
        it = m_map_additional_attrs.begin()
        while it is not self._m_map_additional_attrs.end():
            apply_type = it.first
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            apply_value = it.second * self._m_bBuffValue / 100

            self._m_pBuffOwner.ApplyPoint(apply_type, apply_value)
            it += 1

    def On(self, bValue):
        if 0 != self._m_bBuffValue or 0 == bValue:
            return LGEMiscellaneous.DEFINECONSTANTS.false

        n = len(self._m_p_vec_buff_wear_targets)
        self._m_map_additional_attrs.clear()
        for LaniatusDefVariables in range(0, n):
            pItem = self._m_pBuffOwner.GetWear(self._m_p_vec_buff_wear_targets[LaniatusDefVariables])
            if None is not pItem:
                m = pItem.GetAttributeCount()
                for j in range(0, m):
                    attr = pItem.GetAttribute(j)
                    it = self._m_map_additional_attrs.find(attr.bType)
                    if it is not self._m_map_additional_attrs.end():
                        it.second += attr.sValue
                    else:
                        self._m_map_additional_attrs.insert(TMapAttr.value_type(attr.bType, attr.sValue))

        it = m_map_additional_attrs.begin()
        while it is not self._m_map_additional_attrs.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            self._m_pBuffOwner.ApplyPoint(it.first, it.second * bValue / 100)
            it += 1

        self._m_bBuffValue = bValue

        return ((not LGEMiscellaneous.DEFINECONSTANTS.false))

    def Off(self):
        if 0 == self._m_bBuffValue:
            return

        it = m_map_additional_attrs.begin()
        while it is not self._m_map_additional_attrs.end():
## Laniatus Games Studio Inc. | ROLE FOR THE DEVELOPMENT DEPARTMENT: # Laniatus Games Studio Inc. | cannot determine whether both operands of this division are integer types - if they are then you should change 'lhs / rhs' to 'math.trunc(lhs / float(rhs))':
            self._m_pBuffOwner.ApplyPoint(it.first, -it.second * self._m_bBuffValue / 100)
            it += 1
        self.Initialize()

    def Initialize(self):
        self._m_bBuffValue = 0
        self._m_map_additional_attrs.clear()



