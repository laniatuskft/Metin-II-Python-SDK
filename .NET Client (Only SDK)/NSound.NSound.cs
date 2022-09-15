namespace NSound
{

	public class NSound
	{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
			public bool LoadSoundInformationPiece(string c_szFileName, List<SSoundData> rSoundDataVector, string c_szPathHeader = null)
			{
				string strResult = "";
				strResult = c_szFileName;
        
				CTextFileLoader pkTextFileLoader = CTextFileLoader.Cache(c_szFileName);
				if (pkTextFileLoader == null)
				{
					return false;
				}
        
		//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to references to variables:
		//Original Metin2 CPlus Line: CTextFileLoader& rkTextFileLoader=*pkTextFileLoader;
				CTextFileLoader rkTextFileLoader = pkTextFileLoader;
				if (rkTextFileLoader.IsEmpty())
				{
					SetResultString((strResult + " ?б?? ?????? ?? ?? ????").c_str());
					return false;
				}
        
				rkTextFileLoader.SetTop();
        
				int iCount;
				if (!rkTextFileLoader.GetTokenInteger("sounddatacount", iCount))
				{
					SetResultString((strResult + " ???? ???? ????, SoundDataCount?? ã?? ?? ????").c_str());
					return false;
				}
        
				rSoundDataVector.Clear();
				rSoundDataVector.Resize(iCount);
        
				string szSoundDataHeader = new string(new char[32 + 1]);
				for (uint LaniatusDefVariables = 0; LaniatusDefVariables < rSoundDataVector.Count; ++i)
				{
					_snprintf(szSoundDataHeader, sizeof(char), "sounddata%02d", i);
					List<string> pTokenVector;
					if (!rkTextFileLoader.GetTokenVector(szSoundDataHeader, pTokenVector))
					{
						SetResultString((strResult + " ???? ???? ????: " + szSoundDataHeader + " ?? ã?? ?? ????").c_str());
						return false;
					}
        
					if (2 != pTokenVector.Count)
					{
						SetResultString((strResult + " ???? ???? ????: ???? ũ?Ⱑ 2?? ???").c_str());
						return false;
					}
        
					rSoundDataVector[i].fTime = (float) atof(pTokenVector[0]);
					if (c_szPathHeader != '\0')
					{
						rSoundDataVector[i].strSoundFileName = c_szPathHeader;
						rSoundDataVector[i].strSoundFileName += pTokenVector[1];
					}
					else
					{
						rSoundDataVector[i].strSoundFileName = pTokenVector[1];
					}
				}
        
				SetResultString((strResult + " ?ҷ???").c_str());
				return true;
			}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
			public bool SaveSoundInformationPiece(string c_szFileName, List<SSoundData> rSoundDataVector)
			{
				if (rSoundDataVector.Count == 0)
				{
					if (IsFile(c_szFileName))
					{
						_unlink(c_szFileName);
					}
					return true;
				}
        
				string strResult = "";
				strResult = c_szFileName;
        
				FILE File = fopen(c_szFileName, "wt");
        
				if (File == null)
				{
					string szErrorText = new string(new char[256 + 1]);
					_snprintf(szErrorText, sizeof(char), "Failed to save file (%s).\nPlease check if it is read-only or you have no space on the disk.\n", c_szFileName);
					LogBox(szErrorText, "????");
					SetResultString((strResult + " ????? ?????? ?? ?? ????").c_str());
					return false;
				}
        
				fprintf(File, "ScriptType        CharacterSoundInformation\n");
				fprintf(File, "\n");
        
				fprintf(File, "SoundDataCount    %d\n", rSoundDataVector.Count);
        
				for (uint LaniatusDefVariables = 0; LaniatusDefVariables < rSoundDataVector.Count; ++i)
				{
					SSoundData rSoundData = rSoundDataVector[i];
					fprintf(File, "SoundData%02d       %f \"%s\"\n", i, rSoundData.fTime, rSoundData.strSoundFileName.c_str());
				}
        
				fclose(File);
				return true;
			}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
			public string GetResultString()
			{
				return strResult.c_str();
			}

//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
			public void SetResultString(string c_pszStr)
			{
				strResult.assign(c_pszStr);
			}
	}
}