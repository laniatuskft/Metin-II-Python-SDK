//-----------------------------------------------------------------------------------------------------------------------------------------
//	Copyright © 2014 - 2022 Laniatus Games Studio Inc. | Software Solutions.
//	This class or snippet can be used by anyone, provided the copyright notice remains intact. 
//	In case the copyright notice is removed, the free use license is ignored according to the european madrid (I.P) agreement.
//	This class includes methods to convert C++ rectangular arrays (jagged arrays
//	with inner arrays of the same length).
//-----------------------------------------------------------------------------------------------------------------------------------------
internal static class RectangularArrays
{
	public static SMeshNode[][] RectangularSMeshNodeArray(int size1, int size2)
	{
		SMeshNode[][] newArray = new SMeshNode[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new SMeshNode[size2];
			for (int array2 = 0; array2 < size2; array2++)
			{
				newArray[array1][array2] = new SMeshNode();
			}
		}

		return newArray;
	}

	public static byte[][] RectangularByteArray(int size1, int size2)
	{
		byte[][] newArray = new byte[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new byte[size2];
		}

		return newArray;
	}

	public static Color8888[][] RectangularColor8888Array(int size1, int size2)
	{
		Color8888[][] newArray = new Color8888[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new Color8888[size2];
			for (int array2 = 0; array2 < size2; array2++)
			{
				newArray[array1][array2] = new Color8888();
			}
		}

		return newArray;
	}

	public static char[][] RectangularCharArray(int size1, int size2)
	{
		char[][] newArray = new char[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new char[size2];
		}

		return newArray;
	}

	public static uint[][] RectangularUintArray(int size1, int size2)
	{
		uint[][] newArray = new uint[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new uint[size2];
		}

		return newArray;
	}

	public static bool[][] RectangularBoolArray(int size1, int size2)
	{
		bool[][] newArray = new bool[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new bool[size2];
		}

		return newArray;
	}

	public static _D3DVECTOR[][] Rectangular_D3DVECTORArray(int size1, int size2)
	{
		_D3DVECTOR[][] newArray = new _D3DVECTOR[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new _D3DVECTOR[size2];
			for (int array2 = 0; array2 < size2; array2++)
			{
				newArray[array1][array2] = new _D3DVECTOR();
			}
		}

		return newArray;
	}

	public static float[][] RectangularFloatArray(int size1, int size2)
	{
		float[][] newArray = new float[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new float[size2];
		}

		return newArray;
	}

	public static int[][] RectangularIntArray(int size1, int size2)
	{
		int[][] newArray = new int[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new int[size2];
		}

		return newArray;
	}

	public static SGuildMarkBlock[][] RectangularSGuildMarkBlockArray(int size1, int size2)
	{
		SGuildMarkBlock[][] newArray = new SGuildMarkBlock[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new SGuildMarkBlock[size2];
			for (int array2 = 0; array2 < size2; array2++)
			{
				newArray[array1][array2] = new SGuildMarkBlock();
			}
		}

		return newArray;
	}

	public static TPlayerItemAttribute[][] RectangularTPlayerItemAttributeArray(int size1, int size2)
	{
		TPlayerItemAttribute[][] newArray = new TPlayerItemAttribute[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new TPlayerItemAttribute[size2];
			for (int array2 = 0; array2 < size2; array2++)
			{
				newArray[array1][array2] = new TPlayerItemAttribute();
			}
		}

		return newArray;
	}

	public static TSwitchbotAttributeAlternativeTable[][] RectangularTSwitchbotAttributeAlternativeTableArray(int size1, int size2)
	{
		TSwitchbotAttributeAlternativeTable[][] newArray = new TSwitchbotAttributeAlternativeTable[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new TSwitchbotAttributeAlternativeTable[size2];
			for (int array2 = 0; array2 < size2; array2++)
			{
				newArray[array1][array2] = new TSwitchbotAttributeAlternativeTable();
			}
		}

		return newArray;
	}

	public static D3DXVECTOR3[][] RectangularD3DXVECTOR3Array(int size1, int size2)
	{
		D3DXVECTOR3[][] newArray = new D3DXVECTOR3[size1][];
		for (int array1 = 0; array1 < size1; array1++)
		{
			newArray[array1] = new D3DXVECTOR3[size2];
			for (int array2 = 0; array2 < size2; array2++)
			{
				newArray[array1][array2] = new D3DXVECTOR3();
			}
		}

		return newArray;
	}
}