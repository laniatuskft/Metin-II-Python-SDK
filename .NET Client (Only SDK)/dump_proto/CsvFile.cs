using System.Collections.Generic;
using System.Diagnostics;



public class cCsvAlias : System.IDisposable
{

	private SortedDictionary<string, size_t> m_Name2Index = new SortedDictionary<string, size_t>();
	private SortedDictionary<size_t, string> m_Index2Name = new SortedDictionary<size_t, string>();

	public cCsvAlias()
	{
	}
	public virtual void Dispose()
	{
	}

	public void AddAlias(string name, size_t index)
	{
		string converted = Globals.Lower(name);

		Debug.Assert(!m_Name2Index.ContainsKey(converted));
		Debug.Assert(!m_Index2Name.ContainsKey(index));

		m_Name2Index.insert(NAME2INDEX_MAP.value_type(converted, index));
		m_Index2Name.insert(INDEX2NAME_MAP.value_type(index, name));
	}

	public void Destroy()
	{
		m_Name2Index.Clear();
		m_Index2Name.Clear();
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const char* operator [] (size_t index) const
	public string this [size_t index]
	{
		get
		{
			INDEX2NAME_MAP.const_iterator itr = new INDEX2NAME_MAP.const_iterator(m_Index2Name.find(index));
			if (itr == m_Index2Name.end())
			{
				(0);
				(null, "cannot find suitable conversion for %d", index);
				Debug.Assert(false && "cannot find suitable conversion");
				return null;
			}
    
			return itr.second.c_str();
		}
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: size_t operator [] (const char* name) const
	public size_t this [string name]
	{
		get
		{
			NAME2INDEX_MAP.const_iterator itr = new NAME2INDEX_MAP.const_iterator(m_Name2Index.find(Globals.Lower(name)));
			if (itr == m_Name2Index.end())
			{
				(0);
				(null, "cannot find suitable conversion for %s", name);
				Debug.Assert(false && "cannot find suitable conversion");
				return 0;
			}
    
			return itr.second;
		}
	}

	private cCsvAlias(in cCsvAlias UnnamedParameter)
	{
	}
//# Laniatus Games Studio Inc. |: This 'CopyFrom' method was converted from the original copy assignment operator:
//Original Metin2 CPlus Line: const cCsvAlias& operator = (const cCsvAlias&)
	private cCsvAlias CopyFrom (in cCsvAlias UnnamedParameter)
	{
		return this;
	}
}

public class cCsvRow : List<string>, System.IDisposable
{
	public cCsvRow()
	{
	}
	public void Dispose()
	{
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int AsInt(size_t index) const
	public int AsInt(size_t index)
	{
		return atoi(at(index).c_str());
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: double AsDouble(size_t index) const
	public double AsDouble(size_t index)
	{
		return atof(at(index).c_str());
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const char* AsString(size_t index) const
	public string AsString(size_t index)
	{
		return at(index).c_str();
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int AsInt(const char* name, const cCsvAlias& alias) const
	public int AsInt(string name, in cCsvAlias alias)
	{
		return atoi(at(alias[name]).c_str());
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: double AsDouble(const char* name, const cCsvAlias& alias) const
	public double AsDouble(string name, in cCsvAlias alias)
	{
		return atof(at(alias[name]).c_str());
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const char* AsString(const char* name, const cCsvAlias& alias) const
	public string AsString(string name, in cCsvAlias alias)
	{
		return at(alias[name]).c_str();
	}


	private cCsvRow(in cCsvRow UnnamedParameter)
	{
	}
//# Laniatus Games Studio Inc. |: This 'CopyFrom' method was converted from the original copy assignment operator:
//Original Metin2 CPlus Line: const cCsvRow& operator = (const cCsvRow&)
	private cCsvRow CopyFrom (in cCsvRow UnnamedParameter)
	{
		return this;
	}
}

public class cCsvFile : System.IDisposable
{
	private List<cCsvRow> m_Rows = new List<cCsvRow>();

	public cCsvFile()
	{
	}
	public virtual void Dispose()
	{
		Destroy();
	}

	public bool Load(string fileName, in char seperator = ',', in char quote = '"')
	{
		Debug.Assert(seperator != quote);

		std::ifstream file = new std::ifstream(fileName, std::ios.@in);
		if (file == null)
		{
			return false;
		}

		Destroy();

		cCsvRow row = null;
		ParseState state = ParseState.STATE_NORMAL;
		string token = "";
		char[] buf = Arrays.PadValueTypeArrayWithDefaultInstances(2048 + 1, new char[] {0});

		while (file.good())
		{
			file.getline(buf, 2048);
			buf[sizeof(char) - 1] = 0;

			string line = Globals.Trim(buf);
			if (string.IsNullOrEmpty(line) || (state == ParseState.STATE_NORMAL && line[0] == '#'))
			{
				continue;
			}

			string text = new string(line) + "  ";
			size_t cur = 0;

			while (cur < text.Length)
			{
				if (state == ParseState.STATE_QUOTE)
				{
					if (text[cur] == quote)
					{
						if (text[cur + 1] == quote)
						{
							token += quote;
							++cur;
						}
						else
						{
							state = ParseState.STATE_NORMAL;
						}
					}
					else
					{
						token += text[cur];
					}
				}
				else if (state == ParseState.STATE_NORMAL)
				{
					if (row == null)
					{
						row = new cCsvRow();
					}

					if (text[cur] == seperator)
					{
						row.Add(token);
						token = "";
					}
					else if (text[cur] == quote)
					{
						state = ParseState.STATE_QUOTE;
					}
					else
					{
						token += text[cur];
					}
				}

				++cur;
			}

			if (state == ParseState.STATE_NORMAL)
			{
				Debug.Assert(row != null);
				row.Add(token.Substring(0, token.Length - 2));
				m_Rows.Add(row);
				token = "";
				row = null;
			}
			else
			{
				token = token.Substring(0, token.Length - 2) + "\r\n";
			}
		}

		return true;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: bool Save(const char* fileName, bool append =false, char seperator =',', char quote ='"') const
	public bool Save(string fileName, bool append = false, char seperator = ',', char quote = '"')
	{
		Debug.Assert(seperator != quote);

		std::ofstream file = new std::ofstream();
		if (append)
		{
			file.open(fileName, std::ios.@out | std::ios.app);
		}
		else
		{
			file.open(fileName, std::ios.@out | std::ios.trunc);
		}

		if (file == null)
		{
			return false;
		}

		char[] special_chars = {seperator, quote, '\r', '\n', 0};
		char[] quote_escape_string = {quote, quote, 0};

		for (size_t LaniatusDefVariables = 0; LaniatusDefVariables < m_Rows.Count; i++)
		{
			cCsvRow row = *(this[i]);
			string line = "";

			for (size_t j = 0; j < row.Count; j++)
			{
				string token = row[j];

				if (token.IndexOfAny(special_chars.ToCharArray()) == -1)
				{
					line += token;
				}
				else
				{
					line += quote;

					for (size_t k = 0; k < token.Length; k++)
					{
						if (token[k] == quote)
						{
							line += quote_escape_string;
						}
						else
						{
							line += token[k];
						}
					}

					line += quote;
				}
				if (j != row.Count - 1)
				{
					line += seperator;
				}
			}
			file << line << std::endl;
		}
		return true;
	}

	public void Destroy()
	{
		for (ROWS.iterator itr = m_Rows.GetEnumerator(); itr != m_Rows.end(); ++itr)
		{
			*itr = null;
		}

		m_Rows.Clear();
	}

	public cCsvRow this [size_t index]
	{
		get
		{
			Debug.Assert(index < m_Rows.Count);
			return new cCsvRow(m_Rows[index]);
		}
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const cCsvRow* operator [] (size_t index) const
	public cCsvRow this [size_t index]
	{
		get
		{
			Debug.Assert(index < m_Rows.Count);
			return new cCsvRow(m_Rows[index]);
		}
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: size_t GetRowCount() const
	public size_t GetRowCount()
	{
		return m_Rows.Count;
	}

	private cCsvFile(in cCsvFile UnnamedParameter)
	{
	}
//# Laniatus Games Studio Inc. |: This 'CopyFrom' method was converted from the original copy assignment operator:
//Original Metin2 CPlus Line: const cCsvFile& operator = (const cCsvFile&)
	private cCsvFile CopyFrom (in cCsvFile UnnamedParameter)
	{
		return this;
	}
}

public class cCsvTable : System.IDisposable
{
	public cCsvFile m_File = new cCsvFile();
	private cCsvAlias m_Alias = new cCsvAlias();
	private int m_CurRow;

	public cCsvTable()
	{
		this.m_CurRow = -1;
	}

	public virtual void Dispose()
	{
	}

	public bool Load(string fileName, in char seperator = ',', in char quote = '"')
	{
		Destroy();
		return m_File.Load(fileName, seperator, quote);
	}

	public void AddAlias(string name, size_t index)
	{
		m_Alias.AddAlias(name, new size_t(index));
	}
	public bool Next()
	{
		return ++m_CurRow < (int)m_File.GetRowCount() ? true : false;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: size_t ColCount() const
	public size_t ColCount()
	{
		return CurRow().Count;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int AsInt(size_t index) const
	public int AsInt(size_t index)
	{
		cCsvRow row = CurRow();
		Debug.Assert(row);
		Debug.Assert(index < row.Count);
		return row.AsInt(new size_t(index));
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: double AsDouble(size_t index) const
	public double AsDouble(size_t index)
	{
		cCsvRow row = CurRow();
		Debug.Assert(row);
		Debug.Assert(index < row.Count);
		return row.AsDouble(new size_t(index));
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const char* AsStringByIndex(size_t index) const
	public string AsStringByIndex(size_t index)
	{
		cCsvRow row = CurRow();
		Debug.Assert(row);
		Debug.Assert(index < row.Count);
		return row.AsString(new size_t(index));
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int AsInt(const char* name) const
	public int AsInt(string name)
	{
		return AsInt(m_Alias[name]);
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: double AsDouble(const char* name) const
	public double AsDouble(string name)
	{
		return AsDouble(m_Alias[name]);
	}
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const char* AsString(const char* name) const
	public string AsString(string name)
	{
		return AsStringByIndex(m_Alias[name]);
	}
	public void Destroy()
	{
		m_File.Destroy();
		m_Alias.Destroy();
		m_CurRow = -1;
	}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: const cCsvRow* const CurRow() const
	private cCsvRow CurRow()
	{
		if (m_CurRow < 0)
		{
			Debug.Assert(false && "call Next() first!");
			return null;
		}
		else if (m_CurRow >= (int)m_File.GetRowCount())
		{
			Debug.Assert(false && "no more rows!");
			return null;
		}

		return m_File[m_CurRow];
	}

	private cCsvTable(in cCsvTable UnnamedParameter)
	{
	}
//# Laniatus Games Studio Inc. |: This 'CopyFrom' method was converted from the original copy assignment operator:
//Original Metin2 CPlus Line: const cCsvTable& operator = (const cCsvTable&)
	private cCsvTable CopyFrom (in cCsvTable UnnamedParameter)
	{
		return this;
	}
}


#if ! Assert
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Assert assert
	#define Assert
//# Laniatus Games Studio Inc. | TODO TASK: #define macros defined in multiple preprocessor conditionals can only be replaced within the scope of the preprocessor conditional:
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LogToFile (void)(0);
	#define LogToFile
#endif

//# Laniatus Games Studio Inc. |: C# does not allow anonymous namespaces:
//namespace
	public enum ParseState
	{
		STATE_NORMAL = 0,
		STATE_QUOTE
	}