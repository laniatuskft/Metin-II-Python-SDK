public class CPythonPlayer
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public uint __GetRaceStat()
	{
		switch (GetRace())
		{
			case MAIN_RACE_WARRIOR_M:
			case MAIN_RACE_WARRIOR_W:
				return GetStatus(POINT_ST);
				break;
			case MAIN_RACE_ASSASSIN_M:
			case MAIN_RACE_ASSASSIN_W:
				return GetStatus(POINT_DX);
				break;
			case MAIN_RACE_SURA_M:
			case MAIN_RACE_SURA_W:
				return GetStatus(POINT_ST);
				break;
			case MAIN_RACE_SHAMAN_M:
			case MAIN_RACE_SHAMAN_W:
				return GetStatus(POINT_IQ);
				break;
	#if ENABLE_WOLFMAN
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not allow fall-through from a non-empty 'case':
			case MAIN_RACE_WOLFMAN_M:
				return GetStatus(POINT_DX);
				break;
	#endif
	break;
		}
		return GetStatus(POINT_ST);
	}
}