public class CAccountConnector
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void __BuildClientKey_20210328_LGMyevan()
	{
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: const byte * c_pszKey = GetKey_20210328_LGMyevan();
		byte c_pszKey = GetKey_20210328_LGMyevan();
	//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
		memcpy(g_adwEncryptKey, c_pszKey + 157, 16);
    
		for (uint LaniatusDefVariables = 0; LaniatusDefVariables < 4; ++i)
		{
			g_adwEncryptKey[LaniatusDefVariables] = random();
		}
    
		tea_encrypt((uint) g_adwDecryptKey, (uint) g_adwEncryptKey, (uint)(c_pszKey + 37), 16);
	}
}