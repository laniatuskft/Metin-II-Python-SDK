public class CPythonNetworkStream
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool ClientCommand(string c_szCommand)
	{
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ServerCommand(ref string c_szCommand)
	{
		if (strcmpi(c_szCommand, "ConsoleEnable") == 0)
		{
			return;
		}
    
		if (m_apoPhaseWnd[PHASE_WINDOW_GAME])
		{
			bool isTrue;
			if (PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_ServerCommand_Run", Py_BuildValue("(s)", c_szCommand), isTrue))
			{
				if (isTrue)
				{
					return;
				}
			}
		}
		else if (m_poSerCommandParserWnd)
		{
			bool isTrue;
			if (PyCallClassMemberFunc(m_poSerCommandParserWnd, "BINARY_ServerCommand_Run", Py_BuildValue("(s)", c_szCommand), isTrue))
			{
				if (isTrue)
				{
					return;
				}
			}
		}
    
		CTokenVector TokenVector = new CTokenVector();
		if (!SplitToken(c_szCommand, TokenVector))
		{
			return;
		}
		if (TokenVector.empty())
		{
			return;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * szCmd = TokenVector[0].c_str();
		char szCmd = TokenVector[0].c_str();
    
		if (!strcmpi(szCmd, "quit"))
		{
			PostQuitMessage(0);
		}
		else if (!strcmpi(szCmd, "BettingMoney"))
		{
			if (2 != TokenVector.size())
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
		}
    
		else if (!strcmpi(szCmd, "gift"))
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "Gift_Show", Py_BuildValue("()"));
		}
    
		else if (!strcmpi(szCmd, "cube"))
		{
			if (TokenVector.size() < 2)
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
    
			if ("open" == TokenVector[1])
			{
				if (3 > TokenVector.size())
				{
					TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
					return;
				}
    
				uint npcVNUM = (uint)atoi(TokenVector[2].c_str());
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_Open", Py_BuildValue("(i)", npcVNUM));
			}
			else if ("close" == TokenVector[1])
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_Close", Py_BuildValue("()"));
			}
			else if ("info" == TokenVector[1])
			{
				if (5 != TokenVector.size())
				{
					TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
					return;
				}
    
				uint gold = atoi(TokenVector[2].c_str());
				uint itemVnum = atoi(TokenVector[3].c_str());
				uint count = atoi(TokenVector[4].c_str());
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_UpdateInfo", Py_BuildValue("(iii)", gold, itemVnum, count));
			}
			else if ("success" == TokenVector[1])
			{
				if (4 != TokenVector.size())
				{
					TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
					return;
				}
    
				uint itemVnum = atoi(TokenVector[2].c_str());
				uint count = atoi(TokenVector[3].c_str());
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_Succeed", Py_BuildValue("(ii)", itemVnum, count));
			}
			else if ("fail" == TokenVector[1])
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_Failed", Py_BuildValue("()"));
			}
			else if ("r_list" == TokenVector[1])
			{
				if (5 != TokenVector.size())
				{
					TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %d", c_szCommand, 5);
					return;
				}
    
				uint npcVNUM = (uint)atoi(TokenVector[2].c_str());
    
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_ResultList", Py_BuildValue("(is)", npcVNUM, TokenVector[4].c_str()));
			}
			else if ("m_info" == TokenVector[1])
			{
				if (5 != TokenVector.size())
				{
					TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %d", c_szCommand, 5);
					return;
				}
    
				uint requestStartIndex = (uint)atoi(TokenVector[2].c_str());
				uint resultCount = (uint)atoi(TokenVector[3].c_str());
    
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Cube_MaterialInfo", Py_BuildValue("(iis)", requestStartIndex, resultCount, TokenVector[4].c_str()));
			}
		}
    
		else if (!strcmpi(szCmd, "acce"))
		{
			if (TokenVector.size() < 2)
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
    
			if ("open" == TokenVector[1])
			{
				if (3 > TokenVector.size())
				{
					TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
					return;
				}
    
				byte window = 0;
    
				if ("combine" == TokenVector[2])
				{
					window = 1;
				}
    
				if ("absorb" == TokenVector[2])
				{
					window = 0;
				}
    
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Acce_Open", Py_BuildValue("(i)", window));
			}
    
			else if ("close" == TokenVector[1])
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Acce_Close", Py_BuildValue("()"));
			}
		}
		else if (!strcmpi(szCmd, "ObserverCount"))
		{
			if (2 != TokenVector.size())
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
    
			uint uObserverCount = atoi(TokenVector[1].c_str());
    
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_BettingGuildWar_UpdateObserverCount", Py_BuildValue("(i)", uObserverCount));
		}
		else if (!strcmpi(szCmd, "ObserverMode"))
		{
			if (2 != TokenVector.size())
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
    
			uint uMode = atoi(TokenVector[1].c_str());
    
			IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
			rkPlayer.SetObserverMode(uMode != 0 ? true : false);
    
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_BettingGuildWar_SetObserverMode", Py_BuildValue("(i)", uMode));
		}
		else if (!strcmpi(szCmd, "ObserverTeamInfo"))
		{
		}
		else if (!strcmpi(szCmd, "StoneDetect"))
		{
			if (4 != TokenVector.size())
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
    
			uint dwVID = atoi(TokenVector[1].c_str());
			byte byDistance = atoi(TokenVector[2].c_str());
			float fAngle = atof(TokenVector[3].c_str());
			fAngle = fmod(540.0f - fAngle, 360.0f);
			Tracef("StoneDetect [VID:%d] [Distance:%d] [Angle:%d->%f]\n", dwVID, byDistance, atoi(TokenVector[3].c_str()), fAngle);
    
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
    
			CInstanceBase pInstance = rkChrMgr.GetInstancePtr(dwVID);
			if (pInstance == null)
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Not Exist Instance", c_szCommand);
				return;
			}
    
			TPixelPosition PixelPosition = new TPixelPosition();
			_D3DVECTOR v3Rotation = new _D3DVECTOR(0.0f, 0.0f, fAngle);
			pInstance.NEW_GetPixelPosition(PixelPosition);
    
			PixelPosition.y *= -1.0f;
    
			switch (byDistance)
			{
				case 0:
					CEffectManager.Instance().RegisterEffect("t:/laniaworkstate/effect/etc/firecracker/find_out.mse");
					CEffectManager.Instance().CreateEffect("t:/laniaworkstate/effect/etc/firecracker/find_out.mse", PixelPosition, v3Rotation);
					break;
				case 1:
					CEffectManager.Instance().RegisterEffect("t:/laniaworkstate/effect/etc/compass/appear_small.mse");
					CEffectManager.Instance().CreateEffect("t:/laniaworkstate/effect/etc/compass/appear_small.mse", PixelPosition, v3Rotation);
					break;
				case 2:
					CEffectManager.Instance().RegisterEffect("t:/laniaworkstate/effect/etc/compass/appear_middle.mse");
					CEffectManager.Instance().CreateEffect("t:/laniaworkstate/effect/etc/compass/appear_middle.mse", PixelPosition, v3Rotation);
					break;
				case 3:
					CEffectManager.Instance().RegisterEffect("t:/laniaworkstate/effect/etc/compass/appear_large.mse");
					CEffectManager.Instance().CreateEffect("t:/laniaworkstate/effect/etc/compass/appear_large.mse", PixelPosition, v3Rotation);
					break;
				default:
					TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Distance", c_szCommand);
					break;
			}
    
	#if DEBUG
			IAbstractChat rkChat = IAbstractChat.GetSingleton();
			rkChat.AppendChat(CHAT_TYPE_INFO, c_szCommand);
	#endif
		}
		else if (!strcmpi(szCmd, "StartStaminaConsume"))
		{
			if (3 != TokenVector.size())
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %s", c_szCommand);
				return;
			}
    
			uint dwConsumePerSec = atoi(TokenVector[1].c_str());
			uint dwCurrentStamina = atoi(TokenVector[2].c_str());
    
			IAbstractPlayer rPlayer = IAbstractPlayer.GetSingleton();
			rPlayer.StartStaminaConsume(dwConsumePerSec, dwCurrentStamina);
		}
    
		else if (!strcmpi(szCmd, "StopStaminaConsume"))
		{
			if (2 != TokenVector.size())
			{
				TraceError("CPythonNetworkStream::ServerCommand(c_szCommand=%s) - Strange Parameter Count : %d", c_szCommand, TokenVector.size());
				return;
			}
    
			uint dwCurrentStamina = atoi(TokenVector[1].c_str());
    
			IAbstractPlayer rPlayer = IAbstractPlayer.GetSingleton();
			rPlayer.StopStaminaConsume(dwCurrentStamina);
		}
		else if (!strcmpi(szCmd, "messenger_auth"))
		{
			string c_rstrName = TokenVector[1].c_str();
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnMessengerAddFriendQuestion", Py_BuildValue("(s)", c_rstrName));
		}
		else if (!strcmpi(szCmd, "combo"))
		{
			int iFlag = atoi(TokenVector[1].c_str());
			IAbstractPlayer rPlayer = IAbstractPlayer.GetSingleton();
			rPlayer.SetComboSkillFlag(iFlag);
			m_bComboSkillFlag = iFlag != 0 ? true : false;
		}
		else if (!strcmpi(szCmd, "setblockmode"))
		{
			int iFlag = atoi(TokenVector[1].c_str());
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnBlockMode", Py_BuildValue("(i)", iFlag));
		}
    
		else if (!strcmpi(szCmd, "french_kiss"))
		{
			int iVID1 = atoi(TokenVector[1].c_str());
			int iVID2 = atoi(TokenVector[2].c_str());
    
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance1 = rkChrMgr.GetInstancePtr(iVID1);
			CInstanceBase pInstance2 = rkChrMgr.GetInstancePtr(iVID2);
			if (pInstance1 != null && pInstance2 != null)
			{
				pInstance1.ActDualEmotion(pInstance2, CRaceMotionData.NAME_FRENCH_KISS_START, CRaceMotionData.NAME_FRENCH_KISS_START);
			}
		}
		else if (!strcmpi(szCmd, "kiss"))
		{
			int iVID1 = atoi(TokenVector[1].c_str());
			int iVID2 = atoi(TokenVector[2].c_str());
    
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance1 = rkChrMgr.GetInstancePtr(iVID1);
			CInstanceBase pInstance2 = rkChrMgr.GetInstancePtr(iVID2);
			if (pInstance1 != null && pInstance2 != null)
			{
				pInstance1.ActDualEmotion(pInstance2, CRaceMotionData.NAME_KISS_START, CRaceMotionData.NAME_KISS_START);
			}
		}
		else if (!strcmpi(szCmd, "slap"))
		{
			int iVID1 = atoi(TokenVector[1].c_str());
			int iVID2 = atoi(TokenVector[2].c_str());
    
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance1 = rkChrMgr.GetInstancePtr(iVID1);
			CInstanceBase pInstance2 = rkChrMgr.GetInstancePtr(iVID2);
			if (pInstance1 != null && pInstance2 != null)
			{
				pInstance1.ActDualEmotion(pInstance2, CRaceMotionData.NAME_SLAP_HURT_START, CRaceMotionData.NAME_SLAP_HIT_START);
			}
		}
		else if (!strcmpi(szCmd, "clap"))
		{
			int iVID = atoi(TokenVector[1].c_str());
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance = rkChrMgr.GetInstancePtr(iVID);
			if (pInstance != null)
			{
				pInstance.ActEmotion(CRaceMotionData.NAME_CLAP);
			}
		}
		else if (!strcmpi(szCmd, "cheer1"))
		{
			int iVID = atoi(TokenVector[1].c_str());
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance = rkChrMgr.GetInstancePtr(iVID);
			if (pInstance != null)
			{
				pInstance.ActEmotion(CRaceMotionData.NAME_CHEERS_1);
			}
		}
		else if (!strcmpi(szCmd, "cheer2"))
		{
			int iVID = atoi(TokenVector[1].c_str());
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance = rkChrMgr.GetInstancePtr(iVID);
			if (pInstance != null)
			{
				pInstance.ActEmotion(CRaceMotionData.NAME_CHEERS_2);
			}
		}
		else if (!strcmpi(szCmd, "dance1"))
		{
			int iVID = atoi(TokenVector[1].c_str());
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance = rkChrMgr.GetInstancePtr(iVID);
			if (pInstance != null)
			{
				pInstance.ActEmotion(CRaceMotionData.NAME_DANCE_1);
			}
		}
		else if (!strcmpi(szCmd, "dance2"))
		{
			int iVID = atoi(TokenVector[1].c_str());
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance = rkChrMgr.GetInstancePtr(iVID);
			if (pInstance != null)
			{
				pInstance.ActEmotion(CRaceMotionData.NAME_DANCE_2);
			}
		}
		else if (!strcmpi(szCmd, "dig_motion"))
		{
			int iVID = atoi(TokenVector[1].c_str());
			IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
			CInstanceBase pInstance = rkChrMgr.GetInstancePtr(iVID);
			if (pInstance != null)
			{
				pInstance.ActEmotion(CRaceMotionData.NAME_DIG);
			}
		}
		else
		{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static System.Collections.Generic.SortedDictionary<string, int> s_emotionDict;
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//		static bool s_isFirst = true;
			if (ServerCommand_s_isFirst)
			{
				ServerCommand_s_isFirst = false;
    
				ServerCommand_s_emotionDict["dance3"] = CRaceMotionData.NAME_DANCE_3;
				ServerCommand_s_emotionDict["dance4"] = CRaceMotionData.NAME_DANCE_4;
				ServerCommand_s_emotionDict["dance5"] = CRaceMotionData.NAME_DANCE_5;
				ServerCommand_s_emotionDict["dance6"] = CRaceMotionData.NAME_DANCE_6;
				ServerCommand_s_emotionDict["congratulation"] = CRaceMotionData.NAME_CONGRATULATION;
				ServerCommand_s_emotionDict["forgive"] = CRaceMotionData.NAME_FORGIVE;
				ServerCommand_s_emotionDict["angry"] = CRaceMotionData.NAME_ANGRY;
				ServerCommand_s_emotionDict["attractive"] = CRaceMotionData.NAME_ATTRACTIVE;
				ServerCommand_s_emotionDict["sad"] = CRaceMotionData.NAME_SAD;
				ServerCommand_s_emotionDict["shy"] = CRaceMotionData.NAME_SHY;
				ServerCommand_s_emotionDict["cheerup"] = CRaceMotionData.NAME_CHEERUP;
				ServerCommand_s_emotionDict["banter"] = CRaceMotionData.NAME_BANTER;
				ServerCommand_s_emotionDict["joy"] = CRaceMotionData.NAME_JOY;
			}
    
			SortedDictionary<string, int>.Enumerator f = ServerCommand_s_emotionDict.find(szCmd);
			if (f == ServerCommand_s_emotionDict.end())
			{
				TraceError("Unknown Server Command %s | %s", c_szCommand, szCmd);
			}
			else
			{
	//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
				int emotionIndex = f.second;
    
				int iVID = atoi(TokenVector[1].c_str());
				IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
				CInstanceBase pInstance = rkChrMgr.GetInstancePtr(iVID);
    
				if (pInstance != null)
				{
					pInstance.ActEmotion(emotionIndex);
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnRemoteDisconnect()
	{
		PyCallClassMemberFunc(m_poHandler, "SetLoginPhase", Py_BuildValue("()"));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnDisconnect()
	{
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnScriptEventStart(int iSkin, int iIndex)
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OpenQuestWindow", Py_BuildValue("(ii)", iSkin, iIndex));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshAlignmentWindow()
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshAlignment", Py_BuildValue("()"));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshTargetBoardByVID(uint dwVID)
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshTargetBoardByVID", Py_BuildValue("(i)", dwVID));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshTargetBoardByName(string c_szName)
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshTargetBoardByName", Py_BuildValue("(s)", c_szName));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshTargetBoard()
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshTargetBoard", Py_BuildValue("()"));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshGuildWindowGradePage()
	{
		m_isRefreshGuildWndGradePage = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshGuildWindowSkillPage()
	{
		m_isRefreshGuildWndSkillPage = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshGuildWindowMemberPageGradeComboBox()
	{
		m_isRefreshGuildWndMemberPageGradeComboBox = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshGuildWindowMemberPage()
	{
		m_isRefreshGuildWndMemberPage = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshGuildWindowBoardPage()
	{
		m_isRefreshGuildWndBoardPage = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshGuildWindowInfoPage()
	{
		m_isRefreshGuildWndInfoPage = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshMessengerWindow()
	{
		m_isRefreshMessengerWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshSafeboxWindow()
	{
		m_isRefreshSafeboxWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshMallWindow()
	{
		m_isRefreshMallWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshSkillWindow()
	{
		m_isRefreshSkillWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshExchangeWindow()
	{
		m_isRefreshExchangeWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshStatus()
	{
		m_isRefreshStatus = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshCharacterWindow()
	{
		m_isRefreshCharacterWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshInventoryWindow()
	{
		m_isRefreshInventoryWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshAcceWindow()
	{
		m_isRefreshAcceWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RefreshEquipmentWindow()
	{
		m_isRefreshEquipmentWnd = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetGuildID(uint id)
	{
		if (m_dwGuildID != id)
		{
			m_dwGuildID = id;
			IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
    
			for (int LaniatusDefVariables = 0; LaniatusDefVariables < PLAYER_PER_ACCOUNT4; ++i)
			{
				if (!strncmp(m_akSimplePlayerInfo[LaniatusDefVariables].szName, rkPlayer.GetName(), DefineConstants.CHARACTER_NAME_MAX_LEN))
				{
					m_adwGuildID[LaniatusDefVariables] = id;
    
					string guildName = "";
					if (CPythonGuild.Instance().GetGuildName(id, guildName))
					{
						m_astrGuildName[LaniatusDefVariables] = guildName;
					}
					else
					{
						m_astrGuildName[LaniatusDefVariables] = "";
					}
				}
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void GamePhase()
	{
		if (!m_kQue_stHack.empty())
		{
			__SendHack(m_kQue_stHack.front().c_str());
			m_kQue_stHack.pop_front();
		}
    
		byte header = 0;
		bool ret = true;
    
		const uint MAX_RECV_COUNT = 8;
		const uint SAFE_RECV_BUFSIZE = 8192;
		uint dwRecvCount = 0;
    
		while (ret)
		{
			if (dwRecvCount++ >= MAX_RECV_COUNT - 1 && GetRecvBufferSize() < SAFE_RECV_BUFSIZE && m_strPhase == "Game")
			{
				break;
			}
    
			if (!CheckPacket(header))
			{
				break;
			}
    
			switch (header)
			{
				case LG_HEADER_GC_OBSERVER_ADD:
					ret = RecvObserverAddPacket();
					break;
				case LG_HEADER_GC_OBSERVER_REMOVE:
					ret = RecvObserverRemovePacket();
					break;
				case LG_HEADER_GC_OBSERVER_MOVE:
					ret = RecvObserverMovePacket();
					break;
				case LG_HEADER_GC_WARP:
					ret = RecvWarpPacket();
					break;
    
				case LG_HEADER_GC_PHASE:
					ret = RecvPhasePacket();
					return;
					break;
    
				case LG_HEADER_GC_PVP:
					ret = RecvPVPPacket();
					break;
    
				case LG_HEADER_GC_CHARACTER_ADD:
					 ret = RecvCharacterAppendPacket();
					break;
    
				case LG_HEADER_GC_CHAR_ADDITIONAL_INFO:
					ret = RecvCharacterAdditionalInfo();
					break;
    
				case LG_HEADER_GC_CHARACTER_ADD2:
					ret = RecvCharacterAppendPacketNew();
					break;
    
				case LG_HEADER_GC_CHARACTER_UPDATE:
					ret = RecvCharacterUpdatePacket();
					break;
    
				case LG_HEADER_GC_CHARACTER_DEL:
					ret = RecvCharacterDeletePacket();
					break;
    
				case LG_HEADER_GC_CHAT:
					ret = RecvChatPacket();
					break;
    
				case LG_HEADER_GC_SYNC_POSITION:
					ret = RecvSyncPositionPacket();
					break;
    
				case LG_HEADER_GC_OWNERSHIP:
					ret = RecvOwnerShipPacket();
					break;
    
				case LG_HEADER_GC_WHISPER:
					ret = RecvWhisperPacket();
					break;
    
				case LG_HEADER_GC_CHARACTER_MOVE:
					ret = RecvCharacterMovePacket();
					break;
    
				case LG_HEADER_GC_CHARACTER_POSITION:
					ret = RecvCharacterPositionPacket();
					break;
    
				case LG_HEADER_GC_STUN:
					ret = RecvStunPacket();
					break;
    
				case LG_HEADER_GC_DEAD:
					ret = RecvDeadPacket();
					break;
    
				case LG_HEADER_GC_PLAYER_POINT_CHANGE:
					ret = RecvPointChange();
					break;
    
				case LG_HEADER_GC_ITEM_SET:
					ret = RecvItemSetPacket();
					break;
    
				case LG_HEADER_GC_ITEM_SET2:
					ret = RecvItemSetPacket2();
					break;
    
				case LG_HEADER_GC_ITEM_USE:
					ret = RecvItemUsePacket();
					break;
    
				case LG_HEADER_GC_ITEM_UPDATE:
					ret = RecvItemUpdatePacket();
					break;
    
				case LG_HEADER_GC_ITEM_GROUND_ADD:
					ret = RecvItemGroundAddPacket();
					break;
    
				case LG_HEADER_GC_ITEM_GROUND_DEL:
					ret = RecvItemGroundDelPacket();
					break;
    
				case LG_HEADER_GC_ITEM_OWNERSHIP:
					ret = RecvItemOwnership();
					break;
    
				case LG_HEADER_GC_QUICKSLOT_ADD:
					ret = RecvQuickSlotAddPacket();
					break;
    
				case LG_HEADER_GC_QUICKSLOT_DEL:
					ret = RecvQuickSlotDelPacket();
					break;
    
				case LG_HEADER_GC_QUICKSLOT_SWAP:
					ret = RecvQuickSlotMovePacket();
					break;
    
				case LG_HEADER_GC_MOTION:
					ret = RecvMotionPacket();
					break;
    
				case LG_HEADER_GC_SHOP:
					ret = RecvShopPacket();
					break;
    
				case LG_HEADER_GC_SHOP_SIGN:
					ret = RecvShopSignPacket();
					break;
    
				case LG_HEADER_GC_EXCHANGE:
					ret = RecvExchangePacket();
					break;
    
				case LG_HEADER_GC_QUEST_INFO:
					ret = RecvQuestInfoPacket();
					break;
    
				case LG_HEADER_GC_REQUEST_MAKE_GUILD:
					ret = RecvRequestMakeGuild();
					break;
    
				case LG_HEADER_GC_PING:
					ret = RecvPingPacket();
					break;
    
				case LG_HEADER_GC_SCRIPT:
					ret = RecvScriptPacket();
					break;
    
				case LG_HEADER_GC_QUEST_CONFIRM:
					ret = RecvQuestConfirmPacket();
					break;
    
	#if ENABLE_TARGET_INFO
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
				case LG_HEADER_GC_TARGET_INFO:
					ret = RecvTargetInfoPacket();
					break;
	#endif
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
				case LG_HEADER_GC_TARGET:
					ret = RecvTargetPacket();
					break;
    
				case LG_HEADER_GC_DAMAGE_INFO:
					ret = RecvDamageInfoPacket();
					break;
    
				case LG_HEADER_GC_MOUNT:
					ret = RecvMountPacket();
					break;
    
				case LG_HEADER_GC_CHANGE_SPEED:
					ret = RecvChangeSpeedPacket();
					break;
    
				case LG_HEADER_GC_PLAYER_POINTS:
					ret = __RecvPlayerPoints();
					break;
    
				case LG_HEADER_GC_CREATE_FLY:
					ret = RecvCreateFlyPacket();
					break;
    
				case LG_HEADER_GC_FLY_TARGETING:
					ret = RecvFlyTargetingPacket();
					break;
    
				case LG_HEADER_GC_ADD_FLY_TARGETING:
					ret = RecvAddFlyTargetingPacket();
					break;
    
				case LG_HEADER_GC_SKILL_LEVEL:
					ret = RecvSkillLevel();
					break;
    
				case LG_HEADER_GC_SKILL_LEVEL_NEW:
					ret = RecvSkillLevelNew();
					break;
    
				case LG_HEADER_GC_MESSENGER:
					ret = RecvMessenger();
					break;
    
				case LG_HEADER_GC_GUILD:
					ret = RecvGuild();
					break;
    
				case LG_HEADER_GC_PARTY_INVITE:
					ret = RecvPartyInvite();
					break;
    
				case LG_HEADER_GC_PARTY_ADD:
					ret = RecvPartyAdd();
					break;
    
				case LG_HEADER_GC_PARTY_UPDATE:
					ret = RecvPartyUpdate();
					break;
    
				case LG_HEADER_GC_PARTY_REMOVE:
					ret = RecvPartyRemove();
					break;
    
				case LG_HEADER_GC_PARTY_LINK:
					ret = RecvPartyLink();
					break;
    
				case LG_HEADER_GC_PARTY_UNLINK:
					ret = RecvPartyUnlink();
					break;
    
				case LG_HEADER_GC_PARTY_PARAMETER:
					ret = RecvPartyParameter();
					break;
    
				case LG_HEADER_GC_SAFEBOX_SET:
					ret = RecvSafeBoxSetPacket();
					break;
    
				case LG_HEADER_GC_SAFEBOX_DEL:
					ret = RecvSafeBoxDelPacket();
					break;
    
				case LG_HEADER_GC_SAFEBOX_WRONG_PASSWORD:
					ret = RecvSafeBoxWrongPasswordPacket();
					break;
    
				case LG_HEADER_GC_SAFEBOX_SIZE:
					ret = RecvSafeBoxSizePacket();
					break;
    
				case LG_HEADER_GC_SAFEBOX_MONEY_CHANGE:
					ret = RecvSafeBoxMoneyChangePacket();
					break;
    
				case LG_HEADER_GC_FISHING:
					ret = RecvFishing();
					break;
    
				case LG_HEADER_GC_DUNGEON:
					ret = RecvDungeon();
					break;
    
				case LG_HEADER_GC_TIME:
					ret = RecvTimePacket();
					break;
    
				case LG_HEADER_GC_WALK_MODE:
					ret = RecvWalkModePacket();
					break;
    
				case LG_HEADER_GC_CHANGE_SKILL_GROUP:
					ret = RecvChangeSkillGroupPacket();
					break;
    
				case LG_HEADER_GC_REFINE_INFORMATION:
					ret = RecvRefineInformationPacket();
					break;
    
				case LG_HEADER_GC_REFINE_INFORMATION_NEW:
					ret = RecvRefineInformationPacketNew();
					break;
    
				case LG_HEADER_GC_SEPCIAL_EFFECT:
					ret = RecvSpecialEffect();
					break;
    
				case LG_HEADER_GC_NPC_POSITION:
					ret = RecvNPCList();
					break;
    
				case LG_HEADER_GC_CHANNEL:
					ret = RecvChannelPacket();
					break;
    
				case LG_HEADER_GC_VIEW_EQUIP:
					ret = RecvViewEquipPacket();
					break;
    
				case LG_HEADER_GC_LAND_LIST:
					ret = RecvLandPacket();
					break;
    
				case LG_HEADER_GC_TARGET_CREATE_NEW:
					ret = RecvTargetCreatePacketNew();
					break;
    
				case LG_HEADER_GC_TARGET_UPDATE:
					ret = RecvTargetUpdatePacket();
					break;
    
				case LG_HEADER_GC_TARGET_DELETE:
					ret = RecvTargetDeletePacket();
					break;
    
				case LG_HEADER_GC_AFFECT_ADD:
					ret = RecvAffectAddPacket();
					break;
    
				case LG_HEADER_GC_AFFECT_REMOVE:
					ret = RecvAffectRemovePacket();
					break;
    
				case LG_HEADER_GC_MALL_OPEN:
					ret = RecvMallOpenPacket();
					break;
    
				case LG_HEADER_GC_MALL_SET:
					ret = RecvMallItemSetPacket();
					break;
    
				case LG_HEADER_GC_MALL_DEL:
					ret = RecvMallItemDelPacket();
					break;
    
				case LG_HEADER_GC_LOVER_INFO:
					ret = RecvLoverInfoPacket();
					break;
    
				case LG_HEADER_GC_LOVE_POINT_UPDATE:
					ret = RecvLovePointUpdatePacket();
					break;
    
				case LG_HEADER_GC_DIG_MOTION:
					ret = RecvDigMotionPacket();
					break;
    
				case LG_HEADER_GC_HANDSHAKE:
					RecvHandshakePacket();
					return;
					break;
    
				case LG_HEADER_GC_HANDSHAKE_OK:
					RecvHandshakeOKPacket();
					return;
					break;
    
	#if _IMPROVED_PACKET_ENCRYPTION_
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
				case LG_HEADER_GC_KEY_AGREEMENT:
					RecvKeyAgreementPacket();
					return;
					break;
    
				case LG_HEADER_GC_KEY_AGREEMENT_COMPLETED:
					RecvKeyAgreementCompletedPacket();
					return;
					break;
	#endif
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
				case LG_HEADER_GC_SPECIFIC_EFFECT:
					ret = RecvSpecificEffect();
					break;
    
				case LG_HEADER_GC_DRAGON_SOUL_REFINE:
					ret = RecvDragonSoulRefine();
					break;
    
				case LG_HEADER_GC_ACCE:
					ret = RecvAccePacket();
					break;
    
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
				case LG_HEADER_GC_REQUEST_CHANGE_LANGUAGE:
					ret = RecvRequestChangeLanguage();
					break;
	#endif
    
	#if ENABLE_EXTENDED_WHISPER_DETAILS
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
				case LG_HEADER_GC_WHISPER_DETAILS:
					ret = RecvWhisperDetails();
					break;
	#endif
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
				default:
					ret = RecvDefaultPacket(header);
					break;
			}
		}
    
		if (!ret)
		{
			RecvErrorPacket(header);
		}
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_nextRefreshTime = ELTimer_GetMSec();
    
		uint curTime = ELTimer_GetMSec();
		if (GamePhase_s_nextRefreshTime > curTime)
		{
			return;
		}
    
    
    
		if (m_isRefreshCharacterWnd)
		{
			m_isRefreshCharacterWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshCharacter", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshEquipmentWnd)
		{
			m_isRefreshEquipmentWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshEquipment", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshInventoryWnd)
		{
			m_isRefreshInventoryWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshInventory", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshExchangeWnd)
		{
			m_isRefreshExchangeWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshExchange", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshSkillWnd)
		{
			m_isRefreshSkillWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshSkill", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshSafeboxWnd)
		{
			m_isRefreshSafeboxWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshSafebox", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshMallWnd)
		{
			m_isRefreshMallWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshMall", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshStatus)
		{
			m_isRefreshStatus = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshStatus", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshMessengerWnd)
		{
			m_isRefreshMessengerWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshMessenger", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshGuildWndInfoPage)
		{
			m_isRefreshGuildWndInfoPage = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildInfoPage", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshGuildWndBoardPage)
		{
			m_isRefreshGuildWndBoardPage = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildBoardPage", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshGuildWndMemberPage)
		{
			m_isRefreshGuildWndMemberPage = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildMemberPage", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshGuildWndMemberPageGradeComboBox)
		{
			m_isRefreshGuildWndMemberPageGradeComboBox = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildMemberPageGradeComboBox", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshGuildWndSkillPage)
		{
			m_isRefreshGuildWndSkillPage = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildSkillPage", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshGuildWndGradePage)
		{
			m_isRefreshGuildWndGradePage = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildGradePage", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
    
		if (m_isRefreshAcceWnd)
		{
			m_isRefreshAcceWnd = false;
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshAcce", Py_BuildValue("()"));
			GamePhase_s_nextRefreshTime = curTime + 300;
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __InitializeGamePhase()
	{
		__ServerTimeSync_Initialize();
    
		m_isRefreshStatus = false;
		m_isRefreshCharacterWnd = false;
		m_isRefreshEquipmentWnd = false;
		m_isRefreshInventoryWnd = false;
		m_isRefreshExchangeWnd = false;
		m_isRefreshSkillWnd = false;
		m_isRefreshSafeboxWnd = false;
		m_isRefreshMallWnd = false;
		m_isRefreshMessengerWnd = false;
		m_isRefreshGuildWndInfoPage = false;
		m_isRefreshGuildWndBoardPage = false;
		m_isRefreshGuildWndMemberPage = false;
		m_isRefreshGuildWndMemberPageGradeComboBox = false;
		m_isRefreshGuildWndSkillPage = false;
		m_isRefreshGuildWndGradePage = false;
		m_isRefreshAcceWnd = false;
    
		m_EmoticonStringVector.clear();
    
		m_pInstTarget = null;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void Warp(int lGlobalX, int lGlobalY)
	{
		CPythonBackground rkBgMgr = CPythonBackground.Instance();
		rkBgMgr.Destroy();
		rkBgMgr.Create();
		rkBgMgr.Warp(lGlobalX, lGlobalY);
		rkBgMgr.RefreshShadowLevel();
    
		int lLocalX = lGlobalX;
		int lLocalY = lGlobalY;
		__GlobalPositionToLocalPosition(lLocalX, lLocalY);
		float fHeight = CPythonBackground.Instance().GetHeight((float)lLocalX, (float)lLocalY);
    
		IAbstractApplication rkApp = IAbstractApplication.GetSingleton();
		rkApp.SetCenterPosition((float)lLocalX, (float)lLocalY, fHeight);
    
		__ShowMapName(lLocalX, lLocalY);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ShowMapName(int lLocalX, int lLocalY)
	{
		string c_rstrMapFileName = CPythonBackground.Instance().GetWarpMapName();
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ShowMapName", Py_BuildValue("(sii)", c_rstrMapFileName, lLocalX, lLocalY));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __LeaveGamePhase()
	{
		CInstanceBase.ClearPVPKeySystem();
    
		__ClearNetworkActorManager();
    
		m_bComboSkillFlag = false;
    
		IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
		rkChrMgr.Destroy();
    
		CPythonItem rkItemMgr = CPythonItem.Instance();
		rkItemMgr.Destroy();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetGamePhase()
	{
		if ("Game" != m_strPhase)
		{
			m_phaseLeaveFunc.Run();
		}
    
		Tracen("");
		Tracen("## Network - Game Phase ##");
		Tracen("");
    
		m_strPhase = "Game";
    
		m_dwChangingPhaseTime = ELTimer_GetMSec();
		m_phaseProcessFunc.Set(this, CPythonNetworkStream.GamePhase);
		m_phaseLeaveFunc.Set(this, CPythonNetworkStream.__LeaveGamePhase);
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		rkPlayer.SetMainCharacterIndex(GetMainActorVID());
    
		__RefreshStatus();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvObserverAddPacket()
	{
		packet_observer_add kObserverAddPacket = new packet_observer_add();
		if (!Recv(sizeof(packet_observer_add), kObserverAddPacket))
		{
			return false;
		}
    
		CPythonMiniMap.Instance().AddObserver(kObserverAddPacket.vid, kObserverAddPacket.x * 100.0f, kObserverAddPacket.y * 100.0f);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendTargetInfoLoadPacket(uint dwVID)
	{
		packet_target_info_load TargetInfoLoadPacket = new packet_target_info_load();
		TargetInfoLoadPacket.header = LG_HEADER_CG_TARGET_INFO_LOAD;
		TargetInfoLoadPacket.dwVID = dwVID;
    
		if (!Send(sizeof(packet_target_info_load), TargetInfoLoadPacket))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvObserverRemovePacket()
	{
		packet_observer_add kObserverRemovePacket = new packet_observer_add();
		if (!Recv(sizeof(packet_observer_add), kObserverRemovePacket))
		{
			return false;
		}
    
		CPythonMiniMap.Instance().RemoveObserver(kObserverRemovePacket.vid);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvObserverMovePacket()
	{
		packet_observer_move kObserverMovePacket = new packet_observer_move();
		if (!Recv(sizeof(packet_observer_move), kObserverMovePacket))
		{
			return false;
		}
    
		CPythonMiniMap.Instance().MoveObserver(kObserverMovePacket.vid, kObserverMovePacket.x * 100.0f, kObserverMovePacket.y * 100.0f);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvWarpPacket()
	{
		packet_warp kWarpPacket = new packet_warp();
    
		if (!Recv(sizeof(packet_warp), kWarpPacket))
		{
			return false;
		}
    
		__DirectEnterMode_Set(m_dwSelectedCharacterIndex);
    
		CNetworkStream.Connect((uint)kWarpPacket.lAddr, kWarpPacket.wPort);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPVPPacket()
	{
		packet_pvp kPVPPacket = new packet_pvp();
		if (!Recv(sizeof(packet_pvp), kPVPPacket))
		{
			return false;
		}
    
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
    
		switch (kPVPPacket.bMode)
		{
			case PVP_MODE_AGREE:
				rkChrMgr.RemovePVPKey(kPVPPacket.dwVIDSrc, kPVPPacket.dwVIDDst);
    
				if (rkPlayer.IsMainCharacterIndex(kPVPPacket.dwVIDDst))
				{
					rkPlayer.RememberChallengeInstance(kPVPPacket.dwVIDSrc);
				}
    
				if (rkPlayer.IsMainCharacterIndex(kPVPPacket.dwVIDSrc))
				{
					rkPlayer.RememberCantFightInstance(kPVPPacket.dwVIDDst);
				}
				break;
			case PVP_MODE_REVENGE:
			{
				rkChrMgr.RemovePVPKey(kPVPPacket.dwVIDSrc, kPVPPacket.dwVIDDst);
    
				uint dwKiller = kPVPPacket.dwVIDSrc;
				uint dwVictim = kPVPPacket.dwVIDDst;
    
				if (rkPlayer.IsMainCharacterIndex(dwVictim))
				{
					rkPlayer.RememberRevengeInstance(dwKiller);
				}
    
				if (rkPlayer.IsMainCharacterIndex(dwKiller))
				{
					rkPlayer.RememberCantFightInstance(dwVictim);
				}
				break;
			}
    
			case PVP_MODE_FIGHT:
				rkChrMgr.InsertPVPKey(kPVPPacket.dwVIDSrc, kPVPPacket.dwVIDDst);
				rkPlayer.ForgetInstance(kPVPPacket.dwVIDSrc);
				rkPlayer.ForgetInstance(kPVPPacket.dwVIDDst);
				break;
			case PVP_MODE_NONE:
				rkChrMgr.RemovePVPKey(kPVPPacket.dwVIDSrc, kPVPPacket.dwVIDDst);
				rkPlayer.ForgetInstance(kPVPPacket.dwVIDSrc);
				rkPlayer.ForgetInstance(kPVPPacket.dwVIDDst);
				break;
		}
    
		__RefreshTargetBoardByVID(kPVPPacket.dwVIDSrc);
		__RefreshTargetBoardByVID(kPVPPacket.dwVIDDst);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void NotifyHack(string c_szMsg)
	{
		if (!m_kQue_stHack.empty())
		{
			if (c_szMsg == m_kQue_stHack.back())
			{
				return;
			}
		}
    
		m_kQue_stHack.push_back(c_szMsg);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __SendHack(string c_szMsg)
	{
		Tracen(c_szMsg);
    
		SPacketCGHack kPacketHack = new SPacketCGHack();
		kPacketHack.bHeader = LG_HEADER_CG_HACK;
		strncpy(kPacketHack.szBuf, c_szMsg, sizeof(kPacketHack.szBuf) - 1);
    
		if (!Send(sizeof(SPacketCGHack), kPacketHack))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendMessengerAddByVIDPacket(uint vid)
	{
		command_messenger packet = new command_messenger();
		packet.header = LG_HEADER_CG_MESSENGER;
		packet.subheader = MESSENGER_SUBLG_HEADER_CG_ADD_BY_VID;
		if (!Send(sizeof(command_messenger), packet))
		{
			return false;
		}
		if (!Send(sizeof(uint), vid))
		{
			return false;
		}
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendMessengerAddByNamePacket(string c_szName)
	{
		command_messenger packet = new command_messenger();
		packet.header = LG_HEADER_CG_MESSENGER;
		packet.subheader = MESSENGER_SUBLG_HEADER_CG_ADD_BY_NAME;
		if (!Send(sizeof(command_messenger), packet))
		{
			return false;
		}
		string szName = new string(new char[DefineConstants.CHARACTER_NAME_MAX_LEN]);
		strncpy(szName, c_szName, DefineConstants.CHARACTER_NAME_MAX_LEN - 1);
		szName = StringFunctions.ChangeCharacter(szName, DefineConstants.CHARACTER_NAME_MAX_LEN - 1, '\0');
    
		if (!Send(sizeof(char), szName))
		{
			return false;
		}
		Tracef(" SendMessengerAddByNamePacket : %s\n", c_szName);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendMessengerRemovePacket(string c_szKey, string c_szName)
	{
		command_messenger packet = new command_messenger();
		packet.header = LG_HEADER_CG_MESSENGER;
		packet.subheader = MESSENGER_SUBLG_HEADER_CG_REMOVE;
		if (!Send(sizeof(command_messenger), packet))
		{
			return false;
		}
		string szKey = new string(new char[DefineConstants.CHARACTER_NAME_MAX_LEN]);
		strncpy(szKey, c_szKey, DefineConstants.CHARACTER_NAME_MAX_LEN - 1);
		if (!Send(sizeof(char), szKey))
		{
			return false;
		}
		__RefreshTargetBoardByName(c_szName);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendCharacterStatePacket(in TPixelPosition c_rkPPosDst, float fDstRot, uint eFunc, uint uArg)
	{
		NANOBEGIN if (!__CanActMainInstance()) return true = new NANOBEGIN();
    
		if (fDstRot < 0.0f)
		{
			fDstRot = 360 + fDstRot;
		}
		else if (fDstRot > 360.0f)
		{
			fDstRot = fmodf(fDstRot, 360.0f);
		}
    
		command_move kStatePacket = new command_move();
		kStatePacket.bHeader = LG_HEADER_CG_CHARACTER_MOVE;
		kStatePacket.bFunc = eFunc;
		kStatePacket.bArg = uArg;
		kStatePacket.bRot = fDstRot / 5.0f;
		kStatePacket.lX = (int)c_rkPPosDst.x;
		kStatePacket.lY = (int)c_rkPPosDst.y;
		kStatePacket.dwTime = ELTimer_GetServerMSec();
    
		Debug.Assert(kStatePacket.lX >= 0 && kStatePacket.lX < 204800);
    
		__LocalPositionToGlobalPosition(kStatePacket.lX, kStatePacket.lY);
    
		if (!Send(sizeof(command_move), kStatePacket))
		{
			Tracenf("CPythonNetworkStream::SendCharacterStatePacket(dwCmdTime=%u, fDstPos=(%f, %f), fDstRot=%f, eFunc=%d uArg=%d) - PACKET SEND ERROR", kStatePacket.dwTime, (float)kStatePacket.lX, (float)kStatePacket.lY, fDstRot, kStatePacket.bFunc, kStatePacket.bArg);
			return false;
		}
		NANOEND return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendUseSkillPacket(uint dwSkillIndex, uint dwTargetVID)
	{
		command_use_skill UseSkillPacket = new command_use_skill();
		UseSkillPacket.bHeader = LG_HEADER_CG_USE_SKILL;
		UseSkillPacket.dwVnum = dwSkillIndex;
		UseSkillPacket.dwTargetVID = dwTargetVID;
		if (!Send(sizeof(command_use_skill), UseSkillPacket))
		{
			Tracen("CPythonNetworkStream::SendUseSkillPacket - SEND PACKET ERROR");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendChatPacket(string c_szChat, byte byType)
	{
		if (strlen(c_szChat) == 0)
		{
			return true;
		}
    
		if (strlen(c_szChat) >= 512)
		{
			return true;
		}
    
		if (c_szChat[0] == '/')
		{
			if (1 == strlen(c_szChat))
			{
				if (!m_strLastCommand.empty())
				{
					c_szChat = m_strLastCommand.c_str();
				}
			}
			else
			{
				m_strLastCommand = c_szChat;
			}
		}
    
		if (ClientCommand(c_szChat))
		{
			return true;
		}
    
		int iTextLen = strlen(c_szChat) + 1;
		command_chat ChatPacket = new command_chat();
		ChatPacket.header = LG_HEADER_CG_CHAT;
		ChatPacket.length = sizeof(command_chat) + iTextLen;
		ChatPacket.type = byType;
    
		if (!Send(sizeof(command_chat), ChatPacket))
		{
			return false;
		}
    
		if (!Send(iTextLen, c_szChat))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void RegisterEmoticonString(string pcEmoticonString)
	{
		if (m_EmoticonStringVector.size() >= CInstanceBase.EMOTICON_NUM)
		{
			TraceError("Can't register emoticon string... vector is full (size:%d)", m_EmoticonStringVector.size());
			return;
		}
		m_EmoticonStringVector.push_back(pcEmoticonString);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool ParseEmoticon(string pChatMsg, ref uint pdwEmoticon)
	{
		for (uint dwEmoticonIndex = 0; dwEmoticonIndex < m_EmoticonStringVector.size() ; ++dwEmoticonIndex)
		{
			if (strlen(pChatMsg) > m_EmoticonStringVector[dwEmoticonIndex].size())
			{
				continue;
			}
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const char * pcFind = strstr(pChatMsg, m_EmoticonStringVector[dwEmoticonIndex].c_str());
			char pcFind = strstr(pChatMsg, m_EmoticonStringVector[dwEmoticonIndex].c_str());
    
			if (pcFind != pChatMsg)
			{
				continue;
			}
    
			pdwEmoticon = dwEmoticonIndex;
    
			return true;
		}
    
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ConvertEmpireText(uint dwEmpireID, ref string szText)
	{
		if (dwEmpireID < 1 || dwEmpireID>3)
		{
			return;
		}
    
		uint uHanPos;
    
		STextConvertTable rkTextConvTable = m_aTextConvTable[dwEmpireID - 1];
    
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
		byte * pbText = (byte)szText;
		while ((*pbText) != 0)
		{
			if ((*pbText & 0x80) != 0)
			{
				if (pbText[0] >= 0xb0 && pbText[0] <= 0xc8 && pbText[1] >= 0xa1 && pbText[1] <= 0xfe)
				{
					uHanPos = (pbText[0] - 0xb0) * (0xfe-0xa1 + 1) + (pbText[1] - 0xa1);
					pbText[0] = rkTextConvTable.aacHan[uHanPos][0];
					pbText[1] = rkTextConvTable.aacHan[uHanPos][1];
				}
				pbText += 2;
			}
			else
			{
				if (*pbText >= (byte)'a' && *pbText <= (byte)'z')
				{
					*pbText = rkTextConvTable.acLower[*pbText - 'a'];
				}
				else if (*pbText >= (byte)'A' && *pbText <= (byte)'Z')
				{
					*pbText = rkTextConvTable.acUpper[*pbText - 'A'];
				}
				pbText++;
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvChatPacket()
	{
		packet_chatting kChat = new packet_chatting();
		string buf = new string(new char[1024 + 1]);
		string line = new string(new char[1024 + 1]);
    
		if (!Recv(sizeof(packet_chatting), kChat))
		{
			return false;
		}
    
		uint uChatSize = kChat.size - sizeof(packet_chatting);
    
		if (!Recv(uChatSize, buf))
		{
			return false;
		}
    
		buf = StringFunctions.ChangeCharacter(buf, uChatSize, '\0');
    
		if (kChat.type >= CHAT_TYPE_MAX_NUM)
		{
			return true;
		}
    
		if (CHAT_TYPE_COMMAND == kChat.type)
		{
			ServerCommand(buf);
			return true;
		}
    
		if (kChat.dwVID != 0)
		{
			CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
			CInstanceBase pkInstChatter = rkChrMgr.GetInstancePtr(kChat.dwVID);
			if (null == pkInstChatter)
			{
				return true;
			}
    
			switch (kChat.type)
			{
			case CHAT_TYPE_TALKING:
			case CHAT_TYPE_PARTY:
			case CHAT_TYPE_GUILD:
			case CHAT_TYPE_SHOUT:
			case CHAT_TYPE_WHISPER:
			{
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
					char * p = strchr(buf, ':');
    
					if (p != '\0')
					{
						p += 2;
					}
					else
					{
						p = buf;
					}
    
					uint dwEmoticon;
    
					if (ParseEmoticon(p, dwEmoticon))
					{
						pkInstChatter.SetEmoticon(dwEmoticon);
						return true;
					}
					else
					{
						if (gs_bEmpireLanuageEnable)
						{
							CInstanceBase pkInstMain = rkChrMgr.GetMainInstancePtr();
							if (pkInstMain != null)
							{
								if (!pkInstMain.IsSameEmpire(pkInstChatter))
								{
									__ConvertEmpireText(pkInstChatter.GetEmpireID(), p);
								}
							}
						}
    
						if (m_isEnableChatInsultFilter)
						{
							if (false == pkInstChatter.IsNPC() && false == pkInstChatter.IsEnemy())
							{
								__FilterInsult(p, strlen(p));
							}
						}
    
						_snprintf(line, sizeof(char), "%s", p);
					}
			}
				break;
			case CHAT_TYPE_COMMAND:
			case CHAT_TYPE_INFO:
			case CHAT_TYPE_NOTICE:
			case CHAT_TYPE_BIG_NOTICE:
			case CHAT_TYPE_MAX_NUM:
			default:
				_snprintf(line, sizeof(char), "%s", buf);
				break;
			}
    
			if (CHAT_TYPE_SHOUT != kChat.type)
			{
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
				CPythonTextTail.Instance().RegisterChatTail(kChat.dwVID, FilterChat(line));
	#else
				CPythonTextTail.Instance().RegisterChatTail(kChat.dwVID, line);
	#endif
			}
    
			if (pkInstChatter.IsPC())
			{
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
				CPythonChat.Instance().AppendChat(kChat.type, FilterChat(buf));
	#else
				CPythonChat.Instance().AppendChat(kChat.type, buf);
	#endif
			}
		}
		else
		{
			if (CHAT_TYPE_NOTICE == kChat.type)
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_SetTipMessage", Py_BuildValue("(s)", buf));
			}
			else if (CHAT_TYPE_BIG_NOTICE == kChat.type)
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_SetBigMessage", Py_BuildValue("(s)", buf));
			}
			else if (CHAT_TYPE_SHOUT == kChat.type)
			{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: char * p = strchr(buf, ':');
				char p = strchr(buf, ':');
    
				if (p != '\0')
				{
					if (m_isEnableChatInsultFilter)
					{
						__FilterInsult(p, strlen(p));
					}
				}
			}
    
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
			CPythonChat.Instance().AppendChat(kChat.type, FilterChat(buf));
	#else
			CPythonChat.Instance().AppendChat(kChat.type, buf);
	#endif
    
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvWhisperPacket()
	{
		packet_whisper whisperPacket = new packet_whisper();
		string buf = new string(new char[512 + 1]);
    
		if (!Recv(sizeof(packet_whisper), whisperPacket))
		{
			return false;
		}
    
		Debug.Assert(whisperPacket.wSize - sizeof(packet_whisper) < 512);
    
		if (!Recv(whisperPacket.wSize - sizeof(packet_whisper), buf))
		{
			return false;
		}
    
		buf = StringFunctions.ChangeCharacter(buf, whisperPacket.wSize - sizeof(packet_whisper), '\0');
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static char line[256];
		if (CPythonChat.WHISPER_TYPE_CHAT == whisperPacket.bType || CPythonChat.WHISPER_TYPE_GM == whisperPacket.bType)
		{
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
			_snprintf(RecvWhisperPacket_line, sizeof(RecvWhisperPacket_line), "%s : %s", whisperPacket.szNameFrom, FilterChat(buf));
	#else
			_snprintf(RecvWhisperPacket_line, sizeof(RecvWhisperPacket_line), "%s : %s", whisperPacket.szNameFrom, buf);
	#endif
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnRecvWhisper", Py_BuildValue("(iss)", (int) whisperPacket.bType, whisperPacket.szNameFrom, RecvWhisperPacket_line));
		}
		else if (CPythonChat.WHISPER_TYPE_SYSTEM == whisperPacket.bType || CPythonChat.WHISPER_TYPE_ERROR == whisperPacket.bType)
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnRecvWhisperSystemMessage", Py_BuildValue("(iss)", (int) whisperPacket.bType, whisperPacket.szNameFrom, buf));
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnRecvWhisperError", Py_BuildValue("(iss)", (int) whisperPacket.bType, whisperPacket.szNameFrom, buf));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendWhisperPacket(string name, string c_szChat)
	{
		if (strlen(c_szChat) >= 255)
		{
			return true;
		}
    
		int iTextLen = strlen(c_szChat) + 1;
		command_whisper WhisperPacket = new command_whisper();
		WhisperPacket.bHeader = LG_HEADER_CG_WHISPER;
		WhisperPacket.wSize = sizeof(command_whisper) + iTextLen;
    
		strncpy(WhisperPacket.szNameTo, name, sizeof(WhisperPacket.szNameTo) - 1);
    
		if (!Send(sizeof(command_whisper), WhisperPacket))
		{
			return false;
		}
    
		if (!Send(iTextLen, c_szChat))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPointChange()
	{
		packet_point_change PointChange = new packet_point_change();
    
		if (!Recv(sizeof(packet_point_change), PointChange))
		{
			Tracen("Recv Point Change Packet Error");
			return false;
		}
    
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		rkChrMgr.ShowPointEffect(PointChange.Type, PointChange.dwVID);
    
		CInstanceBase pInstance = CPythonCharacterManager.Instance().GetMainInstancePtr();
    
		if (pInstance != null)
		{
		if (PointChange.dwVID == pInstance.GetVirtualID())
		{
			CPythonPlayer rkPlayer = CPythonPlayer.Instance();
			rkPlayer.SetStatus(PointChange.Type, PointChange.value);
    
			switch (PointChange.Type)
			{
				case POINT_STAT_RESET_COUNT:
					__RefreshStatus();
					break;
				case POINT_LEVEL:
				case POINT_ST:
				case POINT_DX:
				case POINT_HT:
				case POINT_IQ:
					__RefreshStatus();
					__RefreshSkillWindow();
					break;
				case POINT_SKILL:
				case POINT_SUB_SKILL:
				case POINT_HORSE_SKILL:
					__RefreshSkillWindow();
					break;
				case POINT_ENERGY:
					if (PointChange.value == 0)
					{
						rkPlayer.SetStatus(POINT_ENERGY_END_TIME, 0);
					}
					__RefreshStatus();
					break;
				default:
					__RefreshStatus();
					break;
			}
    
			if (POINT_GOLD == PointChange.Type)
			{
				if (!CPythonSystem.Instance().IsShowYang())
				{
					return true;
				}
    
				if (PointChange.amount > 0)
				{
					PyObject args = PyTuple_New(1);
					PyTuple_SetItem(args, 0, PyLong_FromLongLong(PointChange.amount));
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnPickMoney", args);
				}
			}
		}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvStunPacket()
	{
		packet_stun StunPacket = new packet_stun();
    
		if (!Recv(sizeof(packet_stun), StunPacket))
		{
			Tracen("CPythonNetworkStream::RecvStunPacket Error");
			return false;
		}
    
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CInstanceBase pkInstSel = rkChrMgr.GetInstancePtr(StunPacket.vid);
    
		if (pkInstSel != null)
		{
			if (CPythonCharacterManager.Instance().GetMainInstancePtr() == pkInstSel)
			{
				pkInstSel.Die();
			}
			else
			{
				pkInstSel.Stun();
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvDeadPacket()
	{
		packet_dead DeadPacket = new packet_dead();
		if (!Recv(sizeof(packet_dead), DeadPacket))
		{
			Tracen("CPythonNetworkStream::RecvDeadPacket Error");
			return false;
		}
    
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CInstanceBase pkChrInstSel = rkChrMgr.GetInstancePtr(DeadPacket.vid);
		if (pkChrInstSel != null)
		{
			CInstanceBase pkInstMain = rkChrMgr.GetMainInstancePtr();
			if (pkInstMain == pkChrInstSel)
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnGameOver", Py_BuildValue("()"));
				CPythonPlayer.Instance().NotifyDeadMainCharacter();
			}
    
			pkChrInstSel.Die();
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendCharacterPositionPacket(byte iPosition)
	{
		command_position PositionPacket = new command_position();
    
		PositionPacket.header = LG_HEADER_CG_CHARACTER_POSITION;
		PositionPacket.position = iPosition;
    
		if (!Send(sizeof(command_position), PositionPacket))
		{
			Tracen("Send Character Position Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendOnClickPacket(uint vid)
	{
		command_on_click OnClickPacket = new command_on_click();
		OnClickPacket.header = LG_HEADER_CG_ON_CLICK;
		OnClickPacket.vid = vid;
    
		if (!Send(sizeof(command_on_click), OnClickPacket))
		{
			Tracen("Send On_Click Packet Error");
			return false;
		}
    
		Tracef("SendOnClickPacket\n");
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCharacterPositionPacket()
	{
		packet_position PositionPacket = new packet_position();
    
		if (!Recv(sizeof(packet_position), PositionPacket))
		{
			return false;
		}
    
		CInstanceBase pChrInstance = CPythonCharacterManager.Instance().GetInstancePtr(PositionPacket.vid);
    
		if (pChrInstance == null)
		{
			return true;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMotionPacket()
	{
		packet_motion MotionPacket = new packet_motion();
    
		if (!Recv(sizeof(packet_motion), MotionPacket))
		{
			return false;
		}
    
		CInstanceBase pMainInstance = CPythonCharacterManager.Instance().GetInstancePtr(MotionPacket.vid);
		CInstanceBase pVictimInstance = null;
    
		if (0 != MotionPacket.victim_vid)
		{
			pVictimInstance = CPythonCharacterManager.Instance().GetInstancePtr(MotionPacket.victim_vid);
		}
    
		if (pMainInstance == null)
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvShopPacket()
	{
		List<char> vecBuffer = new List<char>();
		vecBuffer.Clear();
    
		packet_shop packet_shop = new packet_shop();
		if (!Recv(sizeof(packet_shop), packet_shop))
		{
			return false;
		}
    
		int iSize = packet_shop.size - sizeof(packet_shop);
		if (iSize > 0)
		{
			vecBuffer.Resize(iSize);
			if (!Recv(iSize, vecBuffer[0]))
			{
				return false;
			}
		}
    
		switch (packet_shop.subheader)
		{
			case SHOP_SUBLG_HEADER_GC_START:
			{
					CPythonShop.Instance().Clear();
    
					uint dwVID = (uint) vecBuffer[0];
    
					packet_shop_start pShopStartPacket = (packet_shop_start) vecBuffer[4];
					for (byte iItemIndex = 0; iItemIndex < SHOP_HOST_ITEM_MAX_NUM; ++iItemIndex)
					{
						CPythonShop.Instance().SetItemData(iItemIndex, pShopStartPacket.items[iItemIndex]);
					}
    
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(i)", dwVID));
			}
				break;
    
			case SHOP_SUBLG_HEADER_GC_START_EX:
			{
					CPythonShop.Instance().Clear();
    
					packet_shop_start_ex pShopStartPacket = (packet_shop_start_ex) vecBuffer[0];
					size_t read_point = sizeof(packet_shop_start_ex);
    
					uint dwVID = pShopStartPacket.owner_vid;
					byte shop_tab_count = pShopStartPacket.shop_tab_count;
    
					CPythonShop.instance().SetTabCount(shop_tab_count);
    
					for (size_t LaniatusDefVariables = 0; LaniatusDefVariables < shop_tab_count; LaniatusDefVariables++)
					{
						packet_shop_start_ex.TSubPacketShopTab pPackTab = (packet_shop_start_ex.TSubPacketShopTab) vecBuffer[read_point];
						read_point += sizeof(packet_shop_start_ex.TSubPacketShopTab);
    
						CPythonShop.instance().SetTabCoinType(i, pPackTab.coin_type);
						CPythonShop.instance().SetTabName(i, pPackTab.name);
    
						packet_shop_item item = pPackTab.items[0];
    
						for (byte j = 0; j < SHOP_HOST_ITEM_MAX_NUM; j++)
						{
							TShopItemData itemData = (item + j);
							CPythonShop.Instance().SetItemData(i, j, itemData);
						}
					}
    
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartShop", Py_BuildValue("(i)", dwVID));
			}
				break;
    
    
			case SHOP_SUBLG_HEADER_GC_END:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "EndShop", Py_BuildValue("()"));
				break;
    
			case SHOP_SUBLG_HEADER_GC_UPDATE_ITEM:
			{
					packet_shop_update_item pShopUpdateItemPacket = (packet_shop_update_item) vecBuffer[0];
					CPythonShop.Instance().SetItemData(pShopUpdateItemPacket.pos, pShopUpdateItemPacket.item);
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshShop", Py_BuildValue("()"));
			}
				break;
    
			case SHOP_SUBLG_HEADER_GC_UPDATE_PRICE :
			{
				PyObject args = PyTuple_New(1);
				PyTuple_SetItem(args, 0, PyLong_FromLongLong((long) & vecBuffer[0]));
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "SetShopSellingPrice", args);
			}
			break;
    
			case SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_MONEY"));
				break;
    
			case SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_MONEY_EX:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_MONEY_EX"));
				break;
    
			case SHOP_SUBLG_HEADER_GC_SOLDOUT:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "SOLDOUT"));
				break;
    
			case SHOP_SUBLG_HEADER_GC_INVENTORY_FULL:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "INVENTORY_FULL"));
				break;
    
			case SHOP_SUBLG_HEADER_GC_INVALID_POS:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "INVALID_POS"));
				break;
    
			case SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_ITEM:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_ITEM"));
				break;
			case SHOP_SUBLG_HEADER_GC_NOT_ENOUGH_EXP:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnShopError", Py_BuildValue("(s)", "NOT_ENOUGH_EXP"));
				break;
    
			default:
				TraceError("CPythonNetworkStream::RecvShopPacket: Unknown subheader\n");
				break;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvExchangePacket()
	{
		packet_exchange exchange_packet = new packet_exchange();
    
		if (!Recv(sizeof(packet_exchange), exchange_packet))
		{
			return false;
		}
    
		switch (exchange_packet.subheader)
		{
			case EXCHANGE_SUBLG_HEADER_GC_START:
				CPythonExchange.Instance().Clear();
				CPythonExchange.Instance().Start();
				CPythonExchange.Instance().SetSelfName(CPythonPlayer.Instance().GetName());
    
				{
					CInstanceBase pCharacterInstance = CPythonCharacterManager.Instance().GetInstancePtr(exchange_packet.arg1);
    
					if (pCharacterInstance != null)
					{
						CPythonExchange.Instance().SetTargetName(pCharacterInstance.GetNameString());
						CPythonExchange.Instance().SetTargetLevel(pCharacterInstance.GetLevel());
					}
				}
    
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartExchange", Py_BuildValue("()"));
				break;
    
			case EXCHANGE_SUBLG_HEADER_GC_ITEM_ADD:
				if (exchange_packet.is_me)
				{
					int iSlotIndex = exchange_packet.arg2.cell;
					CPythonExchange.Instance().SetItemToSelf(iSlotIndex, exchange_packet.arg1, (ushort) exchange_packet.arg3);
					for (int LaniatusDefVariables = 0; LaniatusDefVariables < ITEM_SOCKET_SLOT_MAX_NUM; ++i)
					{
						CPythonExchange.Instance().SetItemMetinSocketToSelf(iSlotIndex, i, exchange_packet.alValues[LaniatusDefVariables]);
					}
					for (int j = 0; j < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++j)
					{
						CPythonExchange.Instance().SetItemAttributeToSelf(iSlotIndex, j, exchange_packet.aAttr[j].bType, exchange_packet.aAttr[j].sValue);
					}
				}
				else
				{
					int iSlotIndex = exchange_packet.arg2.cell;
					CPythonExchange.Instance().SetItemToTarget(iSlotIndex, exchange_packet.arg1, (ushort) exchange_packet.arg3);
					for (int LaniatusDefVariables = 0; LaniatusDefVariables < ITEM_SOCKET_SLOT_MAX_NUM; ++i)
					{
						CPythonExchange.Instance().SetItemMetinSocketToTarget(iSlotIndex, i, exchange_packet.alValues[LaniatusDefVariables]);
					}
					for (int j = 0; j < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++j)
					{
						CPythonExchange.Instance().SetItemAttributeToTarget(iSlotIndex, j, exchange_packet.aAttr[j].bType, exchange_packet.aAttr[j].sValue);
					}
				}
    
				__RefreshExchangeWindow();
				__RefreshInventoryWindow();
				break;
    
			case EXCHANGE_SUBLG_HEADER_GC_ITEM_DEL:
				if (exchange_packet.is_me)
				{
					CPythonExchange.Instance().DelItemOfSelf((byte) exchange_packet.arg1);
				}
				else
				{
					CPythonExchange.Instance().DelItemOfTarget((byte) exchange_packet.arg1);
				}
				__RefreshExchangeWindow();
				__RefreshInventoryWindow();
				break;
    
			case EXCHANGE_SUBLG_HEADER_GC_ELK_ADD:
				if (exchange_packet.is_me)
				{
					CPythonExchange.Instance().SetElkToSelf(exchange_packet.arg1);
				}
				else
				{
					CPythonExchange.Instance().SetElkToTarget(exchange_packet.arg1);
				}
    
				__RefreshExchangeWindow();
				break;
    
			case EXCHANGE_SUBLG_HEADER_GC_ACCEPT:
				if (exchange_packet.is_me)
				{
					CPythonExchange.Instance().SetAcceptToSelf((byte) exchange_packet.arg1);
				}
				else
				{
					CPythonExchange.Instance().SetAcceptToTarget((byte) exchange_packet.arg1);
				}
				__RefreshExchangeWindow();
				break;
    
			case EXCHANGE_SUBLG_HEADER_GC_END:
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "EndExchange", Py_BuildValue("()"));
				__RefreshInventoryWindow();
				CPythonExchange.Instance().End();
				break;
    
			case EXCHANGE_SUBLG_HEADER_GC_ALREADY:
				Tracef("trade_already");
				break;
    
			case EXCHANGE_SUBLG_HEADER_GC_LESS_ELK:
				Tracef("trade_less_elk");
				break;
		};
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvQuestInfoPacket()
	{
		packet_quest_info QuestInfo = new packet_quest_info();
    
		if (!Peek(sizeof(packet_quest_info), QuestInfo))
		{
			Tracen("Recv Quest Info Packet Error #1");
			return false;
		}
    
		if (!Peek(QuestInfo.size))
		{
			Tracen("Recv Quest Info Packet Error #2");
			return false;
		}
    
		Recv(sizeof(packet_quest_info));
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to value types:
	//Original Metin2 CPlus Line: const byte & c_rFlag = QuestInfo.flag;
		byte c_rFlag = QuestInfo.flag;
    
		const int QUEST_PACKET_TYPE_NONE = 0;
		const int QUEST_PACKET_TYPE_BEGIN = 1;
		const int QUEST_PACKET_TYPE_UPDATE = 2;
		const int QUEST_PACKET_TYPE_END = 3;
    
		byte byQuestPacketType = (byte)QUEST_PACKET_TYPE_NONE;
    
		if (0 != (c_rFlag & QUEST_SEND_IS_BEGIN))
		{
			byte isBegin;
			if (!Recv(sizeof(byte), isBegin))
			{
				return false;
			}
    
			if (isBegin != 0)
			{
				byQuestPacketType = (byte)QUEST_PACKET_TYPE_BEGIN;
			}
			else
			{
				byQuestPacketType = (byte)QUEST_PACKET_TYPE_END;
			}
		}
		else
		{
			byQuestPacketType = (byte)QUEST_PACKET_TYPE_UPDATE;
		}
    
		const string szTitle = "";
		const string szClockName = "";
		int iClockValue = 0;
		const string szCounterName = "";
		int iCounterValue = 0;
		const string szIconFileName = "";
    
		if (0 != (c_rFlag & QUEST_SEND_TITLE))
		{
			if (!Recv(sizeof(char), szTitle))
			{
				return false;
			}
    
			szTitle = StringFunctions.ChangeCharacter(szTitle, 30, '\0');
		}
		if (0 != (c_rFlag & QUEST_SEND_CLOCK_NAME))
		{
			if (!Recv(sizeof(char), szClockName))
			{
				return false;
			}
    
			szClockName = StringFunctions.ChangeCharacter(szClockName, 16, '\0');
		}
		if (0 != (c_rFlag & QUEST_SEND_CLOCK_VALUE))
		{
			if (!Recv(sizeof(int), iClockValue))
			{
				return false;
			}
		}
		if (0 != (c_rFlag & QUEST_SEND_COUNTER_NAME))
		{
			if (!Recv(sizeof(char), szCounterName))
			{
				return false;
			}
    
			szCounterName = StringFunctions.ChangeCharacter(szCounterName, 16, '\0');
		}
		if (0 != (c_rFlag & QUEST_SEND_COUNTER_VALUE))
		{
			if (!Recv(sizeof(int), iCounterValue))
			{
				return false;
			}
		}
		if (0 != (c_rFlag & QUEST_SEND_ICON_FILE))
		{
			if (!Recv(sizeof(char), szIconFileName))
			{
				return false;
			}
    
			szIconFileName = StringFunctions.ChangeCharacter(szIconFileName, 24, '\0');
		}
    
		CPythonQuest rkQuest = CPythonQuest.Instance();
    
		if (QUEST_PACKET_TYPE_END == byQuestPacketType)
		{
			rkQuest.DeleteQuestInstance(QuestInfo.index);
		}
		else if (QUEST_PACKET_TYPE_UPDATE == byQuestPacketType)
		{
			if (!rkQuest.IsQuest(QuestInfo.index))
			{
	#if ENABLE_QUEST_RENEWAL
				rkQuest.MakeQuest(QuestInfo.index, QuestInfo.c_index);
	#else
				rkQuest.MakeQuest(QuestInfo.index);
	#endif
			}
    
			if (strlen(szTitle) > 0)
			{
				rkQuest.SetQuestTitle(QuestInfo.index, szTitle);
			}
			if (strlen(szClockName) > 0)
			{
				rkQuest.SetQuestClockName(QuestInfo.index, szClockName);
			}
			if (strlen(szCounterName) > 0)
			{
				rkQuest.SetQuestCounterName(QuestInfo.index, szCounterName);
			}
			if (strlen(szIconFileName) > 0)
			{
				rkQuest.SetQuestIconFileName(QuestInfo.index, szIconFileName);
			}
    
			if ((c_rFlag & QUEST_SEND_CLOCK_VALUE) != 0)
			{
				rkQuest.SetQuestClockValue(QuestInfo.index, iClockValue);
			}
			if ((c_rFlag & QUEST_SEND_COUNTER_VALUE) != 0)
			{
				rkQuest.SetQuestCounterValue(QuestInfo.index, iCounterValue);
			}
		}
		else if (QUEST_PACKET_TYPE_BEGIN == byQuestPacketType)
		{
			CPythonQuest.SQuestInstance QuestInstance = new CPythonQuest.SQuestInstance();
			QuestInstance.dwIndex = QuestInfo.index;
			QuestInstance.strTitle = szTitle;
			QuestInstance.strClockName = szClockName;
			QuestInstance.iClockValue = iClockValue;
			QuestInstance.strCounterName = szCounterName;
			QuestInstance.iCounterValue = iCounterValue;
			QuestInstance.strIconFileName = szIconFileName;
			CPythonQuest.Instance().RegisterQuestInstance(QuestInstance);
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshQuest", Py_BuildValue("()"));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvQuestConfirmPacket()
	{
		packet_quest_confirm kQuestConfirmPacket = new packet_quest_confirm();
		if (!Recv(sizeof(packet_quest_confirm), kQuestConfirmPacket))
		{
			Tracen("RecvQuestConfirmPacket Error");
			return false;
		}
    
		PyObject poArg = Py_BuildValue("(sii)", kQuestConfirmPacket.msg, kQuestConfirmPacket.timeout, kQuestConfirmPacket.requestPID);
		 PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_OnQuestConfirm", poArg);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvRequestMakeGuild()
	{
		packet_blank blank = new packet_blank();
		if (!Recv(sizeof(packet_blank), blank))
		{
			Tracen("RecvRequestMakeGuild Packet Error");
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "AskGuildName", Py_BuildValue("()"));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void ToggleGameDebugInfo()
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ToggleDebugInfo", Py_BuildValue("()"));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendExchangeStartPacket(uint vid)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_exchange packet = new command_exchange();
    
		packet.header = LG_HEADER_CG_EXCHANGE;
		packet.subheader = EXCHANGE_SUBLG_HEADER_CG_START;
		packet.arg1 = vid;
    
		if (!Send(sizeof(command_exchange), packet))
		{
			Tracef("send_trade_start_packet Error\n");
			return false;
		}
    
		Tracef("send_trade_start_packet   vid %d \n", vid);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendExchangeElkAddPacket(long elk)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_exchange packet = new command_exchange();
    
		packet.header = LG_HEADER_CG_EXCHANGE;
		packet.subheader = EXCHANGE_SUBLG_HEADER_CG_ELK_ADD;
		packet.arg1 = elk;
    
		if (!Send(sizeof(command_exchange), packet))
		{
			Tracef("send_trade_elk_add_packet Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendExchangeItemAddPacket(TItemPos ItemPos, byte byDisplayPos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_exchange packet = new command_exchange();
    
		packet.header = LG_HEADER_CG_EXCHANGE;
		packet.subheader = EXCHANGE_SUBLG_HEADER_CG_ITEM_ADD;
		packet.Pos = ItemPos;
		packet.arg2 = byDisplayPos;
    
		if (!Send(sizeof(command_exchange), packet))
		{
			Tracef("send_trade_item_add_packet Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendExchangeItemDelPacket(byte pos)
	{
		Debug.Assert(!"Can't be called function - CPythonNetworkStream::SendExchangeItemDelPacket");
		return true;
    
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_exchange packet = new command_exchange();
    
		packet.header = LG_HEADER_CG_EXCHANGE;
		packet.subheader = EXCHANGE_SUBLG_HEADER_CG_ITEM_DEL;
		packet.arg1 = pos;
    
		if (!Send(sizeof(command_exchange), packet))
		{
			Tracef("send_trade_item_del_packet Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendExchangeAcceptPacket()
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_exchange packet = new command_exchange();
    
		packet.header = LG_HEADER_CG_EXCHANGE;
		packet.subheader = EXCHANGE_SUBLG_HEADER_CG_ACCEPT;
    
		if (!Send(sizeof(command_exchange), packet))
		{
			Tracef("send_trade_accept_packet Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendExchangeExitPacket()
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_exchange packet = new command_exchange();
    
		packet.header = LG_HEADER_CG_EXCHANGE;
		packet.subheader = EXCHANGE_SUBLG_HEADER_CG_CANCEL;
    
		if (!Send(sizeof(command_exchange), packet))
		{
			Tracef("send_trade_exit_packet Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendPointResetPacket()
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "StartPointReset", Py_BuildValue("()"));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsPlayerAttacking()
	{
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CInstanceBase pkInstMain = rkChrMgr.GetMainInstancePtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		if (!pkInstMain.IsAttacking())
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvScriptPacket()
	{
		packet_script ScriptPacket = new packet_script();
    
		if (!Recv(sizeof(packet_script), ScriptPacket))
		{
			TraceError("RecvScriptPacket_RecvError");
			return false;
		}
    
		if (ScriptPacket.size < sizeof(packet_script))
		{
			TraceError("RecvScriptPacket_SizeError");
			return false;
		}
    
		ScriptPacket.size -= sizeof(packet_script);
    
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static string str;
		RecvScriptPacket_str = "";
		RecvScriptPacket_str.resize(ScriptPacket.size+1);
    
		if (!Recv(ScriptPacket.size, RecvScriptPacket_str[0]))
		{
			return false;
		}
    
		RecvScriptPacket_str[RecvScriptPacket_str.size() - 1] = '\0';
    
		int iIndex = CPythonEventManager.Instance().RegisterEventSetFromString(RecvScriptPacket_str);
    
		if (-1 != iIndex)
		{
			CPythonEventManager.Instance().SetVisibleLineCount(iIndex, 30);
			CPythonNetworkStream.Instance().OnScriptEventStart(ScriptPacket.skin,iIndex);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendScriptAnswerPacket(int iAnswer)
	{
		command_script_answer ScriptAnswer = new command_script_answer();
    
		ScriptAnswer.header = LG_HEADER_CG_SCRIPT_ANSWER;
		ScriptAnswer.answer = (byte) iAnswer;
		if (!Send(sizeof(command_script_answer), ScriptAnswer))
		{
			Tracen("Send Script Answer Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendScriptButtonPacket(uint iIndex)
	{
		command_script_button ScriptButton = new command_script_button();
    
		ScriptButton.header = LG_HEADER_CG_SCRIPT_BUTTON;
		ScriptButton.idx = iIndex;
		if (!Send(sizeof(command_script_button), ScriptButton))
		{
			Tracen("Send Script Button Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendAnswerMakeGuildPacket(string c_szName)
	{
		command_guild_answer_make_guild Packet = new command_guild_answer_make_guild();
    
		Packet.header = LG_HEADER_CG_ANSWER_MAKE_GUILD;
		strncpy(Packet.guild_name, c_szName, GUILD_NAME_MAX_LEN);
		Packet.guild_name[GUILD_NAME_MAX_LEN] = '\0';
    
		if (!Send(sizeof(command_guild_answer_make_guild), Packet))
		{
			Tracen("SendAnswerMakeGuild Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendQuestInputStringPacket(string c_szString)
	{
		command_quest_input_string Packet = new command_quest_input_string();
		Packet.bHeader = LG_HEADER_CG_QUEST_INPUT_STRING;
		strncpy(Packet.szString, c_szString, QUEST_INPUT_STRING_MAX_NUM);
    
		if (!Send(sizeof(command_quest_input_string), Packet))
		{
			Tracen("SendQuestInputStringPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendQuestConfirmPacket(byte byAnswer, uint dwPID)
	{
		command_quest_confirm kPacket = new command_quest_confirm();
		kPacket.header = LG_HEADER_CG_QUEST_CONFIRM;
		kPacket.answer = byAnswer;
		kPacket.requestPID = dwPID;
    
		if (!Send(sizeof(command_quest_confirm), kPacket))
		{
			Tracen("SendQuestConfirmPacket Error");
			return false;
		}
    
		Tracenf(" SendQuestConfirmPacket : %d, %d", byAnswer, dwPID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSkillCoolTimeEnd()
	{
		packet_skill_cooltime_end kPacketSkillCoolTimeEnd = new packet_skill_cooltime_end();
		if (!Recv(sizeof(packet_skill_cooltime_end), kPacketSkillCoolTimeEnd))
		{
			Tracen("CPythonNetworkStream::RecvSkillCoolTimeEnd - RecvError");
			return false;
		}
    
		CPythonPlayer.Instance().EndSkillCoolTime(kPacketSkillCoolTimeEnd.bSkill);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSkillLevel()
	{
		Debug.Assert(!"CPythonNetworkStream::RecvSkillLevel - ??????? ?ʴ? ?Լ?");
		packet_skill_level packet = new packet_skill_level();
		if (!Recv(sizeof(packet_skill_level), packet))
		{
			Tracen("CPythonNetworkStream::RecvSkillLevel - RecvError");
			return false;
		}
    
		uint dwSlotIndex;
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < DefineConstants.SKILL_MAX_NUM; ++i)
		{
			if (rkPlayer.GetSkillSlotIndex(i, dwSlotIndex))
			{
				rkPlayer.SetSkillLevel(dwSlotIndex, packet.abSkillLevels[LaniatusDefVariables]);
			}
		}
    
		__RefreshSkillWindow();
		__RefreshStatus();
		Tracef(" >> RecvSkillLevel\n");
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSkillLevelNew()
	{
		packet_skill_level_new packet = new packet_skill_level_new();
    
		if (!Recv(sizeof(packet_skill_level_new), packet))
		{
			Tracen("CPythonNetworkStream::RecvSkillLevelNew - RecvError");
			return false;
		}
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
    
		rkPlayer.SetSkill(7, 0);
		rkPlayer.SetSkill(8, 0);
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < DefineConstants.SKILL_MAX_NUM; ++i)
		{
			SPlayerSkill rPlayerSkill = packet.skills[LaniatusDefVariables];
    
			if (i >= 112 && LaniatusDefVariables <= 115 && rPlayerSkill.bLevel)
			{
				rkPlayer.SetSkill(7, i);
			}
    
			if (i >= 116 && LaniatusDefVariables <= 119 && rPlayerSkill.bLevel)
			{
				rkPlayer.SetSkill(8, i);
			}
    
			rkPlayer.SetSkillLevel_(i, rPlayerSkill.bMasterType, rPlayerSkill.bLevel);
		}
    
		__RefreshSkillWindow();
		__RefreshStatus();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvDamageInfoPacket()
	{
		packet_damage_info DamageInfoPacket = new packet_damage_info();
    
		if (!Recv(sizeof(packet_damage_info), DamageInfoPacket))
		{
			Tracen("Recv Target Packet Error");
			return false;
		}
    
		CInstanceBase pInstTarget = CPythonCharacterManager.Instance().GetInstancePtr(DamageInfoPacket.dwVID);
		bool bSelf = (pInstTarget == CPythonCharacterManager.Instance().GetMainInstancePtr());
		bool bTarget = (pInstTarget == m_pInstTarget);
		if (pInstTarget != null)
		{
			if (DamageInfoPacket.damage >= 0)
			{
				pInstTarget.AddDamageEffect(DamageInfoPacket.damage,DamageInfoPacket.flag,bSelf,bTarget);
			}
			else
			{
				TraceError("Damage is equal or below 0.");
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvTargetPacket()
	{
		packet_target TargetPacket = new packet_target();
    
		if (!Recv(sizeof(packet_target), TargetPacket))
		{
			Tracen("Recv Target Packet Error");
			return false;
		}
    
		CInstanceBase pInstPlayer = CPythonCharacterManager.Instance().GetMainInstancePtr();
		CInstanceBase pInstTarget = CPythonCharacterManager.Instance().GetInstancePtr(TargetPacket.dwVID);
		if (pInstPlayer != null && pInstTarget != null)
		{
			if (!pInstTarget.IsDead())
			{
				if (pInstTarget.IsBuilding())
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "CloseTargetBoardIfDifferent", Py_BuildValue("(i)", TargetPacket.dwVID));
				}
				else if (pInstPlayer.CanViewTargetHP(pInstTarget))
				{
	#if ENABLE_ELEMENT_TARGET
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "SetHPTargetBoard", Py_BuildValue("(iiiii)", TargetPacket.dwVID, TargetPacket.bHPPercent, TargetPacket.iMinHP, TargetPacket.iMaxHP, TargetPacket.bElement));
	#else
    
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "SetHPTargetBoard", Py_BuildValue("(iiii)", TargetPacket.dwVID, TargetPacket.bHPPercent));
	#endif
				}
				else
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "CloseTargetBoard", Py_BuildValue("()"));
				}
    
				m_pInstTarget = pInstTarget;
			}
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "CloseTargetBoard", Py_BuildValue("()"));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvTargetInfoPacket()
	{
		packet_target_info pInfoTargetPacket = new packet_target_info();
    
		if (!Recv(sizeof(packet_target_info), pInfoTargetPacket))
		{
			Tracen("Recv Info Target Packet Error");
			return false;
		}
    
		CInstanceBase pInstPlayer = CPythonCharacterManager.Instance().GetMainInstancePtr();
		CInstanceBase pInstTarget = CPythonCharacterManager.Instance().GetInstancePtr(pInfoTargetPacket.dwVID);
		if (pInstPlayer != null && pInstTarget != null)
		{
			if (!pInstTarget.IsDead())
			{
				if (pInstTarget.IsEnemy() || pInstTarget.IsStone())
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AddTargetMonsterDropInfo", Py_BuildValue("(iii)", pInfoTargetPacket.race, pInfoTargetPacket.dwVnum, pInfoTargetPacket.count));
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_RefreshTargetMonsterDropInfo", Py_BuildValue("(i)", pInfoTargetPacket.race));
				}
				else
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "CloseTargetBoard", Py_BuildValue("()"));
				}
			}
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "CloseTargetBoard", Py_BuildValue("()"));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMountPacket()
	{
		packet_mount MountPacket = new packet_mount();
    
		if (!Recv(sizeof(packet_mount), MountPacket))
		{
			Tracen("Recv Mount Packet Error");
			return false;
		}
    
		CInstanceBase pInstance = CPythonCharacterManager.Instance().GetInstancePtr(MountPacket.vid);
    
		if (pInstance != null)
		{
			if (0 != MountPacket.mount_vid)
			{
			}
			else
			{
			}
		}
    
		if (CPythonPlayer.Instance().IsMainCharacterIndex(MountPacket.vid))
		{
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvChangeSpeedPacket()
	{
		packet_change_speed SpeedPacket = new packet_change_speed();
    
		if (!Recv(sizeof(packet_change_speed), SpeedPacket))
		{
			Tracen("Recv Speed Packet Error");
			return false;
		}
    
		CInstanceBase pInstance = CPythonCharacterManager.Instance().GetInstancePtr(SpeedPacket.vid);
    
		if (pInstance == null)
		{
			return true;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendAttackPacket(uint uMotAttack, uint dwVIDVictim)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		if (!__IsPlayerAttacking())
		{
			return true;
		}
    
	#if ATTACK_TIME_LOG
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint prevTime = timeGetTime();
		uint curTime = timeGetTime();
		TraceError("TIME: %.4f(%.4f) ATTACK_PACKET: %d TARGET: %d", curTime / 1000.0f, (curTime - SendAttackPacket_prevTime) / 1000.0f, uMotAttack, dwVIDVictim);
		SendAttackPacket_prevTime = curTime;
	#endif
    
		command_attack kPacketAtk = new command_attack();
    
		kPacketAtk.header = LG_HEADER_CG_ATTACK;
		kPacketAtk.bType = uMotAttack;
		kPacketAtk.dwVictimVID = dwVIDVictim;
    
		if (!SendSpecial(sizeof(command_attack), kPacketAtk))
		{
			Tracen("Send Battle Attack Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSpecial(int nLen, object pvBuf)
	{
		byte bHeader = (byte) pvBuf;
    
		switch (bHeader)
		{
			case LG_HEADER_CG_ATTACK:
			{
					command_attack pkPacketAtk = (command_attack) pvBuf;
					pkPacketAtk.bCRCMagicCubeProcPiece = GetProcessCRCMagicCubePiece();
					pkPacketAtk.bCRCMagicCubeFilePiece = GetProcessCRCMagicCubePiece();
					return Send(nLen, pvBuf);
			}
				break;
		}
    
		return Send(nLen, pvBuf);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvAddFlyTargetingPacket()
	{
		packet_fly_targeting kPacket = new packet_fly_targeting();
		if (!Recv(sizeof(packet_fly_targeting), kPacket))
		{
			return false;
		}
    
		__GlobalPositionToLocalPosition(kPacket.lX, kPacket.lY);
    
		Tracef("VID [%d]?? Ÿ???? ??? ????\n",kPacket.dwShooterVID);
    
		CPythonCharacterManager rpcm = CPythonCharacterManager.Instance();
    
		CInstanceBase pShooter = rpcm.GetInstancePtr(kPacket.dwShooterVID);
    
		if (pShooter == null)
		{
	#if ! DEBUG
			TraceError("CPythonNetworkStream::RecvFlyTargetingPacket() - dwShooterVID[%d] NOT EXIST", kPacket.dwShooterVID);
	#endif
			return true;
		}
    
		CInstanceBase pTarget = rpcm.GetInstancePtr(kPacket.dwTargetVID);
    
		if (kPacket.dwTargetVID && pTarget != null)
		{
			pShooter.GetGraphicThingInstancePtr().AddFlyTarget(pTarget.GetGraphicThingInstancePtr());
		}
		else
		{
			float h = CPythonBackground.Instance().GetHeight(kPacket.lX,kPacket.lY) + 60.0f;
			pShooter.GetGraphicThingInstancePtr().AddFlyTarget(D3DXVECTOR3(kPacket.lX,kPacket.lY,h));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvFlyTargetingPacket()
	{
		packet_fly_targeting kPacket = new packet_fly_targeting();
		if (!Recv(sizeof(packet_fly_targeting), kPacket))
		{
			return false;
		}
    
		__GlobalPositionToLocalPosition(kPacket.lX, kPacket.lY);
    
		CPythonCharacterManager rpcm = CPythonCharacterManager.Instance();
    
		CInstanceBase pShooter = rpcm.GetInstancePtr(kPacket.dwShooterVID);
    
		if (pShooter == null)
		{
	#if DEBUG
			TraceError("CPythonNetworkStream::RecvFlyTargetingPacket() - dwShooterVID[%d] NOT EXIST", kPacket.dwShooterVID);
	#endif
			return true;
		}
    
		CInstanceBase pTarget = rpcm.GetInstancePtr(kPacket.dwTargetVID);
    
		if (kPacket.dwTargetVID && pTarget != null)
		{
			pShooter.GetGraphicThingInstancePtr().SetFlyTarget(pTarget.GetGraphicThingInstancePtr());
		}
		else
		{
			float h = CPythonBackground.Instance().GetHeight(kPacket.lX, kPacket.lY) + 60.0f;
			pShooter.GetGraphicThingInstancePtr().SetFlyTarget(D3DXVECTOR3(kPacket.lX,kPacket.lY,h));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendShootPacket(uint uSkill)
	{
		packet_shoot kPacketShoot = new packet_shoot();
		kPacketShoot.bHeader = LG_HEADER_CG_SHOOT;
		kPacketShoot.bType = uSkill;
    
		if (!Send(sizeof(packet_shoot), kPacketShoot))
		{
			Tracen("SendShootPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendAddFlyTargetingPacket(uint dwTargetVID, in TPixelPosition kPPosTarget)
	{
		command_fly_targeting packet = new command_fly_targeting();
    
		packet.bHeader = LG_HEADER_CG_ADD_FLY_TARGETING;
		packet.dwTargetVID = dwTargetVID;
		packet.lX = kPPosTarget.x;
		packet.lY = kPPosTarget.y;
    
		__LocalPositionToGlobalPosition(packet.lX, packet.lY);
    
		if (!Send(sizeof(command_fly_targeting), packet))
		{
			Tracen("Send FlyTargeting Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendFlyTargetingPacket(uint dwTargetVID, in TPixelPosition kPPosTarget)
	{
		command_fly_targeting packet = new command_fly_targeting();
    
		packet.bHeader = LG_HEADER_CG_FLY_TARGETING;
		packet.dwTargetVID = dwTargetVID;
		packet.lX = kPPosTarget.x;
		packet.lY = kPPosTarget.y;
    
		__LocalPositionToGlobalPosition(packet.lX, packet.lY);
    
		if (!Send(sizeof(command_fly_targeting), packet))
		{
			Tracen("Send FlyTargeting Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCreateFlyPacket()
	{
		packet_fly kPacket = new packet_fly();
		if (!Recv(sizeof(packet_fly), kPacket))
		{
			return false;
		}
    
		CFlyingManager rkFlyMgr = CFlyingManager.Instance();
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
    
		CInstanceBase pkStartInst = rkChrMgr.GetInstancePtr(kPacket.dwStartVID);
		CInstanceBase pkEndInst = rkChrMgr.GetInstancePtr(kPacket.dwEndVID);
		if (pkStartInst == null || pkEndInst == null)
		{
			return true;
		}
    
		rkFlyMgr.CreateIndexedFly(kPacket.bType, pkStartInst.GetGraphicThingInstancePtr(), pkEndInst.GetGraphicThingInstancePtr());
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendTargetPacket(uint dwVID)
	{
		command_target packet = new command_target();
		packet.header = LG_HEADER_CG_TARGET;
		packet.dwVID = dwVID;
    
		if (!Send(sizeof(command_target), packet))
		{
			Tracen("Send Target Packet Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSyncPositionElementPacket(uint dwVictimVID, uint dwVictimX, uint dwVictimY)
	{
		command_sync_position_element kSyncPos = new command_sync_position_element();
		kSyncPos.dwVID = dwVictimVID;
		kSyncPos.lX = dwVictimX;
		kSyncPos.lY = dwVictimY;
    
		__LocalPositionToGlobalPosition(kSyncPos.lX, kSyncPos.lY);
    
		if (!Send(sizeof(command_sync_position_element), kSyncPos))
		{
			Tracen("CPythonNetworkStream::SendSyncPositionElementPacket - ERROR");
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMessenger()
	{
		packet_messenger p = new packet_messenger();
		if (!Recv(sizeof(packet_messenger), p))
		{
			return false;
		}
    
		int iSize = p.size - sizeof(packet_messenger);
		string char_name = new string(new char[24 + 1]);
    
		switch (p.subheader)
		{
			case MESSENGER_SUBLG_HEADER_GC_LIST:
			{
				packet_messenger_list_online on = new packet_messenger_list_online();
				while (iSize != 0)
				{
					if (!Recv(sizeof(packet_messenger_list_offline), on))
					{
						return false;
					}
    
					if (!Recv(on.length, char_name))
					{
						return false;
					}
    
					char_name = char_name.Substring(0, on.length);
    
					if ((on.connected & MESSENGER_CONNECTED_STATE_ONLINE) != 0)
					{
						CPythonMessenger.Instance().OnFriendLogin(char_name);
					}
					else
					{
						CPythonMessenger.Instance().OnFriendLogout(char_name);
					}
    
					iSize -= sizeof(packet_messenger_list_offline);
					iSize -= on.length;
				}
				break;
			}
    
			case MESSENGER_SUBLG_HEADER_GC_LOGIN:
			{
				packet_messenger_login p = new packet_messenger_login();
				if (!Recv(sizeof(packet_messenger_login), p))
				{
					return false;
				}
				if (!Recv(p.length, char_name))
				{
					return false;
				}
				char_name = char_name.Substring(0, p.length);
				CPythonMessenger.Instance().OnFriendLogin(char_name);
				__RefreshTargetBoardByName(char_name);
				break;
			}
    
			case MESSENGER_SUBLG_HEADER_GC_LOGOUT:
			{
				packet_messenger_logout logout = new packet_messenger_logout();
				if (!Recv(sizeof(packet_messenger_logout), logout))
				{
					return false;
				}
				if (!Recv(logout.length, char_name))
				{
					return false;
				}
				char_name = char_name.Substring(0, logout.length);
				CPythonMessenger.Instance().OnFriendLogout(char_name);
				break;
			}
    
			case MESSENGER_SUBLG_HEADER_GC_REMOVE_FRIEND:
			{
				byte bLength;
				if (!Recv(sizeof(byte), bLength))
				{
					return false;
				}
    
				if (!Recv(bLength, char_name))
				{
					return false;
				}
    
				char_name = char_name.Substring(0, bLength);
				CPythonMessenger.Instance().RemoveFriend(char_name);
				break;
			}
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendPartyInvitePacket(uint dwVID)
	{
		command_party_invite kPartyInvitePacket = new command_party_invite();
		kPartyInvitePacket.header = LG_HEADER_CG_PARTY_INVITE;
		kPartyInvitePacket.vid = dwVID;
    
		if (!Send(sizeof(command_party_invite), kPartyInvitePacket))
		{
			Tracenf("CPythonNetworkStream::SendPartyInvitePacket [%ud] - PACKET SEND ERROR", dwVID);
			return false;
		}
    
		Tracef(" << SendPartyInvitePacket : %d\n", dwVID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendPartyInviteAnswerPacket(uint dwLeaderVID, byte byAnswer)
	{
		command_party_invite_answer kPartyInviteAnswerPacket = new command_party_invite_answer();
		kPartyInviteAnswerPacket.header = LG_HEADER_CG_PARTY_INVITE_ANSWER;
		kPartyInviteAnswerPacket.leader_pid = dwLeaderVID;
		kPartyInviteAnswerPacket.accept = byAnswer;
    
		if (!Send(sizeof(command_party_invite_answer), kPartyInviteAnswerPacket))
		{
			Tracenf("CPythonNetworkStream::SendPartyInviteAnswerPacket [%ud %ud] - PACKET SEND ERROR", dwLeaderVID, byAnswer);
			return false;
		}
    
		Tracef(" << SendPartyInviteAnswerPacket : %d, %d\n", dwLeaderVID, byAnswer);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendPartyRemovePacket(uint dwPID)
	{
		command_party_remove kPartyInviteRemove = new command_party_remove();
		kPartyInviteRemove.header = LG_HEADER_CG_PARTY_REMOVE;
		kPartyInviteRemove.pid = dwPID;
    
		if (!Send(sizeof(command_party_remove), kPartyInviteRemove))
		{
			Tracenf("CPythonNetworkStream::SendPartyRemovePacket [%ud] - PACKET SEND ERROR", dwPID);
			return false;
		}
    
		Tracef(" << SendPartyRemovePacket : %d\n", dwPID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendPartySetStatePacket(uint dwVID, byte byState, byte byFlag)
	{
		command_party_set_state kPartySetState = new command_party_set_state();
		kPartySetState.byHeader = LG_HEADER_CG_PARTY_SET_STATE;
		kPartySetState.dwVID = dwVID;
		kPartySetState.byState = byState;
		kPartySetState.byFlag = byFlag;
    
		if (!Send(sizeof(command_party_set_state), kPartySetState))
		{
			Tracenf("CPythonNetworkStream::SendPartySetStatePacket(%ud, %ud) - PACKET SEND ERROR", dwVID, byState);
			return false;
		}
    
		Tracef(" << SendPartySetStatePacket : %d, %d, %d\n", dwVID, byState, byFlag);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendPartyUseSkillPacket(byte bySkillIndex, uint dwVID)
	{
		command_party_use_skill kPartyUseSkill = new command_party_use_skill();
		kPartyUseSkill.byHeader = LG_HEADER_CG_PARTY_USE_SKILL;
		kPartyUseSkill.bySkillIndex = bySkillIndex;
		kPartyUseSkill.dwTargetVID = dwVID;
    
		if (!Send(sizeof(command_party_use_skill), kPartyUseSkill))
		{
			Tracenf("CPythonNetworkStream::SendPartyUseSkillPacket(%ud, %ud) - PACKET SEND ERROR", bySkillIndex, dwVID);
			return false;
		}
    
		Tracef(" << SendPartyUseSkillPacket : %d, %d\n", bySkillIndex, dwVID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendPartyParameterPacket(byte byDistributeMode)
	{
		command_party_parameter kPartyParameter = new command_party_parameter();
		kPartyParameter.bHeader = LG_HEADER_CG_PARTY_PARAMETER;
		kPartyParameter.bDistributeMode = byDistributeMode;
    
		if (!Send(sizeof(command_party_parameter), kPartyParameter))
		{
			Tracenf("CPythonNetworkStream::SendPartyParameterPacket(%d) - PACKET SEND ERROR", byDistributeMode);
			return false;
		}
    
		Tracef(" << SendPartyParameterPacket : %d\n", byDistributeMode);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPartyInvite()
	{
		packet_party_invite kPartyInvitePacket = new packet_party_invite();
		if (!Recv(sizeof(packet_party_invite), kPartyInvitePacket))
		{
			return false;
		}
    
		CInstanceBase pInstance = CPythonCharacterManager.Instance().GetInstancePtr(kPartyInvitePacket.leader_pid);
		if (pInstance == null)
		{
			TraceError(" CPythonNetworkStream::RecvPartyInvite - Failed to find leader instance [%d]\n", kPartyInvitePacket.leader_pid);
			return true;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RecvPartyInviteQuestion", Py_BuildValue("(is)", kPartyInvitePacket.leader_pid, pInstance.GetNameString()));
		Tracef(" >> RecvPartyInvite : %d, %s\n", kPartyInvitePacket.leader_pid, pInstance.GetNameString());
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPartyAdd()
	{
		packet_party_add kPartyAddPacket = new packet_party_add();
		if (!Recv(sizeof(packet_party_add), kPartyAddPacket))
		{
			return false;
		}
    
		CPythonPlayer.Instance().AppendPartyMember(kPartyAddPacket.pid, kPartyAddPacket.name);
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "AddPartyMember", Py_BuildValue("(is)", kPartyAddPacket.pid, kPartyAddPacket.name));
		Tracef(" >> RecvPartyAdd : %d, %s\n", kPartyAddPacket.pid, kPartyAddPacket.name);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPartyUpdate()
	{
		packet_party_update kPartyUpdatePacket = new packet_party_update();
		if (!Recv(sizeof(packet_party_update), kPartyUpdatePacket))
		{
			return false;
		}
    
		SPartyMemberInfo pPartyMemberInfo;
		if (!CPythonPlayer.Instance().GetPartyMemberPtr(kPartyUpdatePacket.pid, pPartyMemberInfo))
		{
			return true;
		}
    
		byte byOldState = pPartyMemberInfo.byState;
    
		CPythonPlayer.Instance().UpdatePartyMemberInfo(kPartyUpdatePacket.pid, kPartyUpdatePacket.state, kPartyUpdatePacket.percent_hp);
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < PARTY_AFFECT_SLOT_MAX_NUM; ++i)
		{
			CPythonPlayer.Instance().UpdatePartyMemberAffect(kPartyUpdatePacket.pid, i, kPartyUpdatePacket.affects[LaniatusDefVariables]);
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "UpdatePartyMemberInfo", Py_BuildValue("(i)", kPartyUpdatePacket.pid));
    
		uint dwVID;
		if (CPythonPlayer.Instance().PartyMemberPIDToVID(kPartyUpdatePacket.pid, dwVID))
		{
		if (byOldState != kPartyUpdatePacket.state)
		{
			__RefreshTargetBoardByVID(dwVID);
		}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPartyRemove()
	{
		packet_party_remove kPartyRemovePacket = new packet_party_remove();
		if (!Recv(sizeof(packet_party_remove), kPartyRemovePacket))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RemovePartyMember", Py_BuildValue("(i)", kPartyRemovePacket.pid));
		Tracef(" >> RecvPartyRemove : %d\n", kPartyRemovePacket.pid);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPartyLink()
	{
		packet_party_link kPartyLinkPacket = new packet_party_link();
		if (!Recv(sizeof(packet_party_link), kPartyLinkPacket))
		{
			return false;
		}
    
		CPythonPlayer.Instance().LinkPartyMember(kPartyLinkPacket.pid, kPartyLinkPacket.vid);
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "LinkPartyMember", Py_BuildValue("(ii)", kPartyLinkPacket.pid, kPartyLinkPacket.vid));
		Tracef(" >> RecvPartyLink : %d, %d\n", kPartyLinkPacket.pid, kPartyLinkPacket.vid);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPartyUnlink()
	{
		packet_party_unlink kPartyUnlinkPacket = new packet_party_unlink();
		if (!Recv(sizeof(packet_party_unlink), kPartyUnlinkPacket))
		{
			return false;
		}
    
		CPythonPlayer.Instance().UnlinkPartyMember(kPartyUnlinkPacket.pid);
    
		if (CPythonPlayer.Instance().IsMainCharacterIndex(kPartyUnlinkPacket.vid))
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "UnlinkAllPartyMember", Py_BuildValue("()"));
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "UnlinkPartyMember", Py_BuildValue("(i)", kPartyUnlinkPacket.pid));
		}
    
		Tracef(" >> RecvPartyUnlink : %d, %d\n", kPartyUnlinkPacket.pid, kPartyUnlinkPacket.vid);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvPartyParameter()
	{
		paryt_parameter kPartyParameterPacket = new paryt_parameter();
		if (!Recv(sizeof(paryt_parameter), kPartyParameterPacket))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "ChangePartyParameter", Py_BuildValue("(i)", kPartyParameterPacket.bDistributeMode));
		Tracef(" >> RecvPartyParameter : %d\n", kPartyParameterPacket.bDistributeMode);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildAddMemberPacket(uint dwVID)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_ADD_MEMBER;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
		if (!Send(sizeof(uint), dwVID))
		{
			return false;
		}
    
		Tracef(" SendGuildAddMemberPacket\n", dwVID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildRemoveMemberPacket(uint dwPID)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_REMOVE_MEMBER;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
		if (!Send(sizeof(uint), dwPID))
		{
			return false;
		}
    
		Tracef(" SendGuildRemoveMemberPacket %d\n", dwPID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildChangeGradeNamePacket(byte byGradeNumber, string c_szName)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_NAME;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
		if (!Send(sizeof(byte), byGradeNumber))
		{
			return false;
		}
    
		string szName = new string(new char[GUILD_GRADE_NAME_MAX_LEN + 1]);
		strncpy(szName, c_szName, GUILD_GRADE_NAME_MAX_LEN);
		szName = StringFunctions.ChangeCharacter(szName, GUILD_GRADE_NAME_MAX_LEN, '\0');
    
		if (!Send(sizeof(char), szName))
		{
			return false;
		}
    
		Tracef(" SendGuildChangeGradeNamePacket %d, %s\n", byGradeNumber, c_szName);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildChangeGradeAuthorityPacket(byte byGradeNumber, byte byAuthority)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_CHANGE_GRADE_AUTHORITY;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
		if (!Send(sizeof(byte), byGradeNumber))
		{
			return false;
		}
		if (!Send(sizeof(byte), byAuthority))
		{
			return false;
		}
    
		Tracef(" SendGuildChangeGradeAuthorityPacket %d, %d\n", byGradeNumber, byAuthority);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildOfferPacket(uint dwExperience)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_OFFER;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
		if (!Send(sizeof(uint), dwExperience))
		{
			return false;
		}
    
		Tracef(" SendGuildOfferPacket %d\n", dwExperience);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildPostCommentPacket(string c_szMessage)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_POST_COMMENT;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		byte bySize = (byte)((byte)strlen(c_szMessage) + 1);
		if (!Send(sizeof(byte), bySize))
		{
			return false;
		}
		if (!Send(bySize, c_szMessage))
		{
			return false;
		}
    
		Tracef(" SendGuildPostCommentPacket %d, %s\n", bySize, c_szMessage);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildDeleteCommentPacket(uint dwIndex)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_DELETE_COMMENT;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		if (!Send(sizeof(uint), dwIndex))
		{
			return false;
		}
    
		Tracef(" SendGuildDeleteCommentPacket %d\n", dwIndex);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildRefreshCommentsPacket(uint dwHighestIndex)
	{
	//# Laniatus Games Studio Inc. |: This static local variable declaration (not allowed in C#) has been moved just prior to the method:
	//	static uint s_LastTime = timeGetTime() - 1001;
    
		if (timeGetTime() - SendGuildRefreshCommentsPacket_s_LastTime < 1000)
		{
			return true;
		}
		SendGuildRefreshCommentsPacket_s_LastTime = timeGetTime();
    
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_REFRESH_COMMENT;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		Tracef(" SendGuildRefreshCommentPacket %d\n", dwHighestIndex);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildChangeMemberGradePacket(uint dwPID, byte byGrade)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GRADE;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		if (!Send(sizeof(uint), dwPID))
		{
			return false;
		}
		if (!Send(sizeof(byte), byGrade))
		{
			return false;
		}
    
		Tracef(" SendGuildChangeMemberGradePacket %d, %d\n", dwPID, byGrade);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildUseSkillPacket(uint dwSkillID, uint dwTargetVID)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_USE_SKILL;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		if (!Send(sizeof(uint), dwSkillID))
		{
			return false;
		}
		if (!Send(sizeof(uint), dwTargetVID))
		{
			return false;
		}
    
		Tracef(" SendGuildUseSkillPacket %d, %d\n", dwSkillID, dwTargetVID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildChangeMemberGeneralPacket(uint dwPID, byte byFlag)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_CHANGE_MEMBER_GENERAL;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		if (!Send(sizeof(uint), dwPID))
		{
			return false;
		}
		if (!Send(sizeof(byte), byFlag))
		{
			return false;
		}
    
		Tracef(" SendGuildChangeMemberGeneralFlagPacket %d, %d\n", dwPID, byFlag);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildInviteAnswerPacket(uint dwGuildID, byte byAnswer)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_GUILD_INVITE_ANSWER;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		if (!Send(sizeof(uint), dwGuildID))
		{
			return false;
		}
		if (!Send(sizeof(byte), byAnswer))
		{
			return false;
		}
    
		Tracef(" SendGuildInviteAnswerPacket %d, %d\n", dwGuildID, byAnswer);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildChargeGSPPacket(uint dwMoney)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_CHARGE_GSP;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
    
		if (!Send(sizeof(uint), dwMoney))
		{
			return false;
		}
    
		Tracef(" SendGuildChargeGSPPacket %d\n", dwMoney);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildDepositMoneyPacket(uint dwMoney)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_DEPOSIT_MONEY;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
		if (!Send(sizeof(uint), dwMoney))
		{
			return false;
		}
    
		Tracef(" SendGuildDepositMoneyPacket %d\n", dwMoney);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGuildWithdrawMoneyPacket(uint dwMoney)
	{
		command_guild GuildPacket = new command_guild();
		GuildPacket.byHeader = LG_HEADER_CG_GUILD;
		GuildPacket.bySubHeader = GUILD_SUBLG_HEADER_CG_WITHDRAW_MONEY;
		if (!Send(sizeof(command_guild), GuildPacket))
		{
			return false;
		}
		if (!Send(sizeof(uint), dwMoney))
		{
			return false;
		}
    
		Tracef(" SendGuildWithdrawMoneyPacket %d\n", dwMoney);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvGuild()
	{
		packet_guild GuildPacket = new packet_guild();
		if (!Recv(sizeof(packet_guild), GuildPacket))
		{
			return false;
		}
    
		switch (GuildPacket.subheader)
		{
			case GUILD_SUBLG_HEADER_GC_LOGIN:
			{
				uint dwPID;
				if (!Recv(sizeof(uint), dwPID))
				{
					return false;
				}
    
				SGuildMemberData pGuildMemberData;
				if (CPythonGuild.Instance().GetMemberDataPtrByPID(dwPID, pGuildMemberData))
				{
					if (0 != pGuildMemberData.strName.compare(CPythonPlayer.Instance().GetName()))
					{
						CPythonMessenger.Instance().LoginGuildMember(pGuildMemberData.strName.c_str());
					}
				}
    
				break;
			}
			case GUILD_SUBLG_HEADER_GC_LOGOUT:
			{
				uint dwPID;
				if (!Recv(sizeof(uint), dwPID))
				{
					return false;
				}
    
				SGuildMemberData pGuildMemberData;
				if (CPythonGuild.Instance().GetMemberDataPtrByPID(dwPID, pGuildMemberData))
				{
					if (0 != pGuildMemberData.strName.compare(CPythonPlayer.Instance().GetName()))
					{
						CPythonMessenger.Instance().LogoutGuildMember(pGuildMemberData.strName.c_str());
					}
				}
    
				break;
			}
			case GUILD_SUBLG_HEADER_GC_REMOVE:
			{
				uint dwPID;
				if (!Recv(sizeof(uint), dwPID))
				{
					return false;
				}
    
				if (CPythonGuild.Instance().IsMainPlayer(dwPID))
				{
					CPythonGuild.Instance().Destroy();
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "DeleteGuild", Py_BuildValue("()"));
					CPythonMessenger.Instance().RemoveAllGuildMember();
					__SetGuildID(0);
					__RefreshMessengerWindow();
					__RefreshTargetBoard();
					__RefreshCharacterWindow();
				}
				else
				{
					string strMemberName = "";
					SGuildMemberData pData;
					if (CPythonGuild.Instance().GetMemberDataPtrByPID(dwPID, pData))
					{
						strMemberName = pData.strName;
						CPythonMessenger.Instance().RemoveGuildMember(pData.strName.c_str());
					}
    
					CPythonGuild.Instance().RemoveMember(dwPID);
    
					__RefreshTargetBoardByName(strMemberName);
					__RefreshGuildWindowMemberPage();
				}
    
				Tracef(" <Remove> %d\n", dwPID);
				break;
			}
			case GUILD_SUBLG_HEADER_GC_LIST:
			{
				int iPacketSize = (int)GuildPacket.size - sizeof(packet_guild);
    
				for (; iPacketSize > 0;)
				{
					packet_guild_sub_member memberPacket = new packet_guild_sub_member();
					if (!Recv(sizeof(packet_guild_sub_member), memberPacket))
					{
						return false;
					}
    
					const string szName = "";
					if (memberPacket.byNameFlag)
					{
						if (!Recv(sizeof(char), szName))
						{
							return false;
						}
    
						iPacketSize -= DefineConstants.CHARACTER_NAME_MAX_LEN + 1;
					}
					else
					{
						SGuildMemberData pMemberData;
						if (CPythonGuild.Instance().GetMemberDataPtrByPID(memberPacket.pid, pMemberData))
						{
							strncpy(szName, pMemberData.strName.c_str(), DefineConstants.CHARACTER_NAME_MAX_LEN);
						}
					}
    
					CPythonGuild.SGuildMemberData GuildMemberData = new CPythonGuild.SGuildMemberData();
					GuildMemberData.dwPID = memberPacket.pid;
					GuildMemberData.byGrade = memberPacket.byGrade;
					GuildMemberData.strName = szName;
					GuildMemberData.byJob = memberPacket.byJob;
					GuildMemberData.byLevel = memberPacket.byLevel;
					GuildMemberData.dwOffer = memberPacket.dwOffer;
					GuildMemberData.byGeneralFlag = memberPacket.byIsGeneral;
					CPythonGuild.Instance().RegisterMember(GuildMemberData);
    
					if (strcmp(szName, CPythonPlayer.Instance().GetName()))
					{
						CPythonMessenger.Instance().AppendGuildMember(szName);
					}
    
					__RefreshTargetBoardByName(szName);
    
					iPacketSize -= sizeof(packet_guild_sub_member);
				}
    
				__RefreshGuildWindowInfoPage();
				__RefreshGuildWindowMemberPage();
				__RefreshMessengerWindow();
				__RefreshCharacterWindow();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_GRADE:
			{
				byte byCount;
				if (!Recv(sizeof(byte), byCount))
				{
					return false;
				}
    
				for (byte LaniatusDefVariables = 0; LaniatusDefVariables < byCount; ++i)
				{
					byte byIndex;
					if (!Recv(sizeof(byte), byIndex))
					{
						return false;
					}
					packet_guild_sub_grade GradePacket = new packet_guild_sub_grade();
					if (!Recv(sizeof(packet_guild_sub_grade), GradePacket))
					{
						return false;
					}
    
					CPythonGuild.Instance().SetGradeData(byIndex, CPythonGuild.SGuildGradeData(GradePacket.auth_flag, GradePacket.grade_name));
				}
				__RefreshGuildWindowGradePage();
				__RefreshGuildWindowMemberPageGradeComboBox();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_GRADE_NAME:
			{
				byte byGradeNumber;
				if (!Recv(sizeof(byte), byGradeNumber))
				{
					return false;
				}
    
				const string szGradeName = "";
				if (!Recv(sizeof(char), szGradeName))
				{
					return false;
				}
    
				CPythonGuild.Instance().SetGradeName(byGradeNumber, szGradeName);
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildGrade", Py_BuildValue("()"));
    
				Tracef(" <Change Grade Name> %d, %s\n", byGradeNumber, szGradeName);
				__RefreshGuildWindowGradePage();
				__RefreshGuildWindowMemberPageGradeComboBox();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_GRADE_AUTH:
			{
				byte byGradeNumber;
				if (!Recv(sizeof(byte), byGradeNumber))
				{
					return false;
				}
				byte byAuthorityFlag;
				if (!Recv(sizeof(byte), byAuthorityFlag))
				{
					return false;
				}
    
				CPythonGuild.Instance().SetGradeAuthority(byGradeNumber, byAuthorityFlag);
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshGuildGrade", Py_BuildValue("()"));
    
				Tracef(" <Change Grade Authority> %d, %d\n", byGradeNumber, byAuthorityFlag);
				__RefreshGuildWindowGradePage();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_INFO:
			{
				packet_guild_sub_info GuildInfo = new packet_guild_sub_info();
				if (!Recv(sizeof(packet_guild_sub_info), GuildInfo))
				{
					return false;
				}
    
				CPythonGuild.Instance().EnableGuild();
				SGulidInfo rGuildInfo = CPythonGuild.Instance().GetGuildInfoRef();
				strncpy(rGuildInfo.szGuildName, GuildInfo.name, GUILD_NAME_MAX_LEN);
				rGuildInfo.szGuildName[GUILD_NAME_MAX_LEN] = '\0';
    
				rGuildInfo.dwGuildID = GuildInfo.guild_id;
				rGuildInfo.dwMasterPID = GuildInfo.master_pid;
				rGuildInfo.dwGuildLevel = GuildInfo.level;
				rGuildInfo.dwCurrentExperience = GuildInfo.exp;
				rGuildInfo.dwCurrentMemberCount = GuildInfo.member_count;
				rGuildInfo.dwMaxMemberCount = GuildInfo.max_member_count;
				rGuildInfo.dwGuildMoney = GuildInfo.gold;
				rGuildInfo.bHasLand = GuildInfo.hasLand;
    
				__RefreshGuildWindowInfoPage();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_COMMENTS:
			{
				byte byCount;
				if (!Recv(sizeof(byte), byCount))
				{
					return false;
				}
    
				CPythonGuild.Instance().ClearComment();
    
				for (byte LaniatusDefVariables = 0; LaniatusDefVariables < byCount; ++i)
				{
					uint dwCommentID;
					if (!Recv(sizeof(uint), dwCommentID))
					{
						return false;
					}
    
					const string szName = "";
					if (!Recv(sizeof(char), szName))
					{
						return false;
					}
    
					const string szComment = "";
					if (!Recv(sizeof(char), szComment))
					{
						return false;
					}
    
					CPythonGuild.Instance().RegisterComment(dwCommentID, szName, szComment);
				}
    
				__RefreshGuildWindowBoardPage();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_CHANGE_EXP:
			{
				byte byLevel;
				if (!Recv(sizeof(byte), byLevel))
				{
					return false;
				}
				uint dwEXP;
				if (!Recv(sizeof(uint), dwEXP))
				{
					return false;
				}
				CPythonGuild.Instance().SetGuildEXP(byLevel, dwEXP);
				Tracef(" <ChangeEXP> %d, %d\n", byLevel, dwEXP);
				__RefreshGuildWindowInfoPage();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_CHANGE_MEMBER_GRADE:
			{
				uint dwPID;
				if (!Recv(sizeof(uint), dwPID))
				{
					return false;
				}
				byte byGrade;
				if (!Recv(sizeof(byte), byGrade))
				{
					return false;
				}
				CPythonGuild.Instance().ChangeGuildMemberGrade(dwPID, byGrade);
				Tracef(" <ChangeMemberGrade> %d, %d\n", dwPID, byGrade);
				__RefreshGuildWindowMemberPage();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_SKILL_INFO:
			{
				SGuildSkillData rSkillData = CPythonGuild.Instance().GetGuildSkillDataRef();
				if (!Recv(sizeof(rSkillData.bySkillPoint), rSkillData.bySkillPoint))
				{
					return false;
				}
				if (!Recv(sizeof(rSkillData.bySkillLevel), rSkillData.bySkillLevel))
				{
					return false;
				}
				if (!Recv(sizeof(rSkillData.wGuildPoint), rSkillData.wGuildPoint))
				{
					return false;
				}
				if (!Recv(sizeof(rSkillData.wMaxGuildPoint), rSkillData.wMaxGuildPoint))
				{
					return false;
				}
    
				Tracef(" <SkillInfo> %d / %d, %d\n", rSkillData.bySkillPoint, rSkillData.wGuildPoint, rSkillData.wMaxGuildPoint);
				__RefreshGuildWindowSkillPage();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_CHANGE_MEMBER_GENERAL:
			{
				uint dwPID;
				if (!Recv(sizeof(uint), dwPID))
				{
					return false;
				}
				byte byFlag;
				if (!Recv(sizeof(byte), byFlag))
				{
					return false;
				}
    
				CPythonGuild.Instance().ChangeGuildMemberGeneralFlag(dwPID, byFlag);
				Tracef(" <ChangeMemberGeneralFlag> %d, %d\n", dwPID, byFlag);
				__RefreshGuildWindowMemberPage();
				break;
			}
			case GUILD_SUBLG_HEADER_GC_GUILD_INVITE:
			{
				uint dwGuildID;
				if (!Recv(sizeof(uint), dwGuildID))
				{
					return false;
				}
				string szGuildName = new string(new char[GUILD_NAME_MAX_LEN + 1]);
				if (!Recv(GUILD_NAME_MAX_LEN, szGuildName))
				{
					return false;
				}
    
				szGuildName = szGuildName.Substring(0, GUILD_NAME_MAX_LEN);
    
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RecvGuildInviteQuestion", Py_BuildValue("(is)", dwGuildID, szGuildName));
				Tracef(" <Guild Invite> %d, %s\n", dwGuildID, szGuildName);
				break;
			}
			case GUILD_SUBLG_HEADER_GC_WAR:
			{
				packet_guild_war kGuildWar = new packet_guild_war();
				if (!Recv(sizeof(packet_guild_war), kGuildWar))
				{
					return false;
				}
    
				switch (kGuildWar.bWarState)
				{
					case GUILD_WAR_SEND_DECLARE:
						Tracef(" >> GUILD_SUBLG_HEADER_GC_WAR : GUILD_WAR_SEND_DECLARE\n");
						PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_GuildWar_OnSendDeclare", Py_BuildValue("(i)", kGuildWar.dwGuildOpp));
						break;
					case GUILD_WAR_RECV_DECLARE:
						Tracef(" >> GUILD_SUBLG_HEADER_GC_WAR : GUILD_WAR_RECV_DECLARE\n");
						PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_GuildWar_OnRecvDeclare", Py_BuildValue("(ii)", kGuildWar.dwGuildOpp, kGuildWar.bType));
						break;
					case GUILD_WAR_ON_WAR:
						Tracef(" >> GUILD_SUBLG_HEADER_GC_WAR : GUILD_WAR_ON_WAR : %d, %d\n", kGuildWar.dwGuildSelf, kGuildWar.dwGuildOpp);
						PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_GuildWar_OnStart", Py_BuildValue("(ii)", kGuildWar.dwGuildSelf, kGuildWar.dwGuildOpp));
						CPythonGuild.Instance().StartGuildWar(kGuildWar.dwGuildOpp);
						break;
					case GUILD_WAR_END:
						Tracef(" >> GUILD_SUBLG_HEADER_GC_WAR : GUILD_WAR_END\n");
						PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_GuildWar_OnEnd", Py_BuildValue("(ii)", kGuildWar.dwGuildSelf, kGuildWar.dwGuildOpp));
						CPythonGuild.Instance().EndGuildWar(kGuildWar.dwGuildOpp);
						break;
				}
				break;
			}
			case GUILD_SUBLG_HEADER_GC_GUILD_NAME:
			{
				uint dwID;
				string szGuildName = new string(new char[GUILD_NAME_MAX_LEN + 1]);
    
				int iPacketSize = (int)GuildPacket.size - sizeof(packet_guild);
    
				int nItemSize = sizeof(uint) + GUILD_NAME_MAX_LEN;
    
				Debug.Assert(iPacketSize % nItemSize == 0 && "GUILD_SUBLG_HEADER_GC_GUILD_NAME");
    
				for (; iPacketSize > 0;)
				{
					if (!Recv(sizeof(uint), dwID))
					{
						return false;
					}
    
					if (!Recv(GUILD_NAME_MAX_LEN, szGuildName))
					{
						return false;
					}
    
					szGuildName = szGuildName.Substring(0, GUILD_NAME_MAX_LEN);
    
					CPythonGuild.Instance().RegisterGuildName(dwID, szGuildName);
					iPacketSize -= nItemSize;
				}
				break;
			}
			case GUILD_SUBLG_HEADER_GC_GUILD_WAR_LIST:
			{
				uint dwSrcGuildID;
				uint dwDstGuildID;
    
				int iPacketSize = (int)GuildPacket.size - sizeof(packet_guild);
				int nItemSize = sizeof(uint) + sizeof(uint);
    
				Debug.Assert(iPacketSize % nItemSize == 0 && "GUILD_SUBLG_HEADER_GC_GUILD_WAR_LIST");
    
				for (; iPacketSize > 0;)
				{
					if (!Recv(sizeof(uint), dwSrcGuildID))
					{
						return false;
					}
    
					if (!Recv(sizeof(uint), dwDstGuildID))
					{
						return false;
					}
    
					Tracef(" >> GulidWarList [%d vs %d]\n", dwSrcGuildID, dwDstGuildID);
					CInstanceBase.InsertGVGKey(dwSrcGuildID, dwDstGuildID);
					CPythonCharacterManager.Instance().ChangeGVG(dwSrcGuildID, dwDstGuildID);
					iPacketSize -= nItemSize;
				}
				break;
			}
			case GUILD_SUBLG_HEADER_GC_GUILD_WAR_END_LIST:
			{
				uint dwSrcGuildID;
				uint dwDstGuildID;
    
				int iPacketSize = (int)GuildPacket.size - sizeof(packet_guild);
				int nItemSize = sizeof(uint) + sizeof(uint);
    
				Debug.Assert(iPacketSize % nItemSize == 0 && "GUILD_SUBLG_HEADER_GC_GUILD_WAR_END_LIST");
    
				for (; iPacketSize > 0;)
				{
    
					if (!Recv(sizeof(uint), dwSrcGuildID))
					{
						return false;
					}
    
					if (!Recv(sizeof(uint), dwDstGuildID))
					{
						return false;
					}
    
					Tracef(" >> GulidWarEndList [%d vs %d]\n", dwSrcGuildID, dwDstGuildID);
					CInstanceBase.RemoveGVGKey(dwSrcGuildID, dwDstGuildID);
					CPythonCharacterManager.Instance().ChangeGVG(dwSrcGuildID, dwDstGuildID);
					iPacketSize -= nItemSize;
				}
				break;
			}
			case GUILD_SUBLG_HEADER_GC_WAR_POINT:
			{
				SPacketGuildWarPoint GuildWarPoint = new SPacketGuildWarPoint();
				if (!Recv(sizeof(SPacketGuildWarPoint), GuildWarPoint))
				{
					return false;
				}
    
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_GuildWar_OnRecvPoint", Py_BuildValue("(iii)", GuildWarPoint.dwGainGuildID, GuildWarPoint.dwOpponentGuildID, GuildWarPoint.lPoint));
				break;
			}
			case GUILD_SUBLG_HEADER_GC_MONEY_CHANGE:
			{
				uint dwMoney;
				if (!Recv(sizeof(uint), dwMoney))
				{
					return false;
				}
    
				CPythonGuild.Instance().SetGuildMoney(dwMoney);
    
				__RefreshGuildWindowInfoPage();
				Tracef(" >> Guild Money Change : %d\n", dwMoney);
				break;
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendFishingPacket(int iRotation)
	{
		byte byHeader = LG_HEADER_CG_FISHING;
		if (!Send(sizeof(byte), byHeader))
		{
			return false;
		}
		byte byPacketRotation = (byte)(iRotation / 5);
		if (!Send(sizeof(byte), byPacketRotation))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendGiveItemPacket(uint dwTargetVID, TItemPos ItemPos, int iItemCount)
	{
		command_give_item GiveItemPacket = new command_give_item();
		GiveItemPacket.byHeader = LG_HEADER_CG_GIVE_ITEM;
		GiveItemPacket.dwTargetVID = dwTargetVID;
		GiveItemPacket.ItemPos = ItemPos;
		GiveItemPacket.byItemCount = iItemCount;
    
		if (!Send(sizeof(command_give_item), GiveItemPacket))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvFishing()
	{
		packet_fishing FishingPacket = new packet_fishing();
		if (!Recv(sizeof(packet_fishing), FishingPacket))
		{
			return false;
		}
    
		CInstanceBase pFishingInstance = null;
		if (FISHING_SUBLG_HEADER_GC_FISH != FishingPacket.subheader)
		{
			pFishingInstance = CPythonCharacterManager.Instance().GetInstancePtr(FishingPacket.info);
			if (pFishingInstance == null)
			{
				return true;
			}
		}
    
		switch (FishingPacket.subheader)
		{
			case FISHING_SUBLG_HEADER_GC_START:
				pFishingInstance.StartFishing((float)FishingPacket.dir * 5.0f);
				break;
			case FISHING_SUBLG_HEADER_GC_STOP:
				if (pFishingInstance.IsFishing())
				{
					pFishingInstance.StopFishing();
				}
				break;
			case FISHING_SUBLG_HEADER_GC_REACT:
				if (pFishingInstance.IsFishing())
				{
					pFishingInstance.SetFishEmoticon();
					pFishingInstance.ReactFishing();
				}
				break;
			case FISHING_SUBLG_HEADER_GC_SUCCESS:
				pFishingInstance.CatchSuccess();
				break;
			case FISHING_SUBLG_HEADER_GC_FAIL:
				pFishingInstance.CatchFail();
				if (pFishingInstance == CPythonCharacterManager.Instance().GetMainInstancePtr())
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnFishingFailure", Py_BuildValue("()"));
				}
				break;
			case FISHING_SUBLG_HEADER_GC_FISH:
			{
				uint dwFishID = FishingPacket.info;
    
				if (0 == FishingPacket.info)
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnFishingNotifyUnknown", Py_BuildValue("()"));
					return true;
				}
    
				CItemData pItemData;
				if (!CItemManager.Instance().GetItemDataPointer(dwFishID, pItemData))
				{
					return true;
				}
    
				CInstanceBase pMainInstance = CPythonCharacterManager.Instance().GetMainInstancePtr();
				if (pMainInstance == null)
				{
					return true;
				}
    
				if (pMainInstance.IsFishing())
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnFishingNotify", Py_BuildValue("(is)", CItemData.ITEM_TYPE_FISH == pItemData.GetType(), pItemData.GetName()));
				}
				else
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnFishingSuccess", Py_BuildValue("(is)", CItemData.ITEM_TYPE_FISH == pItemData.GetType(), pItemData.GetName()));
				}
				break;
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvDungeon()
	{
		packet_dungeon DungeonPacket = new packet_dungeon();
		if (!Recv(sizeof(packet_dungeon), DungeonPacket))
		{
			return false;
		}
    
		switch (DungeonPacket.subheader)
		{
			case DUNGEON_SUBLG_HEADER_GC_TIME_ATTACK_START:
			{
				break;
			}
			case DUNGEON_SUBLG_HEADER_GC_DESTINATION_POSITION:
			{
				uint ulx;
				uint uly;
				if (!Recv(sizeof(uint), ulx))
				{
					return false;
				}
				if (!Recv(sizeof(uint), uly))
				{
					return false;
				}
    
				CPythonPlayer.Instance().SetDungeonDestinationPosition(ulx, uly);
				break;
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendBuildPrivateShopPacket(string c_szName, in List<SShopItemTable> c_rSellingItemStock)
	{
		SPacketCGMyShop packet = new SPacketCGMyShop();
		packet.bHeader = LG_HEADER_CG_MYSHOP;
		strncpy(packet.szSign, c_szName, SHOP_SIGN_MAX_LEN);
		packet.wCount = c_rSellingItemStock.Count;
		if (!Send(sizeof(SPacketCGMyShop), packet))
		{
			return false;
		}
    
		foreach (SShopItemTable itor in c_rSellingItemStock)
		{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
	//Original Metin2 CPlus Line: const SShopItemTable & c_rItem = itor;
			SShopItemTable c_rItem = itor;
			if (!Send(sizeof(SShopItemTable), c_rItem))
			{
				return false;
			}
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvShopSignPacket()
	{
		SPacketGCShopSign p = new SPacketGCShopSign();
		if (!Recv(sizeof(SPacketGCShopSign), p))
		{
			return false;
		}
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
    
		if (0 == strlen(p.szSign))
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Disappear", Py_BuildValue("(i)", p.dwVID));
    
			if (rkPlayer.IsMainCharacterIndex(p.dwVID))
			{
				rkPlayer.ClosePrivateShop();
			}
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Appear", Py_BuildValue("(is)", p.dwVID, p.szSign));
    
			if (rkPlayer.IsMainCharacterIndex(p.dwVID))
			{
				rkPlayer.OpenPrivateShop();
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvTimePacket()
	{
		SPacketGCTime TimePacket = new SPacketGCTime();
		if (!Recv(sizeof(SPacketGCTime), TimePacket))
		{
			return false;
		}
    
		IAbstractApplication rkApp = IAbstractApplication.GetSingleton();
		rkApp.SetServerTime(TimePacket.time);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvWalkModePacket()
	{
		SPacketGCWalkMode WalkModePacket = new SPacketGCWalkMode();
		if (!Recv(sizeof(SPacketGCWalkMode), WalkModePacket))
		{
			return false;
		}
    
		CInstanceBase pInstance = CPythonCharacterManager.Instance().GetInstancePtr(WalkModePacket.vid);
		if (pInstance != null)
		{
			if (WALKMODE_RUN == WalkModePacket.mode)
			{
				pInstance.SetRunMode();
			}
			else
			{
				pInstance.SetWalkMode();
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvChangeSkillGroupPacket()
	{
		SPacketGCChangeSkillGroup ChangeSkillGroup = new SPacketGCChangeSkillGroup();
		if (!Recv(sizeof(SPacketGCChangeSkillGroup), ChangeSkillGroup))
		{
			return false;
		}
    
		m_dwMainActorSkillGroup = ChangeSkillGroup.skill_group;
    
		CPythonPlayer.Instance().NEW_ClearSkillData();
		__RefreshCharacterWindow();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __TEST_SetSkillGroupFake(int iIndex)
	{
		m_dwMainActorSkillGroup = (uint)iIndex;
    
		CPythonPlayer.Instance().NEW_ClearSkillData();
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshCharacter", Py_BuildValue("()"));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendRefinePacket(byte byPos, byte byType)
	{
		SPacketCGRefine kRefinePacket = new SPacketCGRefine();
		kRefinePacket.header = LG_HEADER_CG_REFINE;
		kRefinePacket.pos = byPos;
		kRefinePacket.type = byType;
    
		if (!Send(sizeof(SPacketCGRefine), kRefinePacket))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSelectItemPacket(uint dwItemPos)
	{
		command_script_select_item kScriptSelectItem = new command_script_select_item();
		kScriptSelectItem.header = LG_HEADER_CG_SCRIPT_SELECT_ITEM;
		kScriptSelectItem.selection = dwItemPos;
    
		if (!Send(sizeof(command_script_select_item), kScriptSelectItem))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvRefineInformationPacket()
	{
		SPacketGCRefineInformation kRefineInfoPacket = new SPacketGCRefineInformation();
		if (!Recv(sizeof(SPacketGCRefineInformation), kRefineInfoPacket))
		{
			return false;
		}
    
		SRefineTable rkRefineTable = kRefineInfoPacket.refine_table;
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OpenRefineDialog", Py_BuildValue("(iiLi)", kRefineInfoPacket.pos, kRefineInfoPacket.refine_table.result_vnum, rkRefineTable.cost, rkRefineTable.prob));
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < rkRefineTable.material_count; ++i)
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "AppendMaterialToRefineDialog", Py_BuildValue("(ii)", rkRefineTable.materials[LaniatusDefVariables].vnum, rkRefineTable.materials[LaniatusDefVariables].count));
		}
    
	#if DEBUG
		Tracef(" >> RecvRefineInformationPacket(pos=%d, result_vnum=%d, cost=%lld, prob=%d)\n", kRefineInfoPacket.pos, kRefineInfoPacket.refine_table.result_vnum, rkRefineTable.cost, rkRefineTable.prob);
	#endif
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvRefineInformationPacketNew()
	{
		SPacketGCRefineInformationNew kRefineInfoPacket = new SPacketGCRefineInformationNew();
		if (!Recv(sizeof(SPacketGCRefineInformationNew), kRefineInfoPacket))
		{
			return false;
		}
    
		SRefineTable rkRefineTable = kRefineInfoPacket.refine_table;
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OpenRefineDialog", Py_BuildValue("(iiLii)", kRefineInfoPacket.pos, kRefineInfoPacket.refine_table.result_vnum, rkRefineTable.cost, rkRefineTable.prob, kRefineInfoPacket.type));
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < rkRefineTable.material_count; ++i)
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "AppendMaterialToRefineDialog", Py_BuildValue("(ii)", rkRefineTable.materials[LaniatusDefVariables].vnum, rkRefineTable.materials[LaniatusDefVariables].count));
		}
    
	#if DEBUG
		Tracef(" >> RecvRefineInformationPacketNew(pos=%d, result_vnum=%d, cost=%lld, prob=%d, type=%d)\n", kRefineInfoPacket.pos, kRefineInfoPacket.refine_table.result_vnum, rkRefineTable.cost, rkRefineTable.prob, kRefineInfoPacket.type);
	#endif
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvNPCList()
	{
		SPacketGCNPCPosition kNPCPosition = new SPacketGCNPCPosition();
		if (!Recv(sizeof(SPacketGCNPCPosition), kNPCPosition))
		{
			return false;
		}
    
		Debug.Assert((int)kNPCPosition.size - sizeof(SPacketGCNPCPosition) == kNPCPosition.count * sizeof(TNPCPosition) && "LG_HEADER_GC_NPC_POSITION");
    
		CPythonMiniMap.Instance().ClearAtlasMarkInfo();
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < kNPCPosition.count; ++i)
		{
			TNPCPosition NPCPosition = new TNPCPosition();
			if (!Recv(sizeof(TNPCPosition), NPCPosition))
			{
				return false;
			}
    
			CPythonMiniMap.Instance().RegisterAtlasMark(NPCPosition.bType, NPCPosition.name, NPCPosition.x, NPCPosition.y);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __SendCRCReportPacket()
	{
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendClientVersionPacket()
	{
		string filename = "";
    
		GetExcutedFileName(filename);
    
		filename = CFileNameHelper.NoPath(filename);
		CFileNameHelper.ChangeDosPath(filename);
    
		command_client_version kVersionPacket = new command_client_version();
		kVersionPacket.header = LG_HEADER_CG_CLIENT_VERSION;
		strncpy(kVersionPacket.filename, filename, sizeof(kVersionPacket.filename) - 1);
		strncpy(kVersionPacket.timestamp, DefineConstants.CLIENT_VERSION, sizeof(kVersionPacket.timestamp) - 1);
    
		if (!Send(sizeof(command_client_version), kVersionPacket))
		{
			Tracef("SendClientReportPacket Error");
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvAffectAddPacket()
	{
		TPacketGCAffectAdd kAffectAdd = new TPacketGCAffectAdd();
		if (!Recv(sizeof(TPacketGCAffectAdd), kAffectAdd))
		{
			return false;
		}
    
		TPacketAffectElement rkElement = kAffectAdd.elem;
		if (rkElement.bPointIdxApplyOn == POINT_ENERGY)
		{
			CPythonPlayer.instance().SetStatus(POINT_ENERGY_END_TIME, CPythonApplication.Instance().GetServerTimeStamp() + rkElement.lDuration);
			__RefreshStatus();
		}
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_NEW_AddAffect", Py_BuildValue("(iiii)", rkElement.dwType, rkElement.bPointIdxApplyOn, rkElement.lApplyValue, rkElement.lDuration));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvAffectRemovePacket()
	{
		TPacketGCAffectRemove kAffectRemove = new TPacketGCAffectRemove();
		if (!Recv(sizeof(TPacketGCAffectRemove), kAffectRemove))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_NEW_RemoveAffect", Py_BuildValue("(ii)", kAffectRemove.dwType, kAffectRemove.bApplyOn));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvChannelPacket()
	{
		packet_channel kChannelPacket = new packet_channel();
		if (!Recv(sizeof(packet_channel), kChannelPacket))
		{
			return false;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvViewEquipPacket()
	{
		packet_view_equip kViewEquipPacket = new packet_view_equip();
		if (!Recv(sizeof(packet_view_equip), kViewEquipPacket))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OpenEquipmentDialog", Py_BuildValue("(i)", kViewEquipPacket.dwVID));
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < WEAR_MAX_NUM; ++i)
		{
			SEquipmentItemSet rItemSet = kViewEquipPacket.equips[LaniatusDefVariables];
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "SetEquipmentDialogItem", Py_BuildValue("(iiii)", kViewEquipPacket.dwVID, i, rItemSet.vnum, rItemSet.count));
    
			for (int j = 0; j < ITEM_SOCKET_SLOT_MAX_NUM; ++j)
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "SetEquipmentDialogSocket", Py_BuildValue("(iiii)", kViewEquipPacket.dwVID, i, j, rItemSet.alSockets[j]));
			}
    
			for (int k = 0; k < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++k)
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "SetEquipmentDialogAttr", Py_BuildValue("(iiiii)", kViewEquipPacket.dwVID, i, k, rItemSet.aAttr[k].bType, rItemSet.aAttr[k].sValue));
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvLandPacket()
	{
		packet_land_list kLandList = new packet_land_list();
		if (!Recv(sizeof(packet_land_list), kLandList))
		{
			return false;
		}
    
		List<uint> kVec_dwGuildID = new List<uint>();
    
		CPythonMiniMap rkMiniMap = CPythonMiniMap.Instance();
		CPythonBackground rkBG = CPythonBackground.Instance();
		CInstanceBase pMainInstance = CPythonPlayer.Instance().NEW_GetMainActorPtr();
    
		rkMiniMap.ClearGuildArea();
		rkBG.ClearGuildArea();
    
		int iPacketSize = (kLandList.size - sizeof(packet_land_list));
		for (; iPacketSize > 0; iPacketSize -= sizeof(TLandPacketElement))
		{
			TLandPacketElement kElement = new TLandPacketElement();
			if (!Recv(sizeof(TLandPacketElement), kElement))
			{
				return false;
			}
    
			rkMiniMap.RegisterGuildArea(kElement.dwID, kElement.dwGuildID, kElement.x, kElement.y, kElement.width, kElement.height);
    
			if (pMainInstance != null)
			{
			if (kElement.dwGuildID == pMainInstance.GetGuildID())
			{
				rkBG.RegisterGuildArea(kElement.x, kElement.y, kElement.x + kElement.width, kElement.y + kElement.height);
			}
			}
    
			if (0 != kElement.dwGuildID)
			{
				kVec_dwGuildID.Add(kElement.dwGuildID);
			}
		}
    
		if (kVec_dwGuildID.Count > 0)
		{
			__DownloadSymbol(kVec_dwGuildID);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvTargetCreatePacket()
	{
		TPacketGCTargetCreate kTargetCreate = new TPacketGCTargetCreate();
		if (!Recv(sizeof(TPacketGCTargetCreate), kTargetCreate))
		{
			return false;
		}
    
		CPythonMiniMap rkpyMiniMap = CPythonMiniMap.Instance();
		rkpyMiniMap.CreateTarget(kTargetCreate.lID, kTargetCreate.szTargetName);
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_OpenAtlasWindow", Py_BuildValue("()"));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvTargetCreatePacketNew()
	{
		TPacketGCTargetCreateNew kTargetCreate = new TPacketGCTargetCreateNew();
		if (!Recv(sizeof(TPacketGCTargetCreateNew), kTargetCreate))
		{
			return false;
		}
    
		CPythonMiniMap rkpyMiniMap = CPythonMiniMap.Instance();
		CPythonBackground rkpyBG = CPythonBackground.Instance();
		if (CREATE_TARGET_TYPE_LOCATION == kTargetCreate.byType)
		{
			rkpyMiniMap.CreateTarget(kTargetCreate.lID, kTargetCreate.szTargetName);
		}
		else
		{
			rkpyMiniMap.CreateTarget(kTargetCreate.lID, kTargetCreate.szTargetName, kTargetCreate.dwVID);
			rkpyBG.CreateTargetEffect(kTargetCreate.lID, kTargetCreate.dwVID);
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_OpenAtlasWindow", Py_BuildValue("()"));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvTargetUpdatePacket()
	{
		TPacketGCTargetUpdate kTargetUpdate = new TPacketGCTargetUpdate();
		if (!Recv(sizeof(TPacketGCTargetUpdate), kTargetUpdate))
		{
			return false;
		}
    
		CPythonMiniMap rkpyMiniMap = CPythonMiniMap.Instance();
		rkpyMiniMap.UpdateTarget(kTargetUpdate.lID, kTargetUpdate.lX, kTargetUpdate.lY);
    
		CPythonBackground rkpyBG = CPythonBackground.Instance();
		rkpyBG.CreateTargetEffect(kTargetUpdate.lID, kTargetUpdate.lX, kTargetUpdate.lY);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvTargetDeletePacket()
	{
		TPacketGCTargetDelete kTargetDelete = new TPacketGCTargetDelete();
		if (!Recv(sizeof(TPacketGCTargetDelete), kTargetDelete))
		{
			return false;
		}
    
		CPythonMiniMap rkpyMiniMap = CPythonMiniMap.Instance();
		rkpyMiniMap.DeleteTarget(kTargetDelete.lID);
    
		CPythonBackground rkpyBG = CPythonBackground.Instance();
		rkpyBG.DeleteTargetEffect(kTargetDelete.lID);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvLoverInfoPacket()
	{
		packet_lover_info kLoverInfo = new packet_lover_info();
		if (!Recv(sizeof(packet_lover_info), kLoverInfo))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_LoverInfo", Py_BuildValue("(si)", kLoverInfo.szName, kLoverInfo.byLovePoint));
	#if DEBUG
		Tracef("RECV LOVER INFO : %s, %d\n", kLoverInfo.szName, kLoverInfo.byLovePoint);
	#endif
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvLovePointUpdatePacket()
	{
		packet_love_point_update kLovePointUpdate = new packet_love_point_update();
		if (!Recv(sizeof(packet_love_point_update), kLovePointUpdate))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_UpdateLovePoint", Py_BuildValue("(i)", kLovePointUpdate.byLovePoint));
	#if DEBUG
		Tracef("RECV LOVE POINT UPDATE : %d\n", kLovePointUpdate.byLovePoint);
	#endif
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvDigMotionPacket()
	{
		packet_dig_motion kDigMotion = new packet_dig_motion();
		if (!Recv(sizeof(packet_dig_motion), kDigMotion))
		{
			return false;
		}
    
	#if DEBUG
		Tracef(" Dig Motion [%d/%d]\n", kDigMotion.vid, kDigMotion.count);
	#endif
    
		IAbstractCharacterManager rkChrMgr = IAbstractCharacterManager.GetSingleton();
		CInstanceBase pkInstMain = rkChrMgr.GetInstancePtr(kDigMotion.vid);
		CInstanceBase pkInstTarget = rkChrMgr.GetInstancePtr(kDigMotion.target_vid);
		if (null == pkInstMain)
		{
			return true;
		}
    
		if (pkInstTarget != null)
		{
			pkInstMain.NEW_LookAtDestInstance(pkInstTarget);
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < kDigMotion.count; ++i)
		{
			pkInstMain.PushOnceMotion(CRaceMotionData.NAME_DIG);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendDragonSoulRefinePacket(byte bRefineType, TItemPos pos)
	{
		SPacketCGDragonSoulRefine pk = new SPacketCGDragonSoulRefine();
		pk.header = LG_HEADER_CG_DRAGON_SOUL_REFINE;
		pk.bSubType = bRefineType;
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(pk.ItemGrid, pos, sizeof(TItemPos) * DS_REFINE_WINDOW_MAX_NUM);
		if (!Send(sizeof(SPacketCGDragonSoulRefine), pk))
		{
			return false;
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendChangeLanguagePacket(byte bLanguage)
	{
		SPacketChangeLanguage packet = new SPacketChangeLanguage();
		packet.bHeader = LG_HEADER_CG_CHANGE_LANGUAGE;
		packet.bLanguage = bLanguage;
    
		if (!Send(sizeof(SPacketChangeLanguage), packet))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvRequestChangeLanguage()
	{
		SPacketChangeLanguage packet = new SPacketChangeLanguage();
		if (!Recv(sizeof(SPacketChangeLanguage), packet))
		{
			return false;
		}
    
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CInstanceBase pkInstMain = rkChrMgr.GetMainInstancePtr();
    
		if (pkInstMain == null)
		{
			TraceError("CPythonNetworkStream::RecvRequestChangeLanguage - MainCharacter is NULL");
			return false;
		}
    
		pkInstMain.SetLanguage(packet.bLanguage);
		pkInstMain.Update();
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_RequestChangeLanguage", Py_BuildValue("(i)", packet.bLanguage));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendWhisperDetails(string name)
	{
		SPacketCGWhisperDetails packet = new SPacketCGWhisperDetails();
		packet.header = LG_HEADER_CG_WHISPER_DETAILS;
		strncpy(packet.name, name, sizeof(packet.name) - 1);
		if (!Send(sizeof(SPacketCGWhisperDetails), packet))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvWhisperDetails()
	{
		SPacketGCWhisperDetails packet = new SPacketGCWhisperDetails();
		if (!Recv(sizeof(SPacketGCWhisperDetails), packet))
		{
			return false;
		}
    
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_RecieveWhisperDetails", Py_BuildValue("(si)", packet.name, packet.bLanguage));
	#else
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_RecieveWhisperDetails", Py_BuildValue("(s)", packet.name));
	#endif
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __GlobalPositionToLocalPosition(ref int rGlobalX, ref int rGlobalY)
	{
		CPythonBackground rkBgMgr = CPythonBackground.Instance();
		rkBgMgr.GlobalPositionToLocalPosition(rGlobalX, rGlobalY);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __LocalPositionToGlobalPosition(ref int rLocalX, ref int rLocalY)
	{
		CPythonBackground rkBgMgr = CPythonBackground.Instance();
		rkBgMgr.LocalPositionToGlobalPosition(rLocalX, rLocalY);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __CanActMainInstance()
	{
		CPythonCharacterManager rkChrMgr = CPythonCharacterManager.Instance();
		CInstanceBase pkInstMain = rkChrMgr.GetMainInstancePtr();
		if (pkInstMain == null)
		{
			return false;
		}
    
		return pkInstMain.CanAct();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __ClearNetworkActorManager()
	{
		m_rokNetActorMgr.Destroy();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCharacterAppendPacket()
	{
		packet_add_char chrAddPacket = new packet_add_char();
		if (!Recv(sizeof(packet_add_char), chrAddPacket))
		{
			return false;
		}
    
		__GlobalPositionToLocalPosition(chrAddPacket.x, chrAddPacket.y);
    
		SNetworkActorData kNetActorData = new SNetworkActorData();
		kNetActorData.m_bType = chrAddPacket.bType;
		kNetActorData.m_dwMovSpd = chrAddPacket.bMovingSpeed;
		kNetActorData.m_dwAtkSpd = chrAddPacket.bAttackSpeed;
		kNetActorData.m_dwRace = chrAddPacket.wRaceNum;
    
		kNetActorData.m_dwStateFlags = chrAddPacket.bStateFlag;
		kNetActorData.m_dwVID = chrAddPacket.dwVID;
		kNetActorData.m_fRot = chrAddPacket.angle;
    
		kNetActorData.m_stName = "";
    
		kNetActorData.m_stName = "";
		kNetActorData.m_kAffectFlags.CopyData(0, sizeof(chrAddPacket.dwAffectFlag[0]), chrAddPacket.dwAffectFlag[0]);
		kNetActorData.m_kAffectFlags.CopyData(32, sizeof(chrAddPacket.dwAffectFlag[1]), chrAddPacket.dwAffectFlag[1]);
    
		kNetActorData.SetPosition(chrAddPacket.x, chrAddPacket.y);
    
		kNetActorData.m_sAlignment = 0;
		kNetActorData.m_byPKMode = 0;
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
		kNetActorData.m_bLanguage = 0;
	#endif
		kNetActorData.m_dwGuildID = 0;
		kNetActorData.m_dwEmpireID = 0;
		kNetActorData.m_dwArmor = 0;
		kNetActorData.m_dwWeapon = 0;
		kNetActorData.m_dwHair = 0;
		kNetActorData.m_dwAcce = 0;
		kNetActorData.m_byAcceDrainRate = 0;
		kNetActorData.m_dwMountVnum = 0;
		kNetActorData.m_dwArrow = 0;
    
		kNetActorData.m_dwLevel = 0;
    
		if (kNetActorData.m_bType != CActorInstance.TYPE_PC && kNetActorData.m_bType != CActorInstance.TYPE_NPC && kNetActorData.m_bType != CActorInstance.TYPE_MOUNT && kNetActorData.m_bType != CActorInstance.TYPE_PET)
		{
			string c_szName;
			CPythonNonPlayer rkNonPlayer = CPythonNonPlayer.Instance();
			if (rkNonPlayer.GetName(kNetActorData.m_dwRace, c_szName))
			{
				kNetActorData.m_stName = c_szName;
			}
    
			__RecvCharacterAppendPacket(kNetActorData);
		}
		else
		{
			s_kNetActorData = kNetActorData;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCharacterAdditionalInfo()
	{
		packet_char_additional_info chrInfoPacket = new packet_char_additional_info();
		if (!Recv(sizeof(packet_char_additional_info), chrInfoPacket))
		{
			return false;
		}
    
    
		SNetworkActorData kNetActorData = s_kNetActorData;
		if (IsInvisibleRace(kNetActorData.m_dwRace))
		{
			return true;
		}
    
		if (kNetActorData.m_dwVID == chrInfoPacket.dwVID)
		{
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
			string c_szNpcClientName;
			if (kNetActorData.m_bType == CActorInstance.TYPE_NPC && kNetActorData.m_dwRace != 30000)
			{
				if (kNetActorData.m_dwRace > 34000 && kNetActorData.m_dwRace < 35000 || kNetActorData.m_dwRace > 20100 && kNetActorData.m_dwRace < 20110)
				{
					string szPetName = new string(new char[DefineConstants.CHARACTER_NAME_MAX_LEN]);
					if (CPythonNonPlayer.Instance().GetName(kNetActorData.m_dwRace, c_szNpcClientName))
					{
						sprintf(szPetName, "%s - %s", chrInfoPacket.name, c_szNpcClientName);
					}
					else
					{
						sprintf(szPetName, "%s", chrInfoPacket.name);
					}
    
					kNetActorData.m_stName = szPetName;
				}
				else
				{
					if (CPythonNonPlayer.Instance().GetName(kNetActorData.m_dwRace, c_szNpcClientName))
					{
						kNetActorData.m_stName = c_szNpcClientName;
					}
					else
					{
						kNetActorData.m_stName = chrInfoPacket.name;
					}
				}
			}
			else
			{
				kNetActorData.m_stName = chrInfoPacket.name;
			}
	#else
			kNetActorData.m_stName = chrInfoPacket.name;
	#endif
			kNetActorData.m_dwGuildID = chrInfoPacket.dwGuildID;
			kNetActorData.m_dwLevel = chrInfoPacket.dwLevel;
			kNetActorData.m_sAlignment = chrInfoPacket.sAlignment;
			kNetActorData.m_byPKMode = chrInfoPacket.bPKMode;
			kNetActorData.m_dwGuildID = chrInfoPacket.dwGuildID;
			kNetActorData.m_dwEmpireID = chrInfoPacket.bEmpire;
			kNetActorData.m_dwArmor = chrInfoPacket.dwPart[CHR_EQUIPPART_ARMOR];
			kNetActorData.m_dwWeapon = chrInfoPacket.dwPart[CHR_EQUIPPART_WEAPON];
			kNetActorData.m_dwHair = chrInfoPacket.dwPart[CHR_EQUIPPART_HAIR];
			kNetActorData.m_dwAcce = chrInfoPacket.dwPart[CHR_EQUIPPART_ACCE];
			kNetActorData.m_byAcceDrainRate = chrInfoPacket.byAcceDrainRate;
			kNetActorData.m_dwMountVnum = chrInfoPacket.dwMountVnum;
			kNetActorData.m_dwArrow = chrInfoPacket.dwArrow;
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
			kNetActorData.m_bLanguage = chrInfoPacket.bLanguage;
	#endif
			__RecvCharacterAppendPacket(kNetActorData);
		}
		else
		{
			TraceError("TPacketGCCharacterAdditionalInfo name=%s vid=%d race=%d Error",chrInfoPacket.name,chrInfoPacket.dwVID,kNetActorData.m_dwRace);
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCharacterAppendPacketNew()
	{
		TraceError("TPacketGCCharacterAdd2?? ???? ?ʴ? ??Ŷ?Դ??.");
		packet_add_char2 chrAddPacket = new packet_add_char2();
		if (!Recv(sizeof(packet_add_char2), chrAddPacket))
		{
			return false;
		}
		if (IsInvisibleRace(chrAddPacket.wRaceNum))
		{
			return true;
		}
    
		__GlobalPositionToLocalPosition(chrAddPacket.x, chrAddPacket.y);
    
		SNetworkActorData kNetActorData = new SNetworkActorData();
		kNetActorData.m_dwLevel = 0;
		kNetActorData.m_bType = chrAddPacket.bType;
		kNetActorData.m_dwGuildID = chrAddPacket.dwGuild;
		kNetActorData.m_dwEmpireID = chrAddPacket.bEmpire;
		kNetActorData.m_dwMovSpd = chrAddPacket.bMovingSpeed;
		kNetActorData.m_dwAtkSpd = chrAddPacket.bAttackSpeed;
		kNetActorData.m_dwRace = chrAddPacket.wRaceNum;
		kNetActorData.m_dwArmor = chrAddPacket.dwPart[CHR_EQUIPPART_ARMOR];
		kNetActorData.m_dwWeapon = chrAddPacket.dwPart[CHR_EQUIPPART_WEAPON];
		kNetActorData.m_dwHair = chrAddPacket.dwPart[CHR_EQUIPPART_HAIR];
		kNetActorData.m_dwAcce = chrAddPacket.dwPart[CHR_EQUIPPART_ACCE];
		kNetActorData.m_byAcceDrainRate = chrAddPacket.byAcceDrainRate;
		kNetActorData.m_dwStateFlags = chrAddPacket.bStateFlag;
		kNetActorData.m_dwVID = chrAddPacket.dwVID;
		kNetActorData.m_dwMountVnum = chrAddPacket.dwMountVnum;
		kNetActorData.m_dwArrow = chrAddPacket.dwArrow;
		kNetActorData.m_fRot = chrAddPacket.angle;
		kNetActorData.m_kAffectFlags.CopyData(0, sizeof(chrAddPacket.dwAffectFlag[0]), chrAddPacket.dwAffectFlag[0]);
		kNetActorData.m_kAffectFlags.CopyData(32, sizeof(chrAddPacket.dwAffectFlag[1]), chrAddPacket.dwAffectFlag[1]);
		kNetActorData.SetPosition(chrAddPacket.x, chrAddPacket.y);
		kNetActorData.m_sAlignment = chrAddPacket.sAlignment;
		kNetActorData.m_byPKMode = chrAddPacket.bPKMode;
		kNetActorData.m_stName = chrAddPacket.name;
		__RecvCharacterAppendPacket(kNetActorData);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCharacterUpdatePacket()
	{
		packet_update_char chrUpdatePacket = new packet_update_char();
		if (!Recv(sizeof(packet_update_char), chrUpdatePacket))
		{
			return false;
		}
    
		SNetworkUpdateActorData kNetUpdateActorData = new SNetworkUpdateActorData();
		kNetUpdateActorData.m_dwGuildID = chrUpdatePacket.dwGuildID;
		kNetUpdateActorData.m_dwMovSpd = chrUpdatePacket.bMovingSpeed;
		kNetUpdateActorData.m_dwAtkSpd = chrUpdatePacket.bAttackSpeed;
		kNetUpdateActorData.m_dwArmor = chrUpdatePacket.dwPart[CHR_EQUIPPART_ARMOR];
		kNetUpdateActorData.m_dwWeapon = chrUpdatePacket.dwPart[CHR_EQUIPPART_WEAPON];
		kNetUpdateActorData.m_dwHair = chrUpdatePacket.dwPart[CHR_EQUIPPART_HAIR];
		kNetUpdateActorData.m_dwAcce = chrUpdatePacket.dwPart[CHR_EQUIPPART_ACCE];
		kNetUpdateActorData.m_byAcceDrainRate = chrUpdatePacket.byAcceDrainRate;
		kNetUpdateActorData.m_dwVID = chrUpdatePacket.dwVID;
		kNetUpdateActorData.m_kAffectFlags.CopyData(0, sizeof(chrUpdatePacket.dwAffectFlag[0]), chrUpdatePacket.dwAffectFlag[0]);
		kNetUpdateActorData.m_kAffectFlags.CopyData(32, sizeof(chrUpdatePacket.dwAffectFlag[1]), chrUpdatePacket.dwAffectFlag[1]);
		kNetUpdateActorData.m_sAlignment = chrUpdatePacket.sAlignment;
		kNetUpdateActorData.m_byPKMode = chrUpdatePacket.bPKMode;
		kNetUpdateActorData.m_dwStateFlags = chrUpdatePacket.bStateFlag;
		kNetUpdateActorData.m_dwMountVnum = chrUpdatePacket.dwMountVnum;
		kNetUpdateActorData.m_dwArrow = chrUpdatePacket.dwArrow;
	#if ENABLE_MULTI_LANGUAGE_SYSTEM
		kNetUpdateActorData.m_bLanguage = chrUpdatePacket.bLanguage;
	#endif
		__RecvCharacterUpdatePacket(kNetUpdateActorData);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RecvCharacterAppendPacket(SNetworkActorData pkNetActorData)
	{
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		if (rkPlayer.IsMainCharacterIndex(pkNetActorData.m_dwVID))
		{
			rkPlayer.SetRace(pkNetActorData.m_dwRace);
    
			__SetWeaponPower(rkPlayer);
    
			if (rkPlayer.NEW_GetMainActorPtr())
			{
				CPythonBackground.Instance().Update(pkNetActorData.m_lCurX, pkNetActorData.m_lCurY, 0.0f);
				CPythonCharacterManager.Instance().Update();
    
				{
					string strMapName = CPythonBackground.Instance().GetWarpMapName();
					if (strMapName == "metin2_map_deviltower1")
					{
						__ShowMapName(pkNetActorData.m_lCurX, pkNetActorData.m_lCurY);
					}
				}
			}
			else
			{
				__ShowMapName(pkNetActorData.m_lCurX, pkNetActorData.m_lCurY);
			}
		}
    
		m_rokNetActorMgr.AppendActor(pkNetActorData);
    
		if (GetMainActorVID() == pkNetActorData.m_dwVID)
		{
			rkPlayer.SetTarget(0);
			if (m_bComboSkillFlag)
			{
				rkPlayer.SetComboSkillFlag(m_bComboSkillFlag);
			}
    
			__SetGuildID(pkNetActorData.m_dwGuildID);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __RecvCharacterUpdatePacket(SNetworkUpdateActorData pkNetUpdateActorData)
	{
		m_rokNetActorMgr.UpdateActor(pkNetUpdateActorData);
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		if (rkPlayer.IsMainCharacterIndex(pkNetUpdateActorData.m_dwVID))
		{
			__SetGuildID(pkNetUpdateActorData.m_dwGuildID);
			__SetWeaponPower(rkPlayer);
    
			__RefreshStatus();
			__RefreshAlignmentWindow();
			__RefreshEquipmentWindow();
			__RefreshInventoryWindow();
		}
		else
		{
			rkPlayer.NotifyCharacterUpdate(pkNetUpdateActorData.m_dwVID);
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCharacterDeletePacket()
	{
		packet_del_char chrDelPacket = new packet_del_char();
    
		if (!Recv(sizeof(packet_del_char), chrDelPacket))
		{
			TraceError("CPythonNetworkStream::RecvCharacterDeletePacket - Recv Error");
			return false;
		}
    
		m_rokNetActorMgr.RemoveActor(chrDelPacket.dwVID);
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_PrivateShop_Disappear", Py_BuildValue("(i)", chrDelPacket.dwVID));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvCharacterMovePacket()
	{
		packet_move kMovePacket = new packet_move();
		if (!Recv(sizeof(packet_move), kMovePacket))
		{
			Tracen("CPythonNetworkStream::RecvCharacterMovePacket - PACKET READ ERROR");
			return false;
		}
    
		__GlobalPositionToLocalPosition(kMovePacket.lX, kMovePacket.lY);
    
		SNetworkMoveActorData kNetMoveActorData = new SNetworkMoveActorData();
		kNetMoveActorData.m_dwArg = kMovePacket.bArg;
		kNetMoveActorData.m_dwFunc = kMovePacket.bFunc;
		kNetMoveActorData.m_dwTime = kMovePacket.dwTime;
		kNetMoveActorData.m_dwVID = kMovePacket.dwVID;
		kNetMoveActorData.m_fRot = kMovePacket.bRot * 5.0f;
		kNetMoveActorData.m_lPosX = kMovePacket.lX;
		kNetMoveActorData.m_lPosY = kMovePacket.lY;
		kNetMoveActorData.m_dwDuration = kMovePacket.dwDuration;
    
		m_rokNetActorMgr.MoveActor(kNetMoveActorData);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvOwnerShipPacket()
	{
		packet_ownership kPacketOwnership = new packet_ownership();
    
		if (!Recv(sizeof(packet_ownership), kPacketOwnership))
		{
			return false;
		}
    
		m_rokNetActorMgr.SetActorOwner(kPacketOwnership.dwOwnerVID, kPacketOwnership.dwVictimVID);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSyncPositionPacket()
	{
		packetd_sync_position kPacketSyncPos = new packetd_sync_position();
		if (!Recv(sizeof(packetd_sync_position), kPacketSyncPos))
		{
			return false;
		}
    
		packetd_sync_position_element kSyncPos = new packetd_sync_position_element();
    
		uint uSyncPosCount = (kPacketSyncPos.wSize - sizeof(packetd_sync_position)) / sizeof(packetd_sync_position_element);
		for (uint iSyncPos = 0; iSyncPos < uSyncPosCount; ++iSyncPos)
		{
			if (!Recv(sizeof(packetd_sync_position_element), kSyncPos))
			{
				return false;
			}
    
			__GlobalPositionToLocalPosition(kSyncPos.lX, kSyncPos.lY);
			m_rokNetActorMgr.SyncActor(kSyncPos.dwVID, kSyncPos.lX, kSyncPos.lY);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSafeBoxMoneyPacket(byte byState, uint dwMoney)
	{
		Debug.Assert(!"CPythonNetworkStream::SendSafeBoxMoneyPacket - »ç¿ëÇÏÁö ¾Ê´Â ÇÔ¼ö");
		return false;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSafeBoxCheckinPacket(TItemPos InventoryPos, byte bySafeBoxPos)
	{
		__PlayInventoryItemDropSound(InventoryPos);
    
		command_safebox_checkin kSafeboxCheckin = new command_safebox_checkin();
		kSafeboxCheckin.bHeader = LG_HEADER_CG_SAFEBOX_CHECKIN;
		kSafeboxCheckin.ItemPos = InventoryPos;
		kSafeboxCheckin.bSafePos = bySafeBoxPos;
		if (!Send(sizeof(command_safebox_checkin), kSafeboxCheckin))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSafeBoxCheckoutPacket(byte bySafeBoxPos, TItemPos InventoryPos)
	{
		__PlaySafeBoxItemDropSound(bySafeBoxPos);
    
		command_safebox_checkout kSafeboxCheckout = new command_safebox_checkout();
		kSafeboxCheckout.bHeader = LG_HEADER_CG_SAFEBOX_CHECKOUT;
		kSafeboxCheckout.bSafePos = bySafeBoxPos;
		kSafeboxCheckout.ItemPos = InventoryPos;
		if (!Send(sizeof(command_safebox_checkout), kSafeboxCheckout))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSafeBoxItemMovePacket(byte bySourcePos, byte byTargetPos, ushort wCount)
	{
		__PlaySafeBoxItemDropSound(bySourcePos);
    
		command_item_move kItemMove = new command_item_move();
		kItemMove.header = LG_HEADER_CG_SAFEBOX_ITEM_MOVE;
		kItemMove.pos = TItemPos(INVENTORY, bySourcePos);
		kItemMove.num = wCount;
		kItemMove.change_pos = TItemPos(INVENTORY, byTargetPos);
		if (!Send(sizeof(command_item_move), kItemMove))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSafeBoxSetPacket()
	{
		packet_set_item2 kItemSet = new packet_set_item2();
		if (!Recv(sizeof(packet_set_item2), kItemSet))
		{
			return false;
		}
    
		TItemData kItemData = new TItemData();
		kItemData.vnum = kItemSet.vnum;
		kItemData.count = kItemSet.count;
		kItemData.flags = kItemSet.flags;
		kItemData.anti_flags = kItemSet.anti_flags;
		for (int isocket = 0; isocket < ITEM_SOCKET_SLOT_MAX_NUM; ++isocket)
		{
			kItemData.alSockets[isocket] = kItemSet.alSockets[isocket];
		}
		for (int iattr = 0; iattr < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++iattr)
		{
			kItemData.aAttr[iattr] = kItemSet.aAttr[iattr];
		}
    
		CPythonSafeBox.Instance().SetItemData(kItemSet.Cell.cell, kItemData);
    
		__RefreshSafeboxWindow();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSafeBoxDelPacket()
	{
		packet_item_del kItemDel = new packet_item_del();
		if (!Recv(sizeof(packet_item_del), kItemDel))
		{
			return false;
		}
    
		CPythonSafeBox.Instance().DelItemData(kItemDel.pos);
    
		__RefreshSafeboxWindow();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSafeBoxWrongPasswordPacket()
	{
		packet_safebox_wrong_password kSafeboxWrongPassword = new packet_safebox_wrong_password();
    
		if (!Recv(sizeof(packet_safebox_wrong_password), kSafeboxWrongPassword))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OnSafeBoxError", Py_BuildValue("()"));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSafeBoxSizePacket()
	{
		packet_safebox_size kSafeBoxSize = new packet_safebox_size();
		if (!Recv(sizeof(packet_safebox_size), kSafeBoxSize))
		{
			return false;
		}
    
		CPythonSafeBox.Instance().OpenSafeBox(kSafeBoxSize.bSize);
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OpenSafeboxWindow", Py_BuildValue("(i)", kSafeBoxSize.bSize));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSafeBoxMoneyChangePacket()
	{
		packet_safebox_money_change kMoneyChange = new packet_safebox_money_change();
		if (!Recv(sizeof(packet_safebox_money_change), kMoneyChange))
		{
			return false;
		}
    
		CPythonSafeBox.Instance().SetMoney(kMoneyChange.dwMoney);
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshSafeboxMoney", Py_BuildValue("()"));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendMallCheckoutPacket(byte byMallPos, TItemPos InventoryPos)
	{
		__PlayMallItemDropSound(byMallPos);
    
		command_mall_checkout kMallCheckoutPacket = new command_mall_checkout();
		kMallCheckoutPacket.bHeader = LG_HEADER_CG_MALL_CHECKOUT;
		kMallCheckoutPacket.bMallPos = byMallPos;
		kMallCheckoutPacket.ItemPos = InventoryPos;
		if (!Send(sizeof(command_mall_checkout), kMallCheckoutPacket))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMallOpenPacket()
	{
		packet_mall_open kMallOpen = new packet_mall_open();
		if (!Recv(sizeof(packet_mall_open), kMallOpen))
		{
			return false;
		}
    
		CPythonSafeBox.Instance().OpenMall(kMallOpen.bSize);
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "OpenMallWindow", Py_BuildValue("(i)", kMallOpen.bSize));
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMallItemSetPacket()
	{
		packet_set_item2 kItemSet = new packet_set_item2();
		if (!Recv(sizeof(packet_set_item2), kItemSet))
		{
			return false;
		}
    
		TItemData kItemData = new TItemData();
		kItemData.vnum = kItemSet.vnum;
		kItemData.count = kItemSet.count;
		kItemData.flags = kItemSet.flags;
		kItemData.anti_flags = kItemSet.anti_flags;
		for (int isocket = 0; isocket < ITEM_SOCKET_SLOT_MAX_NUM; ++isocket)
		{
			kItemData.alSockets[isocket] = kItemSet.alSockets[isocket];
		}
		for (int iattr = 0; iattr < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++iattr)
		{
			kItemData.aAttr[iattr] = kItemSet.aAttr[iattr];
		}
    
		CPythonSafeBox.Instance().SetMallItemData(kItemSet.Cell.cell, kItemData);
    
		__RefreshMallWindow();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMallItemDelPacket()
	{
		packet_item_del kItemDel = new packet_item_del();
		if (!Recv(sizeof(packet_item_del), kItemDel))
		{
			return false;
		}
    
		CPythonSafeBox.Instance().DelMallItemData(kItemDel.pos);
    
		__RefreshMallWindow();
		Tracef(" >> CPythonNetworkStream::RecvMallItemDelPacket\n");
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvItemSetPacket()
	{
		packet_set_item packet_item_set = new packet_set_item();
    
		if (!Recv(sizeof(packet_set_item), packet_item_set))
		{
			return false;
		}
    
		TItemData kItemData = new TItemData();
		kItemData.vnum = packet_item_set.vnum;
		kItemData.count = packet_item_set.count;
		kItemData.flags = 0;
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < ITEM_SOCKET_SLOT_MAX_NUM; ++i)
		{
			kItemData.alSockets[LaniatusDefVariables] = packet_item_set.alSockets[LaniatusDefVariables];
		}
		for (int j = 0; j < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++j)
		{
			kItemData.aAttr[j] = packet_item_set.aAttr[j];
		}
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
    
		rkPlayer.SetItemData(packet_item_set.Cell, kItemData);
    
		__RefreshInventoryWindow();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvItemSetPacket2()
	{
		packet_set_item2 packet_item_set = new packet_set_item2();
    
		if (!Recv(sizeof(packet_set_item2), packet_item_set))
		{
			return false;
		}
    
		TItemData kItemData = new TItemData();
		kItemData.vnum = packet_item_set.vnum;
		kItemData.count = packet_item_set.count;
		kItemData.flags = packet_item_set.flags;
		kItemData.anti_flags = packet_item_set.anti_flags;
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < ITEM_SOCKET_SLOT_MAX_NUM; ++i)
		{
			kItemData.alSockets[LaniatusDefVariables] = packet_item_set.alSockets[LaniatusDefVariables];
		}
		for (int j = 0; j < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++j)
		{
			kItemData.aAttr[j] = packet_item_set.aAttr[j];
		}
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		rkPlayer.SetItemData(packet_item_set.Cell, kItemData);
    
		if (packet_item_set.highlight)
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_Highlight_Item", Py_BuildValue("(ii)", packet_item_set.Cell.window_type, packet_item_set.Cell.cell));
		}
    
		__RefreshInventoryWindow();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvItemUsePacket()
	{
		packet_use_item packet_item_use = new packet_use_item();
    
		if (!Recv(sizeof(packet_use_item), packet_item_use))
		{
			return false;
		}
    
		__RefreshInventoryWindow();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvItemUpdatePacket()
	{
		packet_update_item packet_item_update = new packet_update_item();
    
		if (!Recv(sizeof(packet_update_item), packet_item_update))
		{
			return false;
		}
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		rkPlayer.SetItemCount(packet_item_update.Cell, packet_item_update.count);
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < ITEM_SOCKET_SLOT_MAX_NUM; ++i)
		{
			rkPlayer.SetItemMetinSocket(packet_item_update.Cell, i, packet_item_update.alSockets[LaniatusDefVariables]);
		}
		for (int j = 0; j < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++j)
		{
			rkPlayer.SetItemAttribute(packet_item_update.Cell, j, packet_item_update.aAttr[j].bType, packet_item_update.aAttr[j].sValue);
		}
    
		__RefreshInventoryWindow();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvItemGroundAddPacket()
	{
		packet_ground_add_item packet_item_ground_add = new packet_ground_add_item();
    
		if (!Recv(sizeof(packet_ground_add_item), packet_item_ground_add))
		{
			return false;
		}
    
		__GlobalPositionToLocalPosition(packet_item_ground_add.lX, packet_item_ground_add.lY);
    
		CPythonItem.Instance().CreateItem(packet_item_ground_add.dwVID, packet_item_ground_add.dwVnum, packet_item_ground_add.lX, packet_item_ground_add.lY, packet_item_ground_add.lZ);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvItemOwnership()
	{
		packet_item_ownership p = new packet_item_ownership();
    
		if (!Recv(sizeof(packet_item_ownership), p))
		{
			return false;
		}
    
		CPythonItem.Instance().SetOwnership(p.dwVID, p.szName);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvItemGroundDelPacket()
	{
		packet_ground_del_item packet_item_ground_del = new packet_ground_del_item();
    
		if (!Recv(sizeof(packet_ground_del_item), packet_item_ground_del))
		{
			return false;
		}
    
		CPythonItem.Instance().DeleteItem(packet_item_ground_del.vid);
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvQuickSlotAddPacket()
	{
		packet_quickslot_add packet_quick_slot_add = new packet_quickslot_add();
    
		if (!Recv(sizeof(packet_quickslot_add), packet_quick_slot_add))
		{
			return false;
		}
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		rkPlayer.AddQuickSlot(packet_quick_slot_add.pos, packet_quick_slot_add.slot.Type, packet_quick_slot_add.slot.Position);
    
		__RefreshInventoryWindow();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvQuickSlotDelPacket()
	{
		packet_quickslot_del packet_quick_slot_del = new packet_quickslot_del();
    
		if (!Recv(sizeof(packet_quickslot_del), packet_quick_slot_del))
		{
			return false;
		}
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		rkPlayer.DeleteQuickSlot(packet_quick_slot_del.pos);
    
		__RefreshInventoryWindow();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvQuickSlotMovePacket()
	{
		packet_quickslot_swap packet_quick_slot_swap = new packet_quickslot_swap();
    
		if (!Recv(sizeof(packet_quickslot_swap), packet_quick_slot_swap))
		{
			return false;
		}
    
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		rkPlayer.MoveQuickSlot(packet_quick_slot_swap.pos, packet_quick_slot_swap.change_pos);
    
		__RefreshInventoryWindow();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendShopEndPacket()
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_shop packet_shop = new command_shop();
		packet_shop.header = LG_HEADER_CG_SHOP;
		packet_shop.subheader = SHOP_SUBLG_HEADER_CG_END;
    
		if (!Send(sizeof(command_shop), packet_shop))
		{
			Tracef("SendShopEndPacket Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendShopBuyPacket(byte bPos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_shop PacketShop = new command_shop();
		PacketShop.header = LG_HEADER_CG_SHOP;
		PacketShop.subheader = SHOP_SUBLG_HEADER_CG_BUY;
    
		if (!Send(sizeof(command_shop), PacketShop))
		{
			Tracef("SendShopBuyPacket Error\n");
			return false;
		}
    
		byte bCount = 1;
		if (!Send(sizeof(byte), bCount))
		{
			Tracef("SendShopBuyPacket Error\n");
			return false;
		}
    
		if (!Send(sizeof(byte), bPos))
		{
			Tracef("SendShopBuyPacket Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendShopSellPacket(byte bySlot)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_shop PacketShop = new command_shop();
		PacketShop.header = LG_HEADER_CG_SHOP;
		PacketShop.subheader = SHOP_SUBLG_HEADER_CG_SELL;
    
		if (!Send(sizeof(command_shop), PacketShop))
		{
			Tracef("SendShopSellPacket Error\n");
			return false;
		}
		if (!Send(sizeof(byte), bySlot))
		{
			Tracef("SendShopAddSellPacket Error\n");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendShopSellPacketNew(byte bySlot, ushort wCount)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_shop PacketShop = new command_shop();
		PacketShop.header = LG_HEADER_CG_SHOP;
		PacketShop.subheader = SHOP_SUBLG_HEADER_CG_SELL2;
    
		if (!Send(sizeof(command_shop), PacketShop))
		{
			Tracef("SendShopSellPacket Error\n");
			return false;
		}
		if (!Send(sizeof(byte), bySlot))
		{
			Tracef("SendShopAddSellPacket Error\n");
			return false;
		}
		if (!Send(sizeof(ushort), wCount))
		{
			Tracef("SendShopAddSellPacket Error\n");
			return false;
		}
    
		Tracef(" SendShopSellPacketNew(bySlot=%d, wCount=%d)\n", bySlot, wCount);
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendItemUsePacket(TItemPos pos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		if (__IsEquipItemInSlot(pos))
		{
			if (CPythonExchange.Instance().isTrading())
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AppendNotifyMessage", Py_BuildValue("(s)", "CANNOT_EQUIP_EXCHANGE"));
				return true;
			}
    
			if (CPythonShop.Instance().IsOpen())
			{
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AppendNotifyMessage", Py_BuildValue("(s)", "CANNOT_EQUIP_SHOP"));
				return true;
			}
    
			if (__IsPlayerAttacking())
			{
				return true;
			}
		}
    
		__PlayInventoryItemUseSound(pos);
    
		command_item_use itemUsePacket = new command_item_use();
		itemUsePacket.header = LG_HEADER_CG_ITEM_USE;
		itemUsePacket.pos = pos;
    
		if (!Send(sizeof(command_item_use), itemUsePacket))
		{
			Tracen("SendItemUsePacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendItemUseToItemPacket(TItemPos source_pos, TItemPos target_pos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_item_use_to_item itemUseToItemPacket = new command_item_use_to_item();
		itemUseToItemPacket.header = LG_HEADER_CG_ITEM_USE_TO_ITEM;
		itemUseToItemPacket.source_pos = source_pos;
		itemUseToItemPacket.target_pos = target_pos;
    
		if (!Send(sizeof(command_item_use_to_item), itemUseToItemPacket))
		{
			Tracen("SendItemUseToItemPacket Error");
			return false;
		}
    
	#if DEBUG
		Tracef(" << SendItemUseToItemPacket(src=%d, dst=%d)\n", source_pos, target_pos);
	#endif
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendItemDropPacket(TItemPos pos, uint elk)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_item_drop itemDropPacket = new command_item_drop();
		itemDropPacket.header = LG_HEADER_CG_ITEM_DROP;
		itemDropPacket.pos = pos;
		itemDropPacket.elk = elk;
    
		if (!Send(sizeof(command_item_drop), itemDropPacket))
		{
			Tracen("SendItemDropPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendItemDropPacketNew(TItemPos pos, uint elk, uint count)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_item_drop2 itemDropPacket = new command_item_drop2();
		itemDropPacket.header = LG_HEADER_CG_ITEM_DROP2;
		itemDropPacket.pos = pos;
		itemDropPacket.gold = elk;
		itemDropPacket.count = count;
    
		if (!Send(sizeof(command_item_drop2), itemDropPacket))
		{
			Tracen("SendItemDropPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendItemDestroyPacket(TItemPos pos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_item_destroy itemDestroyPacket = new command_item_destroy();
		itemDestroyPacket.header = LG_HEADER_CG_ITEM_DESTROY;
		itemDestroyPacket.pos = pos;
    
		if (!Send(sizeof(command_item_destroy), itemDestroyPacket))
		{
			Tracen("SendItemDestroyPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __IsEquipItemInSlot(TItemPos uSlotPos)
	{
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		return rkPlayer.IsEquipItemInSlot(uSlotPos);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __PlayInventoryItemUseSound(TItemPos uSlotPos)
	{
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		uint dwItemID = rkPlayer.GetItemIndex(uSlotPos);
    
		CPythonItem rkItem = CPythonItem.Instance();
		rkItem.PlayUseSound(dwItemID);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __PlayInventoryItemDropSound(TItemPos uSlotPos)
	{
		IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
		uint dwItemID = rkPlayer.GetItemIndex(uSlotPos);
    
		CPythonItem rkItem = CPythonItem.Instance();
		rkItem.PlayDropSound(dwItemID);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __PlaySafeBoxItemDropSound(uint uSlotPos)
	{
		uint dwItemID;
		CPythonSafeBox rkSafeBox = CPythonSafeBox.Instance();
		if (!rkSafeBox.GetSlotItemID(uSlotPos, dwItemID))
		{
			return;
		}
    
		CPythonItem rkItem = CPythonItem.Instance();
		rkItem.PlayDropSound(dwItemID);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __PlayMallItemDropSound(uint uSlotPos)
	{
		uint dwItemID;
		CPythonSafeBox rkSafeBox = CPythonSafeBox.Instance();
		if (!rkSafeBox.GetSlotMallItemID(uSlotPos, dwItemID))
		{
			return;
		}
    
		CPythonItem rkItem = CPythonItem.Instance();
		rkItem.PlayDropSound(dwItemID);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendItemMovePacket(TItemPos pos, TItemPos change_pos, ushort num)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		if (__IsEquipItemInSlot(pos))
		{
			if (CPythonExchange.Instance().isTrading())
			{
				if (pos.IsEquipCell() || change_pos.IsEquipCell())
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AppendNotifyMessage", Py_BuildValue("(s)", "CANNOT_EQUIP_EXCHANGE"));
					return true;
				}
			}
    
			if (CPythonShop.Instance().IsOpen())
			{
				if (pos.IsEquipCell() || change_pos.IsEquipCell())
				{
					PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_AppendNotifyMessage", Py_BuildValue("(s)", "CANNOT_EQUIP_SHOP"));
					return true;
				}
			}
    
			if (__IsPlayerAttacking())
			{
				return true;
			}
		}
    
		__PlayInventoryItemDropSound(pos);
    
		command_item_move itemMovePacket = new command_item_move();
		itemMovePacket.header = LG_HEADER_CG_ITEM_MOVE;
		itemMovePacket.pos = pos;
		itemMovePacket.change_pos = change_pos;
		itemMovePacket.num = num;
    
		if (!Send(sizeof(command_item_move), itemMovePacket))
		{
			Tracen("SendItemMovePacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendItemPickUpPacket(uint vid)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_item_pickup itemPickUpPacket = new command_item_pickup();
		itemPickUpPacket.header = LG_HEADER_CG_ITEM_PICKUP;
		itemPickUpPacket.vid = vid;
    
		if (!Send(sizeof(command_item_pickup), itemPickUpPacket))
		{
			Tracen("SendItemPickUpPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendQuickSlotAddPacket(byte wpos, byte type, byte pos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_quickslot_add quickSlotAddPacket = new command_quickslot_add();
    
		quickSlotAddPacket.header = LG_HEADER_CG_QUICKSLOT_ADD;
		quickSlotAddPacket.pos = wpos;
		quickSlotAddPacket.slot.Type = type;
		quickSlotAddPacket.slot.Position = pos;
    
		if (!Send(sizeof(command_quickslot_add), quickSlotAddPacket))
		{
			Tracen("SendQuickSlotAddPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendQuickSlotDelPacket(byte pos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_quickslot_del quickSlotDelPacket = new command_quickslot_del();
    
		quickSlotDelPacket.header = LG_HEADER_CG_QUICKSLOT_DEL;
		quickSlotDelPacket.pos = pos;
    
		if (!Send(sizeof(command_quickslot_del), quickSlotDelPacket))
		{
			Tracen("SendQuickSlotDelPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendQuickSlotMovePacket(byte pos, byte change_pos)
	{
		if (!__CanActMainInstance())
		{
			return true;
		}
    
		command_quickslot_swap quickSlotSwapPacket = new command_quickslot_swap();
    
		quickSlotSwapPacket.header = LG_HEADER_CG_QUICKSLOT_SWAP;
		quickSlotSwapPacket.pos = pos;
		quickSlotSwapPacket.change_pos = change_pos;
    
		if (!Send(sizeof(command_quickslot_swap), quickSlotSwapPacket))
		{
			Tracen("SendQuickSlotSwapPacket Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSpecialEffect()
	{
		SPacketGCSpecialEffect kSpecialEffect = new SPacketGCSpecialEffect();
		if (!Recv(sizeof(SPacketGCSpecialEffect), kSpecialEffect))
		{
			return false;
		}
    
		uint effect = -1;
		bool bPlayPotionSound = false;
		bool bAttachEffect = true;
		switch (kSpecialEffect.type)
		{
			case SE_HPUP_RED:
				effect = CInstanceBase.EFFECT_HPUP_RED;
				bPlayPotionSound = true;
				break;
			case SE_SPUP_BLUE:
				effect = CInstanceBase.EFFECT_SPUP_BLUE;
				bPlayPotionSound = true;
				break;
			case SE_SPEEDUP_GREEN:
				effect = CInstanceBase.EFFECT_SPEEDUP_GREEN;
				bPlayPotionSound = true;
				break;
			case SE_DXUP_PURPLE:
				effect = CInstanceBase.EFFECT_DXUP_PURPLE;
				bPlayPotionSound = true;
				break;
			case SE_CRITICAL:
				effect = CInstanceBase.EFFECT_CRITICAL;
				break;
			case SE_PENETRATE:
				effect = CInstanceBase.EFFECT_PENETRATE;
				break;
			case SE_BLOCK:
				effect = CInstanceBase.EFFECT_BLOCK;
				break;
			case SE_DODGE:
				effect = CInstanceBase.EFFECT_DODGE;
				break;
			case SE_CHINA_FIREWORK:
				effect = CInstanceBase.EFFECT_FIRECRACKER;
				bAttachEffect = false;
				break;
			case SE_SPIN_TOP:
				effect = CInstanceBase.EFFECT_SPIN_TOP;
				bAttachEffect = false;
				break;
			case SE_SUCCESS :
				effect = CInstanceBase.EFFECT_SUCCESS;
				bAttachEffect = false;
				break;
			case SE_FAIL :
				effect = CInstanceBase.EFFECT_FAIL;
				break;
			case SE_FR_SUCCESS:
				effect = CInstanceBase.EFFECT_FR_SUCCESS;
				bAttachEffect = false;
				break;
			case SE_LEVELUP_ON_14_FOR_GERMANY:
				effect = CInstanceBase.EFFECT_LEVELUP_ON_14_FOR_GERMANY;
				bAttachEffect = false;
				break;
			case SE_LEVELUP_UNDER_15_FOR_GERMANY:
				effect = CInstanceBase.EFFECT_LEVELUP_UNDER_15_FOR_GERMANY;
				bAttachEffect = false;
				break;
			case SE_PERCENT_DAMAGE1:
				effect = CInstanceBase.EFFECT_PERCENT_DAMAGE1;
				break;
			case SE_PERCENT_DAMAGE2:
				effect = CInstanceBase.EFFECT_PERCENT_DAMAGE2;
				break;
			case SE_PERCENT_DAMAGE3:
				effect = CInstanceBase.EFFECT_PERCENT_DAMAGE3;
				break;
			case SE_AUTO_HPUP:
				effect = CInstanceBase.EFFECT_AUTO_HPUP;
				break;
			case SE_AUTO_SPUP:
				effect = CInstanceBase.EFFECT_AUTO_SPUP;
				break;
			case SE_EQUIP_RAMADAN_RING:
				effect = CInstanceBase.EFFECT_RAMADAN_RING_EQUIP;
				break;
			case SE_EQUIP_HALLOWEEN_CANDY:
				effect = CInstanceBase.EFFECT_HALLOWEEN_CANDY_EQUIP;
				break;
			case SE_EQUIP_HAPPINESS_RING:
				 effect = CInstanceBase.EFFECT_HAPPINESS_RING_EQUIP;
				break;
			case SE_EQUIP_LOVE_PENDANT:
				effect = CInstanceBase.EFFECT_LOVE_PENDANT_EQUIP;
				break;
			case SE_ACCE_SUCESS_ABSORB:
				effect = CInstanceBase.EFFECT_ACCE_SUCESS_ABSORB;
				break;
			case SE_ACCE_EQUIP:
				effect = CInstanceBase.EFFECT_ACCE_EQUIP;
				break;
			case SE_ACCE_BACK:
				effect = CInstanceBase.EFFECT_ACCE_BACK;
				break;
    
    
			default:
				TraceError("%d ´Â ¾ø´Â ½ºÆä¼È ÀÌÆåÆ® ¹øÈ£ÀÔ´Ï´Ù.TPacketGCSpecialEffect",kSpecialEffect.type);
				break;
		}
    
		if (bPlayPotionSound)
		{
			IAbstractPlayer rkPlayer = IAbstractPlayer.GetSingleton();
			if (rkPlayer.IsMainCharacterIndex(kSpecialEffect.vid))
			{
				CPythonItem rkItem = CPythonItem.Instance();
				rkItem.PlayUsePotionSound();
			}
		}
    
		if (-1 != effect)
		{
			CInstanceBase pInstance = CPythonCharacterManager.Instance().GetInstancePtr(kSpecialEffect.vid);
			if (pInstance != null)
			{
				if (bAttachEffect)
				{
					pInstance.AttachSpecialEffect(effect);
				}
				else
				{
					pInstance.CreateSpecialEffect(effect);
				}
			}
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvSpecificEffect()
	{
		SPacketGCSpecificEffect kSpecificEffect = new SPacketGCSpecificEffect();
		if (!Recv(sizeof(SPacketGCSpecificEffect), kSpecificEffect))
		{
			return false;
		}
    
		CInstanceBase pInstance = CPythonCharacterManager.Instance().GetInstancePtr(kSpecificEffect.vid);
    
		if (pInstance != null)
		{
			CInstanceBase.RegisterEffect(CInstanceBase.EFFECT_TEMP, "", kSpecificEffect.effect_file, false);
			pInstance.AttachSpecialEffect(CInstanceBase.EFFECT_TEMP);
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvDragonSoulRefine()
	{
		SPacketGCDragonSoulRefine kDragonSoul = new SPacketGCDragonSoulRefine();
    
		if (!Recv(sizeof(SPacketGCDragonSoulRefine), kDragonSoul))
		{
			return false;
		}
    
    
		switch (kDragonSoul.bSubType)
		{
		case DS_SUB_LG_HEADER_OPEN:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_DragonSoulRefineWindow_Open", Py_BuildValue("()"));
			break;
		case DS_SUB_LG_HEADER_REFINE_FAIL:
		case DS_SUB_LG_HEADER_REFINE_FAIL_MAX_REFINE:
		case DS_SUB_LG_HEADER_REFINE_FAIL_INVALID_MATERIAL:
		case DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MONEY:
		case DS_SUB_LG_HEADER_REFINE_FAIL_NOT_ENOUGH_MATERIAL:
		case DS_SUB_LG_HEADER_REFINE_FAIL_TOO_MUCH_MATERIAL:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_DragonSoulRefineWindow_RefineFail", Py_BuildValue("(iii)", kDragonSoul.bSubType, kDragonSoul.Pos.window_type, kDragonSoul.Pos.cell));
			break;
		case DS_SUB_LG_HEADER_REFINE_SUCCEED:
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "BINARY_DragonSoulRefineWindow_RefineSucceed", Py_BuildValue("(ii)", kDragonSoul.Pos.window_type, kDragonSoul.Pos.cell));
			break;
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvAccePacket()
	{
		packet_acce AccePacket = new packet_acce();
		if (!Recv(sizeof(packet_acce), AccePacket))
		{
			return false;
		}
    
		switch (AccePacket.subheader)
		{
			case ACCE_SUBLG_HEADER_GC_SET_ITEM:
			{
				TItemPos itemPos = new TItemPos();
				if (!Recv(sizeof(TItemPos), itemPos))
				{
					return false;
				}
    
				packet_set_item2 kItemSet = new packet_set_item2();
				if (!Recv(sizeof(packet_set_item2), kItemSet))
				{
					return false;
				}
    
				TItemData kItemData = new TItemData();
				kItemData.vnum = kItemSet.vnum;
				kItemData.count = kItemSet.count;
				kItemData.flags = kItemSet.flags;
				kItemData.anti_flags = kItemSet.anti_flags;
    
				for (int isocket = 0; isocket < ITEM_SOCKET_SLOT_MAX_NUM; ++isocket)
				{
					kItemData.alSockets[isocket] = kItemSet.alSockets[isocket];
				}
    
				for (int iattr = 0; iattr < ITEM_ATTRIBUTE_SLOT_MAX_NUM; ++iattr)
				{
					kItemData.aAttr[iattr] = kItemSet.aAttr[iattr];
				}
    
				CPythonPlayer.instance().SetAcceItemData(kItemSet.Cell.cell, itemPos, kItemData);
    
				break;
			}
			case ACCE_SUBLG_HEADER_GC_CLEAR_SLOT:
			{
				ushort cell;
				if (!Recv(sizeof(ushort), cell))
				{
					return false;
				}
    
				TItemPos src = new TItemPos();
				if (!Recv(sizeof(TItemPos), src))
				{
					return false;
				}
    
				CPythonPlayer.instance().DelAcceItemData(cell, src);
    
				break;
			}
			case ACCE_SUBLG_HEADER_GC_CLEAR_ALL:
			{
				TItemPos srcLeft = new TItemPos();
				if (!Recv(sizeof(TItemPos), srcLeft))
				{
					return false;
				}
    
				TItemPos srcRight = new TItemPos();
				if (!Recv(sizeof(TItemPos), srcRight))
				{
					return false;
				}
    
				CPythonPlayer.instance().DelAcceItemData(CPythonPlayer.ACCE_SLOT_LEFT, srcLeft);
				CPythonPlayer.instance().DelAcceItemData(CPythonPlayer.ACCE_SLOT_RIGHT, srcRight);
				CPythonPlayer.instance().DelAcceItemData(CPythonPlayer.ACCE_SLOT_RESULT);
    
				break;
			}
		}
    
		__RefreshInventoryWindow();
		__RefreshAcceWindow();
    
		return true;
    
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendAcceRefineCheckinPacket(TItemPos InventoryPos, byte byAccePos)
	{
		__PlayInventoryItemDropSound(InventoryPos);
    
		command_acce kPackAcce = new command_acce();
		kPackAcce.header = LG_HEADER_CG_ACCE;
		kPackAcce.subheader = ACCE_SUBLG_HEADER_CG_REFINE_CHECKIN;
    
    
		command_acce_checkin kAcceCheckin = new command_acce_checkin();
		kAcceCheckin.ItemPos = InventoryPos;
		kAcceCheckin.bAccePos = byAccePos;
    
		if (!Send(sizeof(command_acce), kPackAcce))
		{
			return false;
		}
    
		if (!Send(sizeof(command_acce_checkin), kAcceCheckin))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendAcceRefineCheckoutPacket(byte byAccePos)
	{
		command_acce kPackAcce = new command_acce();
		kPackAcce.header = LG_HEADER_CG_ACCE;
		kPackAcce.subheader = ACCE_SUBLG_HEADER_CG_REFINE_CHECKOUT;
    
    
		command_acce_checkout kAcceCheckin = new command_acce_checkout();
		kAcceCheckin.bAccePos = byAccePos;
    
		if (!Send(sizeof(command_acce), kPackAcce))
		{
			return false;
		}
    
		if (!Send(sizeof(command_acce_checkout), kAcceCheckin))
		{
			return false;
		}
    
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendAcceRefineAcceptPacket(byte windowType)
	{
		command_acce kPackAcce = new command_acce();
		kPackAcce.header = LG_HEADER_CG_ACCE;
		kPackAcce.subheader = ACCE_SUBLG_HEADER_CG_REFINE_ACCEPT;
    
    
		command_acce_accept kAcceCheckin = new command_acce_accept();
		kAcceCheckin.windowType = windowType;
    
		if (!Send(sizeof(command_acce), kPackAcce))
		{
			return false;
		}
    
		if (!Send(sizeof(command_acce_accept), kAcceCheckin))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendAcceRefineCancelPacket()
	{
		command_acce kPackAcce = new command_acce();
		kPackAcce.header = LG_HEADER_CG_ACCE;
		kPackAcce.subheader = ACCE_SUBLG_HEADER_CG_REFINE_CANCEL;
    
    
		if (!Send(sizeof(command_acce), kPackAcce))
		{
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void HandShakePhase()
	{
		byte header;
    
		if (!CheckPacket(header))
		{
			return;
		}
    
		switch (header)
		{
			case LG_HEADER_GC_PHASE:
				if (RecvPhasePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_BINDUDP:
			{
					packet_LG_HEADER_bindudp BindUDP = new packet_LG_HEADER_bindudp();
    
					if (!Recv(sizeof(packet_LG_HEADER_bindudp), BindUDP))
					{
						return;
					}
    
					return;
			}
				break;
    
			case LG_HEADER_GC_HANDSHAKE:
			{
					if (!Recv(sizeof(packet_LG_HEADER_handshake), m_HandshakeData))
					{
						return;
					}
    
					Tracenf("HANDSHAKE RECV %u %d", m_HandshakeData.dwTime, m_HandshakeData.lDelta);
    
					ELTimer_SetServerMSec(m_HandshakeData.dwTime + m_HandshakeData.lDelta);
    
					m_HandshakeData.dwTime = m_HandshakeData.dwTime + m_HandshakeData.lDelta + m_HandshakeData.lDelta;
					m_HandshakeData.lDelta = 0;
    
					Tracenf("HANDSHAKE SEND %u", m_HandshakeData.dwTime);
    
					if (!Send(sizeof(packet_LG_HEADER_handshake), m_HandshakeData))
					{
						Debug.Assert(!"Failed Sending Handshake");
						return;
					}
    
					CTimer.Instance().SetBaseTime();
					return;
			}
				break;
			case LG_HEADER_GC_PING:
				RecvPingPacket();
				return;
				break;
    
	#if _IMPROVED_PACKET_ENCRYPTION_
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case LG_HEADER_GC_KEY_AGREEMENT:
				RecvKeyAgreementPacket();
				return;
				break;
    
			case LG_HEADER_GC_KEY_AGREEMENT_COMPLETED:
				RecvKeyAgreementCompletedPacket();
				return;
				break;
	#endif
	break;
		}
    
		RecvErrorPacket(header);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetHandShakePhase()
	{
		if ("HandShake" != m_strPhase)
		{
			m_phaseLeaveFunc.Run();
		}
    
		Tracen("");
		Tracen("## Network - Hand Shake Phase ##");
		Tracen("");
    
		m_strPhase = "HandShake";
    
		m_dwChangingPhaseTime = ELTimer_GetMSec();
		m_phaseProcessFunc.Set(this, CPythonNetworkStream.HandShakePhase);
		m_phaseLeaveFunc.Set(this, CPythonNetworkStream.__LeaveHandshakePhase);
    
		SetGameOnline();
    
		if (__DirectEnterMode_IsSet())
		{
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOGIN], "OnHandShake", Py_BuildValue("()"));
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvHandshakePacket()
	{
		packet_LG_HEADER_handshake kHandshakeData = new packet_LG_HEADER_handshake();
		if (!Recv(sizeof(packet_LG_HEADER_handshake), kHandshakeData))
		{
			return false;
		}
    
		Tracenf("HANDSHAKE RECV %u %d", kHandshakeData.dwTime, kHandshakeData.lDelta);
    
		m_kServerTimeSync.m_dwChangeServerTime = kHandshakeData.dwTime + kHandshakeData.lDelta;
		m_kServerTimeSync.m_dwChangeClientTime = ELTimer_GetMSec();
    
		kHandshakeData.dwTime = kHandshakeData.dwTime + kHandshakeData.lDelta + kHandshakeData.lDelta;
		kHandshakeData.lDelta = 0;
    
		Tracenf("HANDSHAKE SEND %u", kHandshakeData.dwTime);
    
		kHandshakeData.header = LG_HEADER_CG_TIME_SYNC;
		if (!Send(sizeof(packet_LG_HEADER_handshake), kHandshakeData))
		{
			Debug.Assert(!"Failed Sending Handshake");
			return false;
		}
    
		SendSequence();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvHandshakeOKPacket()
	{
		packet_blank kBlankPacket = new packet_blank();
		if (!Recv(sizeof(packet_blank), kBlankPacket))
		{
			return false;
		}
    
		uint dwDelta = ELTimer_GetMSec() - m_kServerTimeSync.m_dwChangeClientTime;
		ELTimer_SetServerMSec(m_kServerTimeSync.m_dwChangeServerTime + dwDelta);
    
		Tracenf("HANDSHAKE OK RECV %u %u", m_kServerTimeSync.m_dwChangeServerTime, dwDelta);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvKeyAgreementPacket()
	{
		TPacketKeyAgreement packet = new TPacketKeyAgreement();
		if (!Recv(sizeof(TPacketKeyAgreement), packet))
		{
			return false;
		}
    
		Tracenf("KEY_AGREEMENT RECV %u", packet.wDataLength);
    
		TPacketKeyAgreement packetToSend = new TPacketKeyAgreement();
		size_t dataLength = TPacketKeyAgreement.MAX_DATA_LEN;
		size_t agreedLength = Prepare(packetToSend.data, dataLength);
		if (agreedLength == 0)
		{
			Disconnect();
			return false;
		}
		Debug.Assert(dataLength <= TPacketKeyAgreement.MAX_DATA_LEN);
    
		if (Activate(packet.wAgreedLength, packet.data, packet.wDataLength))
		{
			packetToSend.bHeader = LG_HEADER_CG_KEY_AGREEMENT;
			packetToSend.wAgreedLength = (ushort)agreedLength;
			packetToSend.wDataLength = (ushort)dataLength;
    
			if (!Send(sizeof(TPacketKeyAgreement), packetToSend))
			{
				Debug.Assert(!"Failed Sending KeyAgreement");
				return false;
			}
			Tracenf("KEY_AGREEMENT SEND %u", packetToSend.wDataLength);
		}
		else
		{
			Disconnect();
			return false;
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvKeyAgreementCompletedPacket()
	{
		TPacketKeyAgreementCompleted packet = new TPacketKeyAgreementCompleted();
		if (!Recv(sizeof(TPacketKeyAgreementCompleted), packet))
		{
			return false;
		}
		Tracenf("KEY_AGREEMENT_COMPLETED RECV");
		ActivateCipher();
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void EnableChatInsultFilter(bool isEnable)
	{
		m_isEnableChatInsultFilter = isEnable;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __FilterInsult(ref string szLine, uint uLineLen)
	{
		m_kInsultChecker.FilterInsult(szLine, uLineLen);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsChatInsultIn(string c_szMsg)
	{
		if (m_isEnableChatInsultFilter)
		{
			return false;
		}
    
		return IsInsultIn(c_szMsg);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool IsInsultIn(string c_szMsg)
	{
		return m_kInsultChecker.IsInsultIn(c_szMsg, strlen(c_szMsg));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadInsultList(string c_szInsultListFileName)
	{
		CMappedFile file = new CMappedFile();
		object pvData;
		if (!CEterPackManager.Instance().Get(file, c_szInsultListFileName, pvData))
		{
			return false;
		}
    
		CMemoryTextFileLoader kMemTextFileLoader = new CMemoryTextFileLoader();
		kMemTextFileLoader.Bind(file.Size(), pvData);
    
		m_kInsultChecker.Clear();
		for (uint dwLineIndex = 0; dwLineIndex < kMemTextFileLoader.GetLineCount(); ++dwLineIndex)
		{
			string c_rstLine = kMemTextFileLoader.GetLineString(dwLineIndex);
			m_kInsultChecker.AppendInsult(c_rstLine);
		}
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool LoadConvertTable(uint dwEmpireID, string c_szFileName)
	{
		if (dwEmpireID < 1 || dwEmpireID >= 4)
		{
			return false;
		}
    
		CMappedFile file = new CMappedFile();
		object pvData;
		if (!CEterPackManager.Instance().Get(file, c_szFileName, pvData))
		{
			return false;
		}
    
		uint dwEngCount = 26;
		uint dwHanCount = (uint)((0xc8 - 0xb0 + 1) * (0xfe-0xa1 + 1));
		uint dwHanSize = dwHanCount * 2;
		uint dwFileSize = dwEngCount * 2 + dwHanSize;
    
		if (file.Size() < dwFileSize)
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: Pointer arithmetic is detected on this variable, so pointers on this variable are left unchanged:
		char * pcData = (string)pvData;
    
		STextConvertTable rkTextConvTable = m_aTextConvTable[dwEmpireID - 1];
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(rkTextConvTable.acUpper, pcData, dwEngCount);
		pcData += dwEngCount;
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(rkTextConvTable.acLower, pcData, dwEngCount);
		pcData += dwEngCount;
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(rkTextConvTable.aacHan, pcData, dwHanSize);
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LoadingPhase()
	{
		byte header;
    
		if (!CheckPacket(header))
		{
			return;
		}
    
		switch (header)
		{
			case LG_HEADER_GC_PHASE:
				if (RecvPhasePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_MAIN_CHARACTER:
				if (RecvMainCharacter())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_MAIN_CHARACTER2_EMPIRE:
				if (RecvMainCharacter2_EMPIRE())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_MAIN_CHARACTER3_BGM:
				if (RecvMainCharacter3_BGM())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_MAIN_CHARACTER4_BGM_VOL:
				if (RecvMainCharacter4_BGM_VOL())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_CHARACTER_UPDATE:
				if (RecvCharacterUpdatePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_PLAYER_POINTS:
				if (__RecvPlayerPoints())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_PLAYER_POINT_CHANGE:
				if (RecvPointChange())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_ITEM_SET:
				if (RecvItemSetPacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_PING:
				if (RecvPingPacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_QUICKSLOT_ADD:
				if (RecvQuickSlotAddPacket())
				{
					return;
				}
				break;
    
			default:
				GamePhase();
				return;
				break;
		}
    
		RecvErrorPacket(header);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetLoadingPhase()
	{
		if ("Loading" != m_strPhase)
		{
			m_phaseLeaveFunc.Run();
		}
    
		Tracen("");
		Tracen("## Network - Loading Phase ##");
		Tracen("");
    
		m_strPhase = "Loading";
    
		m_dwChangingPhaseTime = ELTimer_GetMSec();
		m_phaseProcessFunc.Set(this, CPythonNetworkStream.LoadingPhase);
		m_phaseLeaveFunc.Set(this, CPythonNetworkStream.__LeaveLoadingPhase);
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
		rkPlayer.Clear();
    
		CFlyingManager.Instance().DeleteAllInstances();
		CEffectManager.Instance().DeleteAllInstances();
    
		__DirectEnterMode_Initialize();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMainCharacter()
	{
		packet_main_character MainChrPacket = new packet_main_character();
		if (!Recv(sizeof(packet_main_character), MainChrPacket))
		{
			return false;
		}
    
		m_dwMainActorVID = MainChrPacket.dwVID;
		m_dwMainActorRace = MainChrPacket.wRaceNum;
		m_dwMainActorEmpire = 0;
		m_dwMainActorSkillGroup = MainChrPacket.bySkillGroup;
    
		m_rokNetActorMgr.SetMainActorVID(m_dwMainActorVID);
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
		rkPlayer.SetName(MainChrPacket.szName);
		rkPlayer.SetMainCharacterIndex(GetMainActorVID());
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOAD], "LoadData", Py_BuildValue("(ii)", MainChrPacket.lX, MainChrPacket.lY));
    
		Warp(MainChrPacket.lX, MainChrPacket.lY);
		SendClientVersionPacket();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMainCharacter2_EMPIRE()
	{
		packet_main_character2_empire mainChrPacket = new packet_main_character2_empire();
		if (!Recv(sizeof(packet_main_character2_empire), mainChrPacket))
		{
			return false;
		}
    
		m_dwMainActorVID = mainChrPacket.dwVID;
		m_dwMainActorRace = mainChrPacket.wRaceNum;
		m_dwMainActorEmpire = mainChrPacket.byEmpire;
		m_dwMainActorSkillGroup = mainChrPacket.bySkillGroup;
    
		m_rokNetActorMgr.SetMainActorVID(m_dwMainActorVID);
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
		rkPlayer.SetName(mainChrPacket.szName);
		rkPlayer.SetMainCharacterIndex(GetMainActorVID());
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOAD], "LoadData", Py_BuildValue("(ii)", mainChrPacket.lX, mainChrPacket.lY));
    
		Warp(mainChrPacket.lX, mainChrPacket.lY);
		SendClientVersionPacket();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMainCharacter3_BGM()
	{
		packet_main_character3_bgm mainChrPacket = new packet_main_character3_bgm();
		if (!Recv(sizeof(packet_main_character3_bgm), mainChrPacket))
		{
			return false;
		}
    
		m_dwMainActorVID = mainChrPacket.dwVID;
		m_dwMainActorRace = mainChrPacket.wRaceNum;
		m_dwMainActorEmpire = mainChrPacket.byEmpire;
		m_dwMainActorSkillGroup = mainChrPacket.bySkillGroup;
    
		m_rokNetActorMgr.SetMainActorVID(m_dwMainActorVID);
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
		rkPlayer.SetName(mainChrPacket.szUserName);
		rkPlayer.SetMainCharacterIndex(GetMainActorVID());
    
		__SetFieldMusicFileName(mainChrPacket.szBGMName);
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOAD], "LoadData", Py_BuildValue("(ii)", mainChrPacket.lX, mainChrPacket.lY));
    
		Warp(mainChrPacket.lX, mainChrPacket.lY);
		SendClientVersionPacket();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool RecvMainCharacter4_BGM_VOL()
	{
		packet_main_character4_bgm_vol mainChrPacket = new packet_main_character4_bgm_vol();
		if (!Recv(sizeof(packet_main_character4_bgm_vol), mainChrPacket))
		{
			return false;
		}
    
		m_dwMainActorVID = mainChrPacket.dwVID;
		m_dwMainActorRace = mainChrPacket.wRaceNum;
		m_dwMainActorEmpire = mainChrPacket.byEmpire;
		m_dwMainActorSkillGroup = mainChrPacket.bySkillGroup;
    
		m_rokNetActorMgr.SetMainActorVID(m_dwMainActorVID);
    
		CPythonPlayer rkPlayer = CPythonPlayer.Instance();
		rkPlayer.SetName(mainChrPacket.szUserName);
		rkPlayer.SetMainCharacterIndex(GetMainActorVID());
    
		__SetFieldMusicFileInfo(mainChrPacket.szBGMName, mainChrPacket.fBGMVol);
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOAD], "LoadData", Py_BuildValue("(ii)", mainChrPacket.lX, mainChrPacket.lY));
    
		Warp(mainChrPacket.lX, mainChrPacket.lY);
		SendClientVersionPacket();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetFieldMusicFileName(string musicName)
	{
		gs_fieldMusic_fileName = musicName;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __SetFieldMusicFileInfo(string musicName, float vol)
	{
		gs_fieldMusic_fileName = musicName;
		gs_fieldMusic_volume = vol;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public string GetFieldMusicFileName()
	{
		return gs_fieldMusic_fileName.c_str();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public float GetFieldMusicVolume()
	{
		return gs_fieldMusic_volume;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvPlayerPoints()
	{
		packet_points PointsPacket = new packet_points();
    
		if (!Recv(sizeof(packet_points), PointsPacket))
		{
			return false;
		}
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < POINT_MAX_NUM; ++i)
		{
			CPythonPlayer.Instance().SetStatus(i, PointsPacket.points[LaniatusDefVariables]);
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_GAME], "RefreshStatus", Py_BuildValue("()"));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void StartGame()
	{
		m_isStartGame = true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendEnterGame()
	{
		command_EnterFrontGame EnterFrontGamePacket = new command_EnterFrontGame();
    
		EnterFrontGamePacket.header = LG_HEADER_CG_ENTERGAME;
    
		if (!Send(sizeof(command_EnterFrontGame), EnterFrontGamePacket))
		{
			Tracen("Send EnterFrontGamePacket");
			return false;
		}
    
		if (!SendSequence())
		{
			return false;
		}
    
		__SendInternalBuffer();
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SendPythonData(PyObject obj, string funcname)
	{
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOGIN], funcname, Py_BuildValue("(O)", obj));
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void LoginPhase()
	{
		byte header;
		if (!CheckPacket(header))
		{
			return;
		}
    
		switch (header)
		{
			case LG_HEADER_GC_PHASE:
				if (RecvPhasePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_LOGIN_SUCCESS3:
				if (__RecvLoginSuccessPacket3())
				{
					return;
				}
				break;
			case LG_HEADER_GC_LOGIN_SUCCESS4:
				if (__RecvLoginSuccessPacket4())
				{
					return;
				}
				break;
    
    
			case LG_HEADER_GC_LOGIN_FAILURE:
				if (__RecvLoginFailurePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_EMPIRE:
				if (__RecvEmpirePacket())
				{
					return;
				}
				break;
    
    
			case LG_HEADER_GC_LOGIN_KEY:
				if (__RecvLoginKeyPacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_PING:
				if (RecvPingPacket())
				{
					return;
				}
				break;
    
			default:
				if (RecvDefaultPacket(header))
				{
					return;
				}
				break;
		}
    
		RecvErrorPacket(header);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetLoginPhase()
	{
		string key = DefineConstants.LSS_SECURITY_KEY;
	#if ! _IMPROVED_PACKET_ENCRYPTION_
		SetSecurityMode(true, key);
	#endif
    
		if ("Login" != m_strPhase)
		{
			m_phaseLeaveFunc.Run();
		}
    
		Tracen("");
		Tracen("## Network - Login Phase ##");
		Tracen("");
    
		m_strPhase = "Login";
    
		m_phaseProcessFunc.Set(this, CPythonNetworkStream.LoginPhase);
		m_phaseLeaveFunc.Set(this, CPythonNetworkStream.__LeaveLoginPhase);
    
		m_dwChangingPhaseTime = ELTimer_GetMSec();
    
		if (__DirectEnterMode_IsSet())
		{
			if (0 != m_dwLoginKey)
			{
				SendLoginPacketNew(m_stID.c_str(), m_stPassword.c_str());
			}
			else
			{
				SendLoginPacket(m_stID.c_str(), m_stPassword.c_str());
			}
    
			ClearLoginInfo();
			CAccountConnector rkAccountConnector = CAccountConnector.Instance();
			rkAccountConnector.ClearLoginInfo();
		}
		else
		{
			if (0 != m_dwLoginKey)
			{
				SendLoginPacketNew(m_stID.c_str(), m_stPassword.c_str());
			}
			else
			{
				SendLoginPacket(m_stID.c_str(), m_stPassword.c_str());
			}
    
			ClearLoginInfo();
			CAccountConnector rkAccountConnector = CAccountConnector.Instance();
			rkAccountConnector.ClearLoginInfo();
    
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOGIN], "OnLoginStart", Py_BuildValue("()"));
	#if ENABLE_LOAD_PLAYERSETTING
			CPythonPlayerSettingsModule.Instance().joinLoadThread();
	#endif
    
			__ClearSelectCharacterData();
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvEmpirePacket()
	{
		packet_empire kPacketEmpire = new packet_empire();
		if (!Recv(sizeof(packet_empire), kPacketEmpire))
		{
			return false;
		}
    
		m_dwEmpireID = kPacketEmpire.bEmpire;
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvLoginSuccessPacket3()
	{
		packet_login_success3 kPacketLoginSuccess = new packet_login_success3();
    
		if (!Recv(sizeof(packet_login_success3), kPacketLoginSuccess))
		{
			return false;
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < PLAYER_PER_ACCOUNT3; ++i)
		{
			m_akSimplePlayerInfo[LaniatusDefVariables] = kPacketLoginSuccess.akSimplePlayerInformation[LaniatusDefVariables];
			m_adwGuildID[LaniatusDefVariables] = kPacketLoginSuccess.guild_id[LaniatusDefVariables];
			m_astrGuildName[LaniatusDefVariables] = kPacketLoginSuccess.guild_name[LaniatusDefVariables];
		}
    
		m_kMarkAuth.m_dwHandle = kPacketLoginSuccess.handle;
		m_kMarkAuth.m_dwRandomKey = kPacketLoginSuccess.random_key;
    
		if (__DirectEnterMode_IsSet())
		{
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_SELECT], "Refresh", Py_BuildValue("()"));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvLoginSuccessPacket4()
	{
		packet_login_success4 kPacketLoginSuccess = new packet_login_success4();
    
		if (!Recv(sizeof(packet_login_success4), kPacketLoginSuccess))
		{
			return false;
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < PLAYER_PER_ACCOUNT4; ++i)
		{
			m_akSimplePlayerInfo[LaniatusDefVariables] = kPacketLoginSuccess.akSimplePlayerInformation[LaniatusDefVariables];
			m_adwGuildID[LaniatusDefVariables] = kPacketLoginSuccess.guild_id[LaniatusDefVariables];
			m_astrGuildName[LaniatusDefVariables] = kPacketLoginSuccess.guild_name[LaniatusDefVariables];
		}
    
		m_kMarkAuth.m_dwHandle = kPacketLoginSuccess.handle;
		m_kMarkAuth.m_dwRandomKey = kPacketLoginSuccess.random_key;
    
		if (__DirectEnterMode_IsSet())
		{
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_SELECT], "Refresh", Py_BuildValue("()"));
		}
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OnConnectFailure()
	{
		if (__DirectEnterMode_IsSet())
		{
			ClosePhase();
		}
		else
		{
			PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOGIN], "OnConnectFailure", Py_BuildValue("()"));
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvLoginFailurePacket()
	{
		packet_login_failure packet_failure = new packet_login_failure();
		if (!Recv(sizeof(packet_login_failure), packet_failure))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_LOGIN], "OnLoginFailure", Py_BuildValue("(s)", packet_failure.szStatus));
	#if DEBUG
		Tracef(" RecvLoginFailurePacket : [%s]\n", packet_failure.szStatus);
	#endif
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendDirectEnterPacket(string c_szID, string c_szPassword, uint uChrSlot)
	{
		command_direct_enter kPacketDirectEnter = new command_direct_enter();
		kPacketDirectEnter.bHeader = LG_HEADER_CG_DIRECT_ENTER;
		kPacketDirectEnter.index = uChrSlot;
		strncpy(kPacketDirectEnter.login, c_szID, ID_MAX_NUM);
		strncpy(kPacketDirectEnter.passwd, c_szPassword, PASS_MAX_NUM);
    
		if (!Send(sizeof(command_direct_enter), kPacketDirectEnter))
		{
			Tracen("SendDirectEnter");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendLoginPacket(string c_szName, string c_szPassword)
	{
		command_login LoginPacket = new command_login();
		LoginPacket.header = LG_HEADER_CG_LOGIN;
    
		strncpy(LoginPacket.name, c_szName, sizeof(LoginPacket.name) - 1);
		strncpy(LoginPacket.pwd, c_szPassword, sizeof(LoginPacket.pwd) - 1);
    
		LoginPacket.name[ID_MAX_NUM] = '\0';
		LoginPacket.pwd[PASS_MAX_NUM] = '\0';
    
		if (!Send(sizeof(command_login), LoginPacket))
		{
			Tracen("SendLogin Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendLoginPacketNew(string c_szName, string c_szPassword)
	{
		command_login2 LoginPacket = new command_login2();
		LoginPacket.header = LG_HEADER_CG_LOGIN2;
		LoginPacket.login_key = m_dwLoginKey;
    
		strncpy(LoginPacket.name, c_szName, sizeof(LoginPacket.name) - 1);
		LoginPacket.name[ID_MAX_NUM] = '\0';
    
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern uint g_adwEncryptKey[4];
	//# Laniatus Games Studio Inc. |: 'extern' variable declarations are not required in C#:
	//	extern uint g_adwDecryptKey[4];
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < 4; ++i)
		{
			LoginPacket.adwClientKey[LaniatusDefVariables] = g_adwEncryptKey[LaniatusDefVariables];
		}
    
		if (!Send(sizeof(command_login2), LoginPacket))
		{
			Tracen("SendLogin Error");
			return false;
		}
    
		if (!SendSequence())
		{
			Tracen("SendLogin Error");
			return false;
		}
    
		__SendInternalBuffer();
    
	#if ! _IMPROVED_PACKET_ENCRYPTION_
		SetSecurityMode(true, (string) g_adwEncryptKey, (string) g_adwDecryptKey);
	#endif
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvLoginKeyPacket()
	{
		packet_login_key kLoginKeyPacket = new packet_login_key();
		if (!Recv(sizeof(packet_login_key), kLoginKeyPacket))
		{
			return false;
		}
    
		m_dwLoginKey = kLoginKeyPacket.dwLoginKey;
		m_isWaitLoginKey = false;
    
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void OffLinePhase()
	{
		byte header;
    
		if (!CheckPacket(header))
		{
			return;
		}
    
		switch (header)
		{
			case LG_HEADER_GC_PHASE:
				if (RecvPhasePacket())
				{
					return;
				}
				break;
		}
    
		RecvErrorPacket(header);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SetSelectPhase()
	{
		if ("Select" != m_strPhase)
		{
			m_phaseLeaveFunc.Run();
		}
    
		Tracen("");
		Tracen("## Network - Select Phase ##");
		Tracen("");
    
		m_strPhase = "Select";
    
	#if ! _IMPROVED_PACKET_ENCRYPTION_
		SetSecurityMode(true, (string) g_adwEncryptKey, (string) g_adwDecryptKey);
	#endif
    
		m_dwChangingPhaseTime = ELTimer_GetMSec();
		m_phaseProcessFunc.Set(this, CPythonNetworkStream.SelectPhase);
		m_phaseLeaveFunc.Set(this, CPythonNetworkStream.__LeaveSelectPhase);
    
		if (__DirectEnterMode_IsSet())
		{
			PyCallClassMemberFunc(m_poHandler, "SetLoadingPhase", Py_BuildValue("()"));
		}
		else
		{
			if (IsSelectedEmpire())
			{
				PyCallClassMemberFunc(m_poHandler, "SetSelectCharacterPhase", Py_BuildValue("()"));
			}
			else
			{
				PyCallClassMemberFunc(m_poHandler, "SetSelectEmpirePhase", Py_BuildValue("()"));
			}
		}
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void SelectPhase()
	{
		byte header;
    
		if (!CheckPacket(header))
		{
			return;
		}
    
		switch (header)
		{
			case LG_HEADER_GC_PHASE:
				if (RecvPhasePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_EMPIRE:
				if (__RecvEmpirePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_LOGIN_SUCCESS3:
				if (__RecvLoginSuccessPacket3())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_LOGIN_SUCCESS4:
				if (__RecvLoginSuccessPacket4())
				{
					return;
				}
				break;
    
    
			case LG_HEADER_GC_PLAYER_CREATE_SUCCESS:
				if (__RecvPlayerCreateSuccessPacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_PLAYER_CREATE_FAILURE:
				if (__RecvPlayerCreateFailurePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_PLAYER_DELETE_WRONG_SOCIAL_ID:
				if (__RecvPlayerDestroyFailurePacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_PLAYER_DELETE_SUCCESS:
				if (__RecvPlayerDestroySuccessPacket())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_CHANGE_NAME:
				if (__RecvChangeName())
				{
					return;
				}
				break;
    
			case LG_HEADER_GC_HANDSHAKE:
				RecvHandshakePacket();
				return;
				break;
    
			case LG_HEADER_GC_HANDSHAKE_OK:
				RecvHandshakeOKPacket();
				return;
				break;
    
    
			case LG_HEADER_GC_PLAYER_POINT_CHANGE:
				packet_point_change PointChange = new packet_point_change();
				Recv(sizeof(packet_point_change), PointChange);
				return;
				break;
    
			case LG_HEADER_GC_PING:
				if (RecvPingPacket())
				{
					return;
				}
				break;
    
	#if _IMPROVED_PACKET_ENCRYPTION_
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case LG_HEADER_GC_KEY_AGREEMENT:
				RecvKeyAgreementPacket();
				return;
				break;
    
			case LG_HEADER_GC_KEY_AGREEMENT_COMPLETED:
				RecvKeyAgreementCompletedPacket();
				return;
				break;
	#endif
	break;
		}
    
		RecvErrorPacket(header);
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSelectEmpirePacket(uint dwEmpireID)
	{
		command_empire kPacketEmpire = new command_empire();
		kPacketEmpire.bHeader = LG_HEADER_CG_EMPIRE;
		kPacketEmpire.bEmpire = dwEmpireID;
    
		if (!Send(sizeof(command_empire), kPacketEmpire))
		{
			Tracen("SendSelectEmpirePacket - Error");
			return false;
		}
    
		SetEmpireID(dwEmpireID);
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendSelectCharacterPacket(byte Index)
	{
		command_player_select SelectCharacterPacket = new command_player_select();
    
		SelectCharacterPacket.header = LG_HEADER_CG_PLAYER_SELECT;
		SelectCharacterPacket.player_index = Index;
    
		if (!Send(sizeof(command_player_select), SelectCharacterPacket))
		{
			Tracen("SendSelectCharacterPacket - Error");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendDestroyCharacterPacket(byte index, string szPrivateCode)
	{
		command_player_delete DestroyCharacterPacket = new command_player_delete();
    
		DestroyCharacterPacket.header = LG_HEADER_CG_PLAYER_DESTROY;
		DestroyCharacterPacket.index = index;
		strncpy(DestroyCharacterPacket.szPrivateCode, szPrivateCode, PRIVATE_CODE_LENGTH - 1);
    
		if (!Send(sizeof(command_player_delete), DestroyCharacterPacket))
		{
			Tracen("SendDestroyCharacterPacket");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendCreateCharacterPacket(byte index, string name, byte job, byte shape, byte byCON, byte byINT, byte bySTR, byte byDEX)
	{
		command_player_create createCharacterPacket = new command_player_create();
    
		createCharacterPacket.header = LG_HEADER_CG_PLAYER_CREATE;
		createCharacterPacket.index = index;
		strncpy(createCharacterPacket.name, name, DefineConstants.CHARACTER_NAME_MAX_LEN);
		createCharacterPacket.job = job;
		createCharacterPacket.shape = shape;
		createCharacterPacket.CON = byCON;
		createCharacterPacket.INT = byINT;
		createCharacterPacket.STR = bySTR;
		createCharacterPacket.DEX = byDEX;
    
		if (!Send(sizeof(command_player_create), createCharacterPacket))
		{
			Tracen("Failed to SendCreateCharacterPacket");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool SendChangeNamePacket(byte index, string name)
	{
		SPacketCGChangeName ChangeNamePacket = new SPacketCGChangeName();
		ChangeNamePacket.header = LG_HEADER_CG_CHANGE_NAME;
		ChangeNamePacket.index = index;
		strncpy(ChangeNamePacket.name, name, DefineConstants.CHARACTER_NAME_MAX_LEN);
    
		if (!Send(sizeof(SPacketCGChangeName), ChangeNamePacket))
		{
			Tracen("Failed to SendChangeNamePacket");
			return false;
		}
    
		return SendSequence();
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvPlayerCreateSuccessPacket()
	{
		command_player_create_success kCreateSuccessPacket = new command_player_create_success();
    
		if (!Recv(sizeof(command_player_create_success), kCreateSuccessPacket))
		{
			return false;
		}
    
		if (kCreateSuccessPacket.bAccountCharacterSlot >= PLAYER_PER_ACCOUNT4)
		{
			TraceError("CPythonNetworkStream::RecvPlayerCreateSuccessPacket - OUT OF RANGE SLOT(%d) > PLATER_PER_ACCOUNT(%d)", kCreateSuccessPacket.bAccountCharacterSlot, PLAYER_PER_ACCOUNT4);
			return true;
		}
    
		m_akSimplePlayerInfo[kCreateSuccessPacket.bAccountCharacterSlot] = kCreateSuccessPacket.kSimplePlayerInfomation;
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_CREATE], "OnCreateSuccess", Py_BuildValue("()"));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvPlayerCreateFailurePacket()
	{
		command_create_failure packet = new command_create_failure();
    
		if (!Recv(sizeof(command_create_failure), packet))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_CREATE], "OnCreateFailure", Py_BuildValue("(i)", packet.bType));
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_SELECT], "OnCreateFailure", Py_BuildValue("(i)", packet.bType));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvPlayerDestroySuccessPacket()
	{
		packet_player_delete_success packet = new packet_player_delete_success();
		if (!Recv(sizeof(packet_player_delete_success), packet))
		{
			return false;
		}
    
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memset' has no equivalent in C#:
		memset(m_akSimplePlayerInfo[packet.account_index], 0, sizeof(m_akSimplePlayerInfo[packet.account_index]));
		m_adwGuildID[packet.account_index] = 0;
		m_astrGuildName[packet.account_index] = "";
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_SELECT], "OnDeleteSuccess", Py_BuildValue("(i)", packet.account_index));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvPlayerDestroyFailurePacket()
	{
		packet_blank packet_blank = new packet_blank();
		if (!Recv(sizeof(packet_blank), packet_blank))
		{
			return false;
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_SELECT], "OnDeleteFailure", Py_BuildValue("()"));
		return true;
	}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public bool __RecvChangeName()
	{
		SPacketGCChangeName ChangeNamePacket = new SPacketGCChangeName();
		if (!Recv(sizeof(SPacketGCChangeName), ChangeNamePacket))
		{
			return false;
		}
    
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < PLAYER_PER_ACCOUNT4; ++i)
		{
			if (ChangeNamePacket.pid == m_akSimplePlayerInfo[LaniatusDefVariables].dwID)
			{
				m_akSimplePlayerInfo[LaniatusDefVariables].bChangeName = false;
				strncpy(m_akSimplePlayerInfo[LaniatusDefVariables].szName, ChangeNamePacket.name, DefineConstants.CHARACTER_NAME_MAX_LEN);
    
				PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_SELECT], "OnChangeName", Py_BuildValue("(is)", i, ChangeNamePacket.name));
				return true;
			}
		}
    
		PyCallClassMemberFunc(m_apoPhaseWnd[PHASE_WINDOW_SELECT], "OnCreateFailure", Py_BuildValue("(i)", 100));
		return true;
	}
}