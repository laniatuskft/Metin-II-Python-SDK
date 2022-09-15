using System.Diagnostics;




//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma pack(push)
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma pack(1)
public class TGA_HEADER
{
	public char idLen;
	public char palType;
	public char imgType;
	public ushort colorBegin;
	public ushort colorCount;
	public char palEntrySize;
	public ushort left;
	public ushort top;
	public ushort width;
	public ushort height;
	public char colorBits;
	public char desc;
}
//# Laniatus Games Studio Inc. | TODO TASK: There is no equivalent to most C++ 'pragma' directives in C#:
//#pragma pack(pop)

public class CImage : System.IDisposable
{
		public CImage()
		{
			Initialize();
		}

		public CImage(CImage image)
		{
			Initialize();

			int w = image.GetWidth();
			int h = image.GetHeight();

			Create(w, h);

//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: uint * pdwDest = GetBasePointer();
			uint pdwDest = GetBasePointer();
//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: uint * pdwSrc = image.GetBasePointer();
			uint pdwSrc = image.GetBasePointer();

//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
			memcpy(pdwDest, pdwSrc, w * h * sizeof(uint));
		}

		public virtual void Dispose()
		{
			Destroy();
		}

		public void Destroy()
		{
			if (m_pdwColors)
			{
				m_pdwColors = null;
				m_pdwColors = null;
			}
		}

		public void Create(int width, int height)
		{
			Destroy();

			m_width = width;
			m_height = height;
			m_pdwColors = new uint[m_width * m_height];
		}

		public void Clear(uint color = 0)
		{
			Debug.Assert(m_pdwColors != null);

			for (int y = 0; y < m_height; ++y)
			{
				uint[] colorLine = m_pdwColors[y * m_width];

				for (int x = 0; x < m_width; ++x)
				{
					colorLine[x] = color;
				}
			}
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int GetWidth() const
		public int GetWidth()
		{
			Debug.Assert(m_pdwColors != null);
			return m_width;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int GetHeight() const
		public int GetHeight()
		{
			Debug.Assert(m_pdwColors != null);
			return m_height;
		}

//# Laniatus Games Studio Inc. | WARN: C# has no equivalent to methods returning pointers to value types:
//Original Metin2 CPlus Line: uint* GetBasePointer()
		public uint GetBasePointer()
		{
			Debug.Assert(m_pdwColors != null);
			return m_pdwColors;
		}

//# Laniatus Games Studio Inc. | WARN: C# has no equivalent to methods returning pointers to value types:
//Original Metin2 CPlus Line: uint* GetLinePointer(int line)
		public uint GetLinePointer(int line)
		{
			Debug.Assert(m_pdwColors != null);
			return m_pdwColors + line * m_width;
		}

		public void PutImage(int x, int y, CImage pImage)
		{
			Debug.Assert(x >= 0 && x + pImage.GetWidth() <= GetWidth());
			Debug.Assert(y >= 0 && y + pImage.GetHeight() <= GetHeight());

			int len = pImage.GetWidth() * sizeof(uint);

			for (int j = 0; j < pImage.GetHeight(); ++j)
			{
//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: uint * pdwDest = GetLinePointer(y + j) + x;
				uint pdwDest = GetLinePointer(y + j) + x;
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
				memcpy(pdwDest, pImage.GetLinePointer(j), len);
			}
		}

		public void FlipTopToBottom()
		{
			uint[] swap = new uint[m_width * m_height];

			int row;
			uint width = (uint)GetWidth();
			uint height = (uint)GetHeight();
//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: uint * end_row;
			uint end_row;
//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
//Original Metin2 CPlus Line: uint * start_row;
			uint start_row;

			for (row = 0; row < GetHeight() / 2; row++)
			{
				end_row = &(m_pdwColors[width * (height - row - 1)]);
				start_row = &(m_pdwColors[width * row]);

//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
				memcpy(swap, end_row, width * sizeof(uint));
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
				memcpy(end_row, start_row, width * sizeof(uint));
//# Laniatus Games Studio Inc. | TODO TASK: The memory management function 'memcpy' has no equivalent in C#:
				memcpy(start_row, swap, width * sizeof(uint));
			}

			swap = null;
		}

		public void SetFileName(string c_szFileName)
		{
			m_stFileName = c_szFileName;
		}

		public string GetFileNameString()
		{
			return m_stFileName;
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool IsEmpty() const
		public bool IsEmpty()
		{
			return (m_pdwColors == null) ? true : false;
		}

		protected void Initialize()
		{
			m_pdwColors = null;
			m_width = 0;
			m_height = 0;
		}

		protected uint[] m_pdwColors;
		protected int m_width;
		protected int m_height;

		protected string m_stFileName = "";
}
