public class CPythonCharacterManager
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SCRIPT_SetAffect(uint dwVID, uint eState, bool isVisible)
	{
		CInstanceBase pkInstSel = (dwVID == 0xffffffff) ? GetSelectedInstancePtr() : GetInstancePtr(dwVID);
		if (pkInstSel == null)
		{
			return;
		}
    
		pkInstSel.SCRIPT_SetAffect(eState, isVisible ? true : false);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetEmoticon(uint dwVID, uint eState)
	{
		CInstanceBase pkInstSel = (dwVID == 0xffffffff) ? GetSelectedInstancePtr() : GetInstancePtr(dwVID);
		if (pkInstSel == null)
		{
			return;
		}
    
		pkInstSel.SetEmoticon(eState);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsPossibleEmoticon(uint dwVID)
	{
		CInstanceBase pkInstSel = (dwVID == 0xffffffff) ? GetSelectedInstancePtr() : GetInstancePtr(dwVID);
		if (pkInstSel == null)
		{
			return false;
		}
    
		return pkInstSel.IsPossibleEmoticon();
	}
}