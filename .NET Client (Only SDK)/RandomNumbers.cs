//-----------------------------------------------------------------------------------------------------------------------------------------
//	Copyright © 2014 - 2022 Laniatus Games Studio Inc. | Software Solutions.
//	This class or snippet can be used by anyone, provided the copyright notice remains intact. 
//	In case the copyright notice is removed, the free use license is ignored according to the european madrid (I.P) agreement.

//	This class provides the ability to replicate the behavior of the C/C++ functions for 
//	generating random numbers, using the .NET Framework System.Random class.
//	'rand' converts to the parameterless overload of NextNumber
//	'random' converts to the single-parameter overload of NextNumber
//	'randomize' converts to the parameterless overload of Seed
//	'srand' converts to the single-parameter overload of Seed
//-----------------------------------------------------------------------------------------------------------------------------------------

internal static class RandomNumbers
{
	private static System.Random r;

	public static int NextNumber()
	{
		if (r == null)
			Seed();

		return r.Next();
	}

	public static int NextNumber(int ceiling)
	{
		if (r == null)
			Seed();

		return r.Next(ceiling);
	}

	public static void Seed()
	{
		r = new System.Random();
	}

	public static void Seed(int seed)
	{
		r = new System.Random(seed);
	}
}