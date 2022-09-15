public class CPythonEventManager
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __InitEventSet(TEventSet rEventSet)
	{
		rEventSet.ix = 0;
		rEventSet.iy = 0;
		rEventSet.iWidth = 0;
		rEventSet.iyLocal = 0;
    
		rEventSet.isLock = false;
		rEventSet.lLastDelayTime = 0;
		rEventSet.iCurrentLetter = 0;
		rEventSet.CurrentColor = D3DXCOLOR(1, 1, 1, 1);
		rEventSet.strCurrentLine = "";
    
		rEventSet.pCurrentTextLine = null;
		rEventSet.ScriptTextLineList.clear();
    
		rEventSet.isConfirmWait = false;
		rEventSet.pConfirmTimeTextLine = null;
		rEventSet.iConfirmEndTime = 0;
    
		rEventSet.DiffuseColor = D3DXCOLOR(1, 1, 1, 1);
		rEventSet.lWaitingTime = c_lNormal_Waiting_Time;
		rEventSet.iRestrictedCharacterCount = 30;
    
		rEventSet.iVisibleStartLine = 0;
		rEventSet.iVisibleLineCount = BOX_VISIBLE_LINE_COUNT;
    
		rEventSet.iAdjustLine = 0;
    
		rEventSet.isTextCenterMode = false;
		rEventSet.isWaitFlag = false;
    
		__InsertLine(rEventSet);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearEventSetp(TEventSet pEventSet)
	{
		if (pEventSet == null)
		{
			return;
		}
    
		for (TScriptTextLineList.iterator itor = pEventSet.ScriptTextLineList.begin(); itor != pEventSet.ScriptTextLineList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TTextLine & rkLine = *itor;
			TTextLine rkLine = *itor;
			rkLine.pInstance.Destroy();
			m_ScriptTextLinePool.Free(rkLine.pInstance);
		}
		pEventSet.ScriptTextLineList.clear();
    
		if (pEventSet.pCurrentTextLine)
		{
			pEventSet.pCurrentTextLine.Destroy();
			m_ScriptTextLinePool.Free(pEventSet.pCurrentTextLine);
		}
		pEventSet.pCurrentTextLine = null;
		pEventSet.strCurrentLine = "";
		pEventSet.iCurrentLetter = 0;
    
		m_EventSetPool.Free(pEventSet);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ProcessEventSet(TEventSet pEventSet)
	{
		if (pEventSet.isLock)
		{
			return;
		}
    
		SCmd ScriptCommand = new SCmd();
    
		IAbstractApplication rApp = IAbstractApplication.GetSingleton();
    
		if (!pEventSet.ScriptGroup.GetCmd(ScriptCommand))
		{
			pEventSet.isLock = true;
			return;
		}
    
		int pEventPosition;
		int iEventType;
		if (!GetScriptEventIndex(ScriptCommand.name.c_str(), pEventPosition, iEventType))
		{
			return;
		}
    
		switch (iEventType)
		{
			case EVENT_TYPE_LETTER:
			{
				string c_rstValue = GetArgumentString("value", ScriptCommand.argList);
				pEventSet.strCurrentLine.append(c_rstValue);
				pEventSet.pCurrentTextLine.SetValueString(pEventSet.strCurrentLine);
				pEventSet.pCurrentTextLine.SetColor(pEventSet.CurrentColor.r,pEventSet.CurrentColor.g,pEventSet.CurrentColor.b);
				pEventSet.iCurrentLetter += c_rstValue.Length;
    
				if (pEventSet.iCurrentLetter >= pEventSet.iRestrictedCharacterCount)
				{
					__InsertLine(pEventSet);
				}
    
				pEventSet.lLastDelayTime = pEventSet.lWaitingTime;
				break;
			}
    
			case EVENT_TYPE_DELAY:
			{
				if (EVENT_POSITION_START == pEventPosition)
				{
					pEventSet.lWaitingTime = atoi(GetArgument("value", ScriptCommand.argList));
				}
				else
				{
					pEventSet.lWaitingTime = c_lNormal_Waiting_Time;
				}
				break;
			}
    
			case EVENT_TYPE_COLOR:
			{
				if (EVENT_POSITION_START == pEventPosition)
				{
					pEventSet.CurrentColor.r = (float)atof(GetArgument("r", ScriptCommand.argList));
					pEventSet.CurrentColor.g = (float)atof(GetArgument("g", ScriptCommand.argList));
					pEventSet.CurrentColor.b = (float)atof(GetArgument("b", ScriptCommand.argList));
					pEventSet.CurrentColor.a = 1.0f;
				}
				else
				{
					pEventSet.CurrentColor.r = 1.0f;
					pEventSet.CurrentColor.g = 1.0f;
					pEventSet.CurrentColor.a = 1.0f;
					pEventSet.CurrentColor.b = 1.0f;
				}
				break;
			}
    
			case EVENT_TYPE_COLOR256:
			{
				if (EVENT_POSITION_START == pEventPosition)
				{
					pEventSet.CurrentColor.r = (float)(atof(GetArgument("r", ScriptCommand.argList)) / 255.0f);
					pEventSet.CurrentColor.g = (float)(atof(GetArgument("g", ScriptCommand.argList)) / 255.0f);
					pEventSet.CurrentColor.b = (float)(atof(GetArgument("b", ScriptCommand.argList)) / 255.0f);
					pEventSet.CurrentColor.a = 1.0f;
				}
				else
				{
					pEventSet.CurrentColor.r = 1.0f;
					pEventSet.CurrentColor.g = 1.0f;
					pEventSet.CurrentColor.a = 1.0f;
					pEventSet.CurrentColor.b = 1.0f;
				}
				break;
			}
    
			case EVENT_TYPE_ENTER:
			{
				__InsertLine(pEventSet);
				break;
			}
    
			case EVENT_TYPE_WAIT:
			{
				pEventSet.iyLocal = 0;
				pEventSet.isLock = true;
				break;
			}
    
			case EVENT_TYPE_NEXT:
			{
				MakeNextButton(pEventSet, BUTTON_TYPE_NEXT);
				pEventSet.iAdjustLine += 2;
				break;
			}
    
			case EVENT_TYPE_DONE:
			{
				MakeNextButton(pEventSet, BUTTON_TYPE_DONE);
				PyCallClassMemberFunc(pEventSet.poEventHandler, "DoneEvent", Py_BuildValue("()"));
				pEventSet.iAdjustLine += 2;
				break;
			}
    
			case EVENT_TYPE_CLEAR:
			{
				ClearLine(pEventSet);
				break;
			}
    
			case EVENT_TYPE_QUESTION:
			{
				MakeQuestion(pEventSet, ScriptCommand.argList);
				break;
			}
    
			case EVENT_TYPE_LEFT_IMAGE:
			{
				PyCallClassMemberFunc(pEventSet.poEventHandler, "OnLeftImage", Py_BuildValue("(s)", GetArgument("src", ScriptCommand.argList)));
				break;
			}
    
			case EVENT_TYPE_TOP_IMAGE:
			{
				PyCallClassMemberFunc(pEventSet.poEventHandler, "OnTopImage", Py_BuildValue("(s)", GetArgument("src", ScriptCommand.argList)));
				break;
			}
    
			case EVENT_TYPE_BACKGROUND_IMAGE:
			{
				PyCallClassMemberFunc(pEventSet.poEventHandler, "OnBackgroundImage", Py_BuildValue("(s)",GetArgument("src", ScriptCommand.argList)));
				break;
			}
    
			case EVENT_TYPE_IMAGE:
			{
				int x = atoi(GetArgument("x", ScriptCommand.argList));
				int y = atoi(GetArgument("y", ScriptCommand.argList));
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * src = GetArgument("src", ScriptCommand.argList);
				char src = GetArgument("src", ScriptCommand.argList);
    
				PyCallClassMemberFunc(pEventSet.poEventHandler, "OnImage", Py_BuildValue("(iis)", x, y, src));
				break;
			}
    
			case EVENT_TYPE_INSERT_IMAGE:
			{
				string imageFile = GetArgumentString("image_name", ScriptCommand.argList);
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * title = GetArgument("title", ScriptCommand.argList);
				char title = GetArgument("title", ScriptCommand.argList);
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * desc = GetArgument("desc", ScriptCommand.argList);
				char desc = GetArgument("desc", ScriptCommand.argList);
				int index = atoi(GetArgument("index", ScriptCommand.argList));
				int total = atoi(GetArgument("total", ScriptCommand.argList));
    
				if (string.IsNullOrEmpty(imageFile))
				{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * imageType = GetArgument("image_type", ScriptCommand.argList);
					char imageType = GetArgument("image_type", ScriptCommand.argList);
					int iItemIndex = atoi(GetArgument("idx", ScriptCommand.argList));
					PyCallClassMemberFunc(pEventSet.poEventHandler, "OnInsertItemIcon", Py_BuildValue("(sissii)", imageType, iItemIndex, title, desc, index, total));
				}
				else
				{
					PyCallClassMemberFunc(pEventSet.poEventHandler, "OnInsertImage", Py_BuildValue("(ssssii)", imageFile, title, title, desc, index, total));
				}
				pEventSet.iAdjustLine += 2;
				break;
			}
    
			case EVENT_TYPE_ADD_MAP_SIGNAL:
			{
				float x;
				float y;
				x = (float)atof(GetArgument("x",ScriptCommand.argList));
				y = (float)atof(GetArgument("y",ScriptCommand.argList));
				CPythonMiniMap.Instance().AddSignalPoint(x,y);
				CPythonMiniMap.Instance().OpenAtlasWindow();
				break;
			}
    
			case EVENT_TYPE_CLEAR_MAP_SIGNAL:
			{
				CPythonMiniMap.Instance().ClearAllSignalPoint();
				break;
			}
    
			case EVENT_TYPE_QUEST_BUTTON_CLOSE:
			{
				PyCallClassMemberFunc(m_poInterface, "BINARY_ClearQuest", Py_BuildValue("(i)", atoi(GetArgument("idx", ScriptCommand.argList))));
				break;
			}
    
			case EVENT_TYPE_QUEST_BUTTON:
			{
				string c_rstType = GetArgumentString("icon_type", ScriptCommand.argList);
				string c_rstFile = GetArgumentString("icon_name", ScriptCommand.argList);
    
				int idx = atoi(GetArgument("idx", ScriptCommand.argList));
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * name = GetArgument("name", ScriptCommand.argList);
				char name = GetArgument("name", ScriptCommand.argList);
    
				if (!strcmp(name, "?????? ??ȥ???...."))
				{
					PyCallClassMemberFunc(m_poInterface, "BINARY_RecvQuest", Py_BuildValue("(isss)", idx, name, "highlight", ""));
				}
				else
				{
					if (string.IsNullOrEmpty(c_rstFile))
					{
						PyCallClassMemberFunc(m_poInterface, "RecvQuest", Py_BuildValue("(is)", idx, name));
					}
					else
					{
						PyCallClassMemberFunc(m_poInterface, "BINARY_RecvQuest", Py_BuildValue("(isss)", idx, name, c_rstType, c_rstFile));
					}
				}
				break;
			}
			case EVENT_TYPE_SET_MESSAGE_POSITION:
			{
				break;
			}
			case EVENT_TYPE_ADJUST_MESSAGE_POSITION:
			{
				break;
			}
			case EVENT_TYPE_SET_CENTER_MAP_POSITION:
			{
				CPythonMiniMap.Instance().SetAtlasCenterPosition(atoi(GetArgument("x", ScriptCommand.argList)),atoi(GetArgument("y", ScriptCommand.argList)));
				break;
			}
			case EVENT_TYPE_SLEEP:
				pEventSet.lLastDelayTime = atoi(GetArgument("value", ScriptCommand.argList));
				break;
			case EVENT_TYPE_SET_CAMERA:
			{
				IAbstractApplication.SCameraSetting CameraSetting = new IAbstractApplication.SCameraSetting();
				GetCameraSettingFromArgList(ScriptCommand.argList, CameraSetting);
				rApp.SetEventCamera(CameraSetting);
				break;
			}
			case EVENT_TYPE_BLEND_CAMERA:
			{
				IAbstractApplication.SCameraSetting CameraSetting = new IAbstractApplication.SCameraSetting();
				GetCameraSettingFromArgList(ScriptCommand.argList, CameraSetting);
    
				float fBlendTime = atoi(GetArgument("blendtime", ScriptCommand.argList));
    
				rApp.BlendEventCamera(CameraSetting, fBlendTime);
				break;
			}
			case EVENT_TYPE_RESTORE_CAMERA:
			{
				rApp.SetDefaultCamera();
				break;
			}
			case EVENT_TYPE_FADE_OUT:
			{
				float fSpeed = (float)atof(GetArgument("speed", ScriptCommand.argList));
				PyCallClassMemberFunc(pEventSet.poEventHandler, "FadeOut", Py_BuildValue("(f)", fSpeed));
				pEventSet.isWaitFlag = true;
				break;
			}
			case EVENT_TYPE_FADE_IN:
			{
				PyCallClassMemberFunc(pEventSet.poEventHandler, "FadeIn", Py_BuildValue("(f)", atof(GetArgument("speed", ScriptCommand.argList))));
				pEventSet.isWaitFlag = true;
				break;
			}
			case EVENT_TYPE_WHITE_OUT:
			{
				PyCallClassMemberFunc(pEventSet.poEventHandler, "WhiteOut", Py_BuildValue("(f)", atof(GetArgument("speed", ScriptCommand.argList))));
				pEventSet.isWaitFlag = true;
				break;
			}
			case EVENT_TYPE_WHITE_IN:
			{
				PyCallClassMemberFunc(pEventSet.poEventHandler, "WhiteIn", Py_BuildValue("(f)", atof(GetArgument("speed", ScriptCommand.argList))));
				pEventSet.isWaitFlag = true;
				break;
			}
			case EVENT_TYPE_CLEAR_TEXT:
			{
				ClearLine(pEventSet);
				break;
			}
			case EVENT_TYPE_TEXT_HORIZONTAL_ALIGN_CENTER:
			{
				pEventSet.isTextCenterMode = true;
				if (pEventSet.pCurrentTextLine)
				{
					pEventSet.pCurrentTextLine.SetHorizonalAlign(CGraphicTextInstance.HORIZONTAL_ALIGN_CENTER);
				}
				break;
			}
			case EVENT_TYPE_TITLE_IMAGE:
			{
				PyCallClassMemberFunc(pEventSet.poEventHandler, "OnTitleImage", Py_BuildValue("(s)", GetArgument("src", ScriptCommand.argList)));
				break;
			}
			case EVENT_TYPE_DUNGEON_RESULT:
			{
				int killstone_count = atoi(GetArgument("killstone_count", ScriptCommand.argList));
				int killmob_count = atoi(GetArgument("killmob_count", ScriptCommand.argList));
				int find_hidden = atoi(GetArgument("find_hidden", ScriptCommand.argList));
				int hidden_total = atoi(GetArgument("hidden_total", ScriptCommand.argList));
				int use_potion = atoi(GetArgument("use_potion", ScriptCommand.argList));
				int is_revived = atoi(GetArgument("is_revived", ScriptCommand.argList));
				int killallmob = atoi(GetArgument("killallmob", ScriptCommand.argList));
				int total_time = atoi(GetArgument("total_time", ScriptCommand.argList));
				int bonus_exp = atoi(GetArgument("bonus_exp", ScriptCommand.argList));
    
				PyCallClassMemberFunc(m_poInterface, "ShowDungeonResult", Py_BuildValue("(iiiiiiiii)", killstone_count, killmob_count, find_hidden, hidden_total, use_potion, is_revived, killallmob, total_time, bonus_exp));
				break;
			}
			case EVENT_TYPE_ITEM_NAME:
			{
				int iIndex = atoi(GetArgument("value", ScriptCommand.argList));
				CItemData pItemData;
				if (CItemManager.Instance().GetItemDataPointer(iIndex, pItemData))
				{
					pEventSet.strCurrentLine.append(pItemData.GetName());
					pEventSet.pCurrentTextLine.SetValue(pEventSet.strCurrentLine.c_str());
					pEventSet.pCurrentTextLine.SetColor(1.0f, 0.2f, 0.2f);
					pEventSet.iCurrentLetter += strlen(pItemData.GetName());
    
					if (pEventSet.iCurrentLetter >= pEventSet.iRestrictedCharacterCount)
					{
						__InsertLine(pEventSet);
					}
    
					pEventSet.lLastDelayTime = pEventSet.lWaitingTime;
				}
    
				break;
			}
			case EVENT_TYPE_MONSTER_NAME:
			{
				int iIndex = atoi(GetArgument("value", ScriptCommand.argList));
				string c_szName;
    
				CPythonNonPlayer rkNonPlayer = CPythonNonPlayer.Instance();
				if (rkNonPlayer.GetName(iIndex, c_szName))
				{
					pEventSet.strCurrentLine.append(c_szName);
					pEventSet.pCurrentTextLine.SetValue(pEventSet.strCurrentLine.c_str());
					pEventSet.iCurrentLetter += strlen(c_szName);
    
					if (pEventSet.iCurrentLetter >= pEventSet.iRestrictedCharacterCount)
					{
						__InsertLine(pEventSet);
					}
    
					pEventSet.lLastDelayTime = pEventSet.lWaitingTime;
				}
    
				break;
			}
			case EVENT_TYPE_WINDOW_SIZE:
			{
				int iWidth = atoi(GetArgument("width", ScriptCommand.argList));
				int iHeight = atoi(GetArgument("height", ScriptCommand.argList));
				PyCallClassMemberFunc(pEventSet.poEventHandler, "OnSize", Py_BuildValue("(ii)", iWidth, iHeight));
				break;
			}
			case EVENT_TYPE_INPUT:
			{
				__InsertLine(pEventSet);
				PyCallClassMemberFunc(pEventSet.poEventHandler, "OnInput", Py_BuildValue("()"));
				break;
			}
			case EVENT_TYPE_CONFIRM_WAIT:
			{
				int iTimeOut = atoi(GetArgument("timeout", ScriptCommand.argList));
				pEventSet.isConfirmWait = true;
				pEventSet.pConfirmTimeTextLine = pEventSet.pCurrentTextLine;
				pEventSet.iConfirmEndTime = timeGetTime() / 1000 + iTimeOut;
				__InsertLine(pEventSet, true);
				MakeNextButton(pEventSet, BUTTON_TYPE_CANCEL);
				break;
			}
			case EVENT_TYPE_END_CONFIRM_WAIT:
			{
				for (uint LaniatusDefVariables = 0; LaniatusDefVariables < m_EventSetVector.size(); ++i)
				{
					if (null == m_EventSetVector[i])
					{
						continue;
					}
    
					TEventSet pSet = m_EventSetVector[i];
					if (!pSet.isConfirmWait)
					{
						continue;
					}
    
					pSet.isConfirmWait = false;
					pSet.pConfirmTimeTextLine = null;
					pSet.iConfirmEndTime = 0;
    
					PyCallClassMemberFunc(pSet.poEventHandler, "CloseSelf", Py_BuildValue("()"));
				}
				break;
			}
			case EVENT_TYPE_SELECT_ITEM:
			{
				PyCallClassMemberFunc(m_poInterface, "BINARY_OpenSelectItemWindow", Py_BuildValue("()"));
				break;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MakeNextButton(TEventSet pEventSet, int iButtonType)
	{
		__AddSpace(pEventSet, c_fLine_Temp + 5);
		PyCallClassMemberFunc(pEventSet.poEventHandler, "MakeNextButton", Py_BuildValue("(i)", iButtonType));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void MakeQuestion(TEventSet pEventSet, LinkedList<SArgumet> rArgumentList)
	{
		if (rArgumentList.Count == 0)
		{
			return;
		}
    
		PyCallClassMemberFunc(pEventSet.poEventHandler, "MakeQuestion", Py_BuildValue("(i)", rArgumentList.Count));
		pEventSet.nAnswer = rArgumentList.Count;
    
		int iIndex = 0;
		for (LinkedList<SArgumet>.Enumerator itor = rArgumentList.GetEnumerator(); itor.MoveNext();)
		{
			SArgumet rArgument = itor.Current;
			PyCallClassMemberFunc(pEventSet.poEventHandler, "AppendQuestion", Py_BuildValue("(si)", rArgument.strValue.c_str(), iIndex));
			++iIndex;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ClearLine(TEventSet pEventSet)
	{
		if (pEventSet == null)
		{
			return;
		}
    
		for (TScriptTextLineList.iterator itor = pEventSet.ScriptTextLineList.begin(); itor != pEventSet.ScriptTextLineList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TTextLine & rkLine = *itor;
			TTextLine rkLine = *itor;
			CGraphicTextInstance pInstance = rkLine.pInstance;
			pInstance.Destroy();
			pInstance.Update();
		}
    
		pEventSet.pCurrentTextLine.Destroy();
		pEventSet.pCurrentTextLine.Update();
    
		pEventSet.pCurrentTextLine = null;
		pEventSet.ScriptTextLineList.clear();
    
		__InsertLine(pEventSet);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __InsertLine(TEventSet rEventSet, bool isCenter, int iX_pos)
	{
		if (rEventSet.pCurrentTextLine)
		{
			TTextLine kLine = new TTextLine();
			if (CGraphicTextInstance.HORIZONTAL_ALIGN_CENTER == rEventSet.pCurrentTextLine.GetHorizontalAlign())
			{
				kLine.ixLocal = rEventSet.iWidth / 2;
				kLine.iyLocal = rEventSet.iyLocal;
    
			}
			else
			{
				int textWidth;
				int textHeight;
				rEventSet.pCurrentTextLine.GetTextSize(textWidth, textHeight);
				if (GetDefaultCodePage() == CP_1256)
				{
					kLine.ixLocal = rEventSet.iWidth;
					if (iX_pos != 0)
					{
						kLine.ixLocal -= iX_pos - 20;
						kLine.ixLocal += textWidth / 2;
					}
				}
				else
				{
					kLine.ixLocal = 0;
					if (iX_pos != 0)
					{
						kLine.ixLocal += (iX_pos - 20);
						kLine.ixLocal -= textWidth / 2;
					}
				}
    
				kLine.iyLocal = rEventSet.iyLocal;
			}
			kLine.pInstance = rEventSet.pCurrentTextLine;
			rEventSet.ScriptTextLineList.push_back(kLine);
			__AddSpace(rEventSet, c_fLine_Temp);
		}
    
		CGraphicText pkDefaultFont = (CGraphicText)DefaultFont_GetResource();
		if (pkDefaultFont == null)
		{
			TraceError("CPythonEventManager::InsertLine - CANNOT_FIND_DEFAULT_FONT");
			return;
		}
    
		rEventSet.pCurrentTextLine = m_ScriptTextLinePool.Alloc();
		if (!rEventSet.pCurrentTextLine)
		{
			TraceError("CPythonEventManager::InsertLine - OUT_OF_TEXT_LINE");
			return;
		}
    
		rEventSet.pCurrentTextLine.SetTextPointer(pkDefaultFont);
		rEventSet.pCurrentTextLine.SetColor(1.0f, 1.0f, 1.0f);
		rEventSet.pCurrentTextLine.SetValue("");
    
		if (rEventSet.isTextCenterMode || isCenter)
		{
			rEventSet.pCurrentTextLine.SetHorizonalAlign(CGraphicTextInstance.HORIZONTAL_ALIGN_CENTER);
			rEventSet.pCurrentTextLine.SetPosition(rEventSet.ix + rEventSet.iWidth / 2, rEventSet.iy + rEventSet.iyLocal);
		}
		else
		{
			if (GetDefaultCodePage() == CP_1256)
			{
				rEventSet.pCurrentTextLine.SetHorizonalAlign(CGraphicTextInstance.HORIZONTAL_ALIGN_LEFT);
				rEventSet.pCurrentTextLine.SetPosition(rEventSet.ix + rEventSet.iWidth, rEventSet.iy + rEventSet.iyLocal);
			}
			else
			{
				rEventSet.pCurrentTextLine.SetHorizonalAlign(CGraphicTextInstance.HORIZONTAL_ALIGN_LEFT);
				rEventSet.pCurrentTextLine.SetPosition(rEventSet.ix, rEventSet.iy + rEventSet.iyLocal);
			}
		}
    
		rEventSet.iCurrentLetter = 0;
		rEventSet.strCurrentLine = "";
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RefreshLinePosition(TEventSet pEventSet)
	{
		for (TScriptTextLineList.iterator itor = pEventSet.ScriptTextLineList.begin(); itor != pEventSet.ScriptTextLineList.end(); ++itor)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: TTextLine & rkLine = *itor;
			TTextLine rkLine = *itor;
			CGraphicTextInstance pInstance = rkLine.pInstance;
			pInstance.SetPosition(pEventSet.ix + rkLine.ixLocal, pEventSet.iy + rkLine.iyLocal);
		}
    
		int ixTextPos;
		if (CGraphicTextInstance.HORIZONTAL_ALIGN_CENTER == pEventSet.pCurrentTextLine.GetHorizontalAlign())
		{
			ixTextPos = pEventSet.ix + pEventSet.iWidth / 2;
		}
		else
		{
			if (GetDefaultCodePage() == CP_1256)
			{
				ixTextPos = pEventSet.ix + pEventSet.iWidth;
			}
			else
			{
				ixTextPos = pEventSet.ix;
			}
		}
		pEventSet.pCurrentTextLine.SetPosition(ixTextPos, pEventSet.iy + pEventSet.iyLocal);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __AddSpace(TEventSet rEventSet, int iSpace)
	{
		rEventSet.iyLocal += iSpace;
	}
}