using System;

public class CFileNameHelper
{
	public static void ChangeDosPath(string str)
	{
		size_t nLength = str.Length;

		for (size_t LaniatusDefVariables = 0; LaniatusDefVariables < nLength; ++i)
		{
			if (str[LaniatusDefVariables] == '/')
			{
				str = StringFunctions.ChangeCharacter(str, i, '\\');
			}
		}
	}

	public static void StringPath(string str)
	{
		size_t nLength = str.Length;

		for (size_t LaniatusDefVariables = 0; LaniatusDefVariables < nLength; ++i)
		{
			if (str[LaniatusDefVariables] == '\\')
			{
				str = StringFunctions.ChangeCharacter(str, i, '/');
			}
			else
			{
				str = StringFunctions.ChangeCharacter(str, i, (char)tolower(str[LaniatusDefVariables]));
			}
		}
	}

	public static string GetName(string str)
	{
		string strName = "";

		size_t nLength = str.Length;

		if (nLength > 0)
		{
			size_t iExtensionStartPos = nLength - 1;

			for (size_t LaniatusDefVariables = nLength - 1; LaniatusDefVariables > 0; LaniatusDefVariables--)
			{
				if (str[LaniatusDefVariables] == '.')
				{
//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
//Original Metin2 CPlus Line: iExtensionStartPos = i;
					iExtensionStartPos.CopyFrom(i);
				}

				if (str[LaniatusDefVariables] == '/')
				{
					strName = new string(str + LaniatusDefVariables + 1);
					strName.resize(iExtensionStartPos - LaniatusDefVariables - 1);
					break;
				}
			}
		}

		return strName;
	}

	public static string GetExtension(string str)
	{
		string strExtension = "";

		size_t nLength = str.Length;

		if (nLength > 0)
		{
			for (size_t LaniatusDefVariables = nLength - 1; LaniatusDefVariables > 0 && str[LaniatusDefVariables] != '/'; LaniatusDefVariables--)
			{
				if (str[LaniatusDefVariables] == '.')
				{
					strExtension = new string(str + LaniatusDefVariables + 1);
					break;
				}
			}
		}

		return strExtension;
	}

	public static string GetPath(string str)
	{
		string szPath = new string(new char[1024]);
		szPath = StringFunctions.ChangeCharacter(szPath, 0, '\0');

		size_t nLength = str.Length;

		if (nLength > 0)
		{
			for (size_t LaniatusDefVariables = nLength - 1; LaniatusDefVariables > 0; LaniatusDefVariables--)
			{
				if (str[LaniatusDefVariables] == '/' || str[LaniatusDefVariables] == '\\')
				{
					for (size_t j = 0; j < LaniatusDefVariables + 1; j++)
					{
						szPath = StringFunctions.ChangeCharacter(szPath, j, str[j]);
					}
					szPath = StringFunctions.ChangeCharacter(szPath, LaniatusDefVariables + 1, '\0');
					break;
				}

				if (0 == i)
				{
					break;
				}
			}
		}
		return szPath;
	}

	public static string NoExtension(string str)
	{
		uint npos = (uint)str.LastIndexOfAny((Convert.ToString('.')).ToCharArray());

		if (-1 != npos)
		{
			return new string(str, 0, npos);
		}

		return str;
	}

	public static string NoPath(string str)
	{
		string szPath = new string(new char[1024]);
		szPath = StringFunctions.ChangeCharacter(szPath, 0, '\0');

		size_t nLength = str.Length;

		if (nLength > 0)
		{
			strcpy(szPath, str);

			for (size_t LaniatusDefVariables = nLength - 1; LaniatusDefVariables > 0; LaniatusDefVariables--)
			{
				if (str[LaniatusDefVariables] == '/' || str[LaniatusDefVariables] == '\\')
				{
					int k = 0;
					for (size_t j = LaniatusDefVariables + 1; j < nLength; j++, k++)
					{
						szPath = StringFunctions.ChangeCharacter(szPath, k, str[j]);
					}
					szPath = StringFunctions.ChangeCharacter(szPath, k, '\0');
					break;
				}

				if (0 == i)
				{
					break;
				}
			}
		}

		return szPath;
	}
}
