public class CSlotWindow
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ClearSlot(TSlot pSlot)
	{
		pSlot.bActive = false;
		pSlot.byxPlacedItemSize = 1;
		pSlot.byyPlacedItemSize = 1;
    
		pSlot.isItem = false;
		pSlot.dwState = 0;
		pSlot.fCoolTime = 0.0f;
		pSlot.fStartCoolTime = 0.0f;
		pSlot.dwCenterSlotNumber = 0xffffffff;
    
		pSlot.dwItemIndex = 0;
		pSlot.bRenderBaseSlotImage = true;
    
		if (pSlot.pInstance)
		{
			CGraphicImageInstance.Delete(pSlot.pInstance);
			pSlot.pInstance = null;
		}
		if (pSlot.pCoverButton)
		{
			pSlot.pCoverButton.Hide();
		}
		if (pSlot.pSlotButton)
		{
			pSlot.pSlotButton.Hide();
		}
		if (pSlot.pSignImage)
		{
			 pSlot.pSignImage.Hide();
		}
		if (pSlot.pFinishCoolTimeEffect)
		{
			pSlot.pFinishCoolTimeEffect.Hide();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetSlotPointer(uint dwIndex, TSlot[] ppSlot)
	{
		for (TSlotListIterator itor = m_SlotList.begin(); itor != m_SlotList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TSlot & rSlot = *itor;
			TSlot rSlot = *itor;
    
			if (dwIndex == rSlot.dwSlotNumber)
			{
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *ppSlot = &rSlot;
				ppSlot[0].CopyFrom(rSlot);
				return true;
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetSelectedSlotPointer(TSlot[] ppSlot)
	{
		int lx;
		int ly;
		GetMouseLocalPosition(lx, ly);
    
		for (TSlotListIterator itor = m_SlotList.begin(); itor != m_SlotList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TSlot & rSlot = *itor;
			TSlot rSlot = *itor;
    
			if (lx >= rSlot.ixPosition)
			{
			if (ly >= rSlot.iyPosition)
			{
			if (lx <= rSlot.ixPosition + rSlot.ixCellSize)
			{
			if (ly <= rSlot.iyPosition + rSlot.iyCellSize)
			{
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *ppSlot = &rSlot;
				ppSlot[0].CopyFrom(rSlot);
				return true;
			}
			}
			}
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool GetPickedSlotPointer(TSlot[] ppSlot)
	{
		int lx;
		int ly;
		CWindowManager.Instance().GetMousePosition(lx, ly);
    
		int ixLocal = lx - m_rect.left;
		int iyLocal = ly - m_rect.top;
    
		for (TSlotListIterator itor = m_SlotList.begin(); itor != m_SlotList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TSlot & rSlot = *itor;
			TSlot rSlot = *itor;
    
			int ixCellSize = rSlot.ixCellSize;
			int iyCellSize = rSlot.iyCellSize;
    
			if (rSlot.isItem)
			{
				ixCellSize = Math.Max(rSlot.ixCellSize, (int)(rSlot.byxPlacedItemSize * ITEM_WIDTH));
				iyCellSize = Math.Max(rSlot.iyCellSize, (int)(rSlot.byyPlacedItemSize * ITEM_HEIGHT));
			}
    
			if (ixLocal >= rSlot.ixPosition)
			{
			if (iyLocal >= rSlot.iyPosition)
			{
			if (ixLocal <= rSlot.ixPosition + ixCellSize)
			{
			if (iyLocal <= rSlot.iyPosition + iyCellSize)
			{
	//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
	//Original Metin2 CPlus Line: *ppSlot = &rSlot;
				ppSlot[0].CopyFrom(rSlot);
				return true;
			}
			}
			}
			}
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __CreateFinishCoolTimeEffect(TSlot pSlot)
	{
		__DestroyFinishCoolTimeEffect(pSlot);
    
		CAniImageBox pFinishCoolTimeEffect = new CCoolTimeFinishEffect(this, pSlot.dwSlotNumber);
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/00.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/01.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/02.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/03.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/04.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/05.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/06.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/07.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/08.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/09.sub");
		pFinishCoolTimeEffect.AppendImage("t:/laniaworkstate/uinterface/public/slotfinishcooltimeeffect/10.sub");
		pFinishCoolTimeEffect.SetRenderingMode(CGraphicExpandedImageInstance.RENDERING_MODE_SCREEN);
		pFinishCoolTimeEffect.ResetFrame();
		pFinishCoolTimeEffect.SetDelay(2);
		pFinishCoolTimeEffect.Show();
    
		pSlot.pFinishCoolTimeEffect = pFinishCoolTimeEffect;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __DestroyFinishCoolTimeEffect(TSlot pSlot)
	{
		if (pSlot.pFinishCoolTimeEffect)
		{
			pSlot.pFinishCoolTimeEffect = null;
			pSlot.pFinishCoolTimeEffect = null;
		}
	}
}