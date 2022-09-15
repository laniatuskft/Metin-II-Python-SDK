public class CItemData
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetItemTableData(TItemTable pItemTable)
	{
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(m_ItemTable, pItemTable, sizeof(TItemTable));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetLimit(byte byIndex, TItemLimit pItemLimit)
	{
		if (byIndex >= ITEM_LIMIT_MAX_NUM)
		{
			Debug.Assert(byIndex < ITEM_LIMIT_MAX_NUM);
			return false;
		}
    
		pItemLimit = m_ItemTable.aLimits[byIndex];
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetApply(byte byIndex, TItemApply pItemApply)
	{
		if (byIndex >= ITEM_APPLY_MAX_NUM)
		{
			Debug.Assert(byIndex < ITEM_APPLY_MAX_NUM);
			return false;
		}
    
		pItemApply = m_ItemTable.aApplies[byIndex];
		return true;
	}
}