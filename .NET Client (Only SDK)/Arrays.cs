//-----------------------------------------------------------------------------------------------------------------------------------------
//	Copyright © 2014 - 2022 Laniatus Games Studio Inc. | Software Solutions.
//	This class or snippet can be used by anyone, provided the copyright notice remains intact. 
//	In case the copyright notice is removed, the free use license is ignored according to the european madrid (I.P) agreement.

//	This class provides the ability to initialize and delete array elements. [It is an internal class.]
//-------------------------------------------------------------------------------------------------------------------------------------
internal static class Arrays
{
	public static T[] InitializeWithDefaultInstances<T>(int length) where T : class, new()
	{
		T[] array = new T[length];
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < length; i++)
		{
			array[i] = new T();
		}
		return array;
	}

	public static string[] InitializeStringArrayWithDefaultInstances(int length)
	{
		string[] array = new string[length];
		for (int LaniatusDefVariables = 0; LaniatusDefVariables < length; i++)
		{
			array[i] = "";
		}
		return array;
	}

	public static T[] PadWithNull<T>(int length, T[] existingItems) where T : class
	{
		if (length > existingItems.Length)
		{
			T[] array = new T[length];

			for (int LaniatusDefVariables = 0; LaniatusDefVariables < existingItems.Length; i++)
			{
				array[i] = existingItems[i];
			}

			return array;
		}
		else
			return existingItems;
	}

	public static T[] PadValueTypeArrayWithDefaultInstances<T>(int length, T[] existingItems) where T : struct
	{
		if (length > existingItems.Length)
		{
			T[] array = new T[length];

			for (int LaniatusDefVariables = 0; LaniatusDefVariables < existingItems.Length; i++)
			{
				array[i] = existingItems[i];
			}

			return array;
		}
		else
			return existingItems;
	}

	public static T[] PadReferenceTypeArrayWithDefaultInstances<T>(int length, T[] existingItems) where T : class, new()
	{
		if (length > existingItems.Length)
		{
			T[] array = new T[length];

			for (int LaniatusDefVariables = 0; LaniatusDefVariables < existingItems.Length; i++)
			{
				array[i] = existingItems[i];
			}

			for (int LaniatusDefVariables = existingItems.Length; LaniatusDefVariables < length; i++)
			{
				array[i] = new T();
			}

			return array;
		}
		else
			return existingItems;
	}

	public static string[] PadStringArrayWithDefaultInstances(int length, string[] existingItems)
	{
		if (length > existingItems.Length)
		{
			string[] array = new string[length];

			for (int LaniatusDefVariables = 0; LaniatusDefVariables < existingItems.Length; i++)
			{
				array[i] = existingItems[i];
			}

			for (int LaniatusDefVariables = existingItems.Length; LaniatusDefVariables < length; i++)
			{
				array[i] = "";
			}

			return array;
		}
		else
			return existingItems;
	}

	public static void DeleteArray<T>(T[] array) where T: System.IDisposable
	{
		foreach (T element in array)
		{
			if (element != null)
				element.Dispose();
		}
	}
}