using System;
using System.Collections.Generic;
using System.Diagnostics;

//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE __int64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE __int64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE __INT64_TYPE__
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) __declspec(dllimport) ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) __declspec(dllexport) ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) __declspec(dllimport) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) __declspec(dllexport) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) [DllImport("granny2.dll")] ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) [DllExport("granny2.dll")] ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) __declspec(dllimport) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) __declspec(dllexport) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) __declspec(dllimport) ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) __declspec(dllexport) ret __stdcall
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret __cdecl
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) __declspec(dllimport) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) __declspec(dllexport) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE __int64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXP(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_CALLBACK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNIMPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNEXPDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_64BIT_TYPE long long
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNLINK(ret) ret
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNLINKDATA(type) type
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNLINK(ret) GRANNY_DYNEXP(ret)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNLINKDATA(type) GRANNY_DYNEXPDATA(type)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNLINK(ret) GRANNY_DYNIMP(ret)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_DYNLINKDATA(type) GRANNY_DYNIMPDATA(type)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_NAMESPACE_BEING typedef char Ignored_RequireSemi
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_NAMESPACE_END typedef char Ignored_RequireSemi
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_NAMESPACE_BEGIN namespace granny { typedef char Ignored_RequireSemi
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_NAMESPACE_END } typedef char Ignored_RequireSemi
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY granny::
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_FORWARD_DECL_STRUCT(x) typedef struct granny_ ## x granny_ ## x
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_FORWARD_DECL_OPAQUE_STRUCT(x) GRANNY_NAMESPACE_BEGIN; struct x; GRANNY_NAMESPACE_END; typedef struct GRANNY x granny_ ## x
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_FORWARD_DECL_OPAQUE_STRUCT(x) GRANNY_FORWARD_DECL_STRUCT(x)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_STRUCT(x) public x
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GRANNY_STRUCT(x) x
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RR_STRING_JOIN(arg1, arg2) RR_STRING_JOIN_DELAY(arg1, arg2)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RR_STRING_JOIN_DELAY(arg1, arg2) RR_STRING_JOIN_IMMEDIATE(arg1, arg2)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RR_STRING_JOIN_IMMEDIATE(arg1, arg2) arg1 ## arg2
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RR_NUMBERNAME(name) RR_STRING_JOIN(name,__COUNTER__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RR_NUMBERNAME(name) RR_STRING_JOIN(name,__LINE__)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyTypeSizeCheck(expr) typedef int RR_NUMBERNAME(GrannyTypeSizeCheck_) [(expr) ? 1 : -1]
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyCurrentGRNStandardTag (0x80000000 + 57)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyCloseFileReader(Reader) { if(Reader) {(*((Reader)->CloseFileReaderCallback))(Reader);} } typedef int __granny_require_semicolon
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyReadAtMost(Reader, Pos, Count, Buffer) (*((Reader)->ReadAtMostCallback))(Reader, Pos, Count, Buffer)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyReadExactly(Reader, Pos, Count, Buffer) ((*((Reader)->ReadAtMostCallback))(Reader, Pos, Count, Buffer) == Count)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyGetReaderSize(Reader, SizeVar) ((*((Reader)->GetReaderSizeCallback))(Reader, SizeVar))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyCloseFileWriter(Writer) { if (Writer) {(*(Writer)->DeleteFileWriterCallback)(Writer);} } typedef int __granny_require_semicolon
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyGetWriterPosition(Writer) (*((Writer)->SeekWriterCallback))(Writer, 0, 2)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannySeekWriterFromStart(Writer, OffsetInUInt8s) (*((Writer)->SeekWriterCallback))(Writer, OffsetInUInt8s, 0)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannySeekWriterFromEnd(Writer, OffsetInUInt8s) (*((Writer)->SeekWriterCallback))(Writer, OffsetInUInt8s, 1)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannySeekWriterFromCurrentPosition(Writer, OffsetInUInt8s) (*((Writer)->SeekWriterCallback))(Writer, OffsetInUInt8s, 2)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyWriteBytes(Writer, UInt8Count, WritePointer) (*((Writer)->WriteCallback))(Writer, UInt8Count, WritePointer)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyBeginWriterCRC(Writer) (*((Writer)->BeginCRCCallback))(Writer)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyEndWriterCRC(Writer) (*((Writer)->EndCRCCallback))(Writer)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyWriterIsCRCing(Writer) (((Writer)->CRCing))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumSystemFileNameSize (1 << 9)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumTempFileNameSize (1 << 9)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumMessageBufferSize (1 << 10)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumLogFileNameSize (1 << 9)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumNumberToStringBuffer (1 << 8)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumIKLinkCount (1 << 5)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumMIPLevelCount (1 << 5)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumVertexNameLength (1 << 6)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumUserData (1 << 2)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumBoneNameLength (1 << 9)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumChannelCount (1 << 8)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumChannelWidth (1 << 2)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumPolygonSides (1 << 7)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyBlockFileFixupCount (1 << 8)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMinimumAllocationsPerFixedBlock (1 << 6)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyFileCopyBufferSize (1 << 16)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyCRCCheckBufferSize (1 << 16)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyCurrentMODStandardTag ((GrannyCurrentGRNStandardTag) | ((MOD_VERSION_TAG) << 15))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannySPUTransformTrackNoCurve (0xffffffff)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyProductReleaseName release
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyProductTrademarks ProductName " is a registered trademark of " ProductCompanyName
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyVersionsMatch GrannyVersionsMatch_(GrannyProductMajorVersion, GrannyProductMinorVersion, GrannyProductBuildNumber, GrannyProductCustomization)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define GrannyMaximumWeightCount (1 << 8)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_DELETE(p) { if (p) { delete (p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_DELETE_ARRAY(p) { if (p) { delete[] (p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_RELEASE(p) { if (p) { (p)->Release(); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_FREE_GLOBAL(p) { if (p) { ::GlobalFree(p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAFE_FREE_LIBRARY(p) { if (p) { ::FreeLibrary(p); (p) = NULL; } }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define AssertLog(str) TraceError(str); assert(!str)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAKEFOURCC(ch0, ch1, ch2, ch3) ((DWORD)(BYTE) (ch0 ) | ((DWORD)(BYTE) (ch1) << 8) | ((DWORD)(BYTE) (ch2) << 16) | ((DWORD)(BYTE) (ch3) << 24))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define IS_SET(flag,bit) ((flag) & (bit))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SET_BIT(var,bit) ((var) |= (bit))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define REMOVE_BIT(var,bit) ((var) &= ~(bit))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define TOGGLE_BIT(var,bit) ((var) = (var) ^ (bit))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define CHECK_RETURN(flag, string) if (flag) { LogBox(string); return; }
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOBEGIN __emit__ (0xEB,0x03,0xD6,0xD7,0x01)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOEND __emit__ (0xEB,0x03,0xD6,0xD7,0x00)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOBEGIN __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x01
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define NANOEND __asm _emit 0xEB __asm _emit 0x03 __asm _emit 0xD6 __asm _emit 0xD7 __asm _emit 0x00
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_WINTRUST (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_WEBSERVICES (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_EVENTLOGSERVICE (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_VHD (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_PERFCOUNTER (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_SECURESTARTUP (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_REMOTEFS (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_BOOTABLESKU (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_CMD (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_CMDTOOLS (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_DISM (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_CORESETUP (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_APPRUNTIME (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_ESENT (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PKG_WINMGMT (WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_FAMILY_APP WINAPI_FAMILY_PC_APP
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_FAMILY WINAPI_FAMILY_DESKTOP_APP
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_DESKTOP (WINAPI_FAMILY == WINAPI_FAMILY_DESKTOP_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_APP (WINAPI_FAMILY == WINAPI_FAMILY_DESKTOP_APP || WINAPI_FAMILY == WINAPI_FAMILY_PC_APP || WINAPI_FAMILY == WINAPI_FAMILY_PHONE_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PC_APP (WINAPI_FAMILY == WINAPI_FAMILY_DESKTOP_APP || WINAPI_FAMILY == WINAPI_FAMILY_PC_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PHONE_APP (WINAPI_FAMILY == WINAPI_FAMILY_PHONE_APP)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_SYSTEM (WINAPI_FAMILY == WINAPI_FAMILY_SYSTEM || WINAPI_FAMILY == WINAPI_FAMILY_SERVER)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_PARTITION_PHONE WINAPI_PARTITION_PHONE_APP
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define WINAPI_FAMILY_PARTITION(Partitions) (Partitions)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _WINAPI_DEPRECATED_DECLARATION __declspec(deprecated("This API cannot be used in the context of the caller's application type."))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define APP_DEPRECATED_HRESULT HRESULT _WINAPI_DEPRECATED_DECLARATION
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_64 __ptr64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_32 __ptr32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_64 __ptr64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_64 __ptr64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define FIRMWARE_PTR POINTER_32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_SIGNED __sptr
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define POINTER_UNSIGNED __uptr
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SPOINTER_32 POINTER_SIGNED POINTER_32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UPOINTER_32 POINTER_UNSIGNED POINTER_32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _W64 __w64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __int3264 __int64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define __int3264 __int32
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ADDRESS_TAG_BIT 0x40000000000UI64
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToPtr64( p ) ((void * POINTER_64) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Ptr64ToPtr( p ) ((void *) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToHandle64( h ) (PtrToPtr64( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Handle64ToHandle( h ) (Ptr64ToPtr( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToHandle32( h ) (PtrToPtr32( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToULong( h ) ((ULONG)(ULONG_PTR)(h) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToLong( h ) ((LONG)(LONG_PTR) (h) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ULongToHandle( ul ) ((HANDLE)(ULONG_PTR) (ul) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LongToHandle( h ) ((HANDLE)(LONG_PTR) (h) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToUlong( p ) ((ULONG)(ULONG_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToLong( p ) ((LONG)(LONG_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToUint( p ) ((UINT)(UINT_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToInt( p ) ((INT)(INT_PTR) (p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToUshort( p ) ((unsigned short)(ULONG_PTR)(p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToShort( p ) ((short)(LONG_PTR)(p) )
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define IntToPtr( LaniatusDefVariables ) ((VOID *)(INT_PTR)((int)i))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UIntToPtr( ui ) ((VOID *)(UINT_PTR)((unsigned int)ui))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define LongToPtr( l ) ((VOID *)(LONG_PTR)((long)l))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define ULongToPtr( ul ) ((VOID *)(ULONG_PTR)((unsigned long)ul))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Ptr32ToPtr( p ) ((void *) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define Handle32ToHandle( h ) (Ptr32ToPtr( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define PtrToPtr32( p ) ((void * POINTER_32) p)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToHandle32( h ) (PtrToPtr32( h ))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define HandleToUlong(h) HandleToULong(h)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UlongToHandle(ul) ULongToHandle(ul)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UlongToPtr(ul) ULongToPtr(ul)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define UintToPtr(ui) UIntToPtr(ui)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT_PTR (~((UINT_PTR)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT_PTR ((INT_PTR)(MAXUINT_PTR >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT_PTR (~MAXINT_PTR)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONG_PTR (~((ULONG_PTR)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXLONG_PTR ((LONG_PTR)(MAXULONG_PTR >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONG_PTR (~MAXLONG_PTR)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUHALF_PTR ((UHALF_PTR)~0)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXHALF_PTR ((HALF_PTR)(MAXUHALF_PTR >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINHALF_PTR (~MAXHALF_PTR)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT8 ((UINT8)~((UINT8)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT8 ((INT8)(MAXUINT8 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT8 ((INT8)~MAXINT8)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT16 ((UINT16)~((UINT16)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT16 ((INT16)(MAXUINT16 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT16 ((INT16)~MAXINT16)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT32 ((UINT32)~((UINT32)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT32 ((INT32)(MAXUINT32 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT32 ((INT32)~MAXINT32)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT64 ((UINT64)~((UINT64)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT64 ((INT64)(MAXUINT64 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT64 ((INT64)~MAXINT64)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONG32 ((ULONG32)~((ULONG32)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXLONG32 ((LONG32)(MAXULONG32 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONG32 ((LONG32)~MAXLONG32)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONG64 ((ULONG64)~((ULONG64)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXLONG64 ((LONG64)(MAXULONG64 >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONG64 ((LONG64)~MAXLONG64)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXULONGLONG ((ULONGLONG)~((ULONGLONG)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINLONGLONG ((LONGLONG)~MAXLONGLONG)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXSIZE_T ((SIZE_T)~((SIZE_T)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXSSIZE_T ((SSIZE_T)(MAXSIZE_T >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MINSSIZE_T ((SSIZE_T)~MAXSSIZE_T)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXUINT ((UINT)~((UINT)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXINT ((INT)(MAXUINT >> 1))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MININT ((INT)~MAXINT)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXDWORD32 ((DWORD32)~((DWORD32)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define MAXDWORD64 ((DWORD64)~((DWORD64)0))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define midl_user_allocate MIDL_user_allocate
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define midl_user_free MIDL_user_free
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DECLSPEC_IMPORT __declspec(dllimport)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RPCRTAPI DECLSPEC_IMPORT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RPCNSAPI DECLSPEC_IMPORT
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define RPCXCWORD (sizeof(jmp_buf)/sizeof(int))
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define DECLSPEC_NORETURN __declspec(noreturn)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_SAL2(_A) SAL_2_Clean_Violation_using ## _A
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_SAL2(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_CHECK(_A) _SAL_VERSION_SAL2(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_VERSION_CHECK(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAL_VERSION_CHECK(_A) _SAL_VERSION_CHECK(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define SAL_VERSION_SAL2(_A) _SAL_VERSION_SAL2(_A)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.1") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _GrouP_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_1_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.1") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL1_2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "1.2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL2_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _SAL_L_Source_(Name, args, annotes) _SA_annotes3(SAL_name, #Name, "", "2") _Group_(annotes _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_(target, annos) _At_impl_(target, annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _At_buffer_(target, iter, bound, annos) _At_buffer_impl_(target, iter, bound, annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _When_(expr, annos) _When_impl_(expr, annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Group_(annos) _Group_impl_(annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _GrouP_(annos) _GrouP_impl_(annos _SAL_nop_impl_)
//# Laniatus Games Studio Inc. |: The following #define macro was replaced in-line:
//Original Metin2 CPlus Line: #define _Success_(expr) _SAL2_Source_(_Success_, (expr), _Success_impl_(expr))
//# Laniatus Games Studio Inc. | TODO TASK: Conditional typedefs are not handled by # Laniatus Games Studio Inc. |:
//#define _Return_type_success_(expr) _SAL2_Source_(_Return_type_success_, (expr), _Success_impl_(expr))
public class CGraphicThingInstance : CGraphicObjectInstance
{
		public class SModelThingSet
		{
			public void Clear()
			{
				Globals.stl_wipe(m_pLODThingRefVector);
			}

			public List<CGraphicThing.TRef > m_pLODThingRefVector = new List<CGraphicThing.TRef >();
		}

		public const int ID = THING_OBJECT;
//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: int GetType() const
		public int GetType()
		{
			return ID;
		}

		public CGraphicThingInstance()
		{
			Initialize();
		}

		public virtual void Dispose()
		{
		}

		public void DeformNoSkin()
		{
			m_bUpdated = true;

			for (List<CGrannyLODController>.size_type LaniatusDefVariables = 0; LaniatusDefVariables != m_LODControllerVector.size(); i++)
			{
				CGrannyLODController pkLOD = m_LODControllerVector[i];
				if (pkLOD != null && pkLOD.isModelInstance())
				{
					if (i == 5)
					{
						RecalcAccePositionMatrixFromBoneMatrix();
						pkLOD.DeformNoSkin(m_matAbsoluteTrans);
					}
					else
					{
						pkLOD.DeformNoSkin(m_worldMatrix);
					}
				}
			}
		}

		public void UpdateLODLevel()
		{
			CCamera pcurCamera = CCameraManager.Instance().GetCurrentCamera();
			if (pcurCamera == null)
			{
				TraceError("CGraphicThingInstance::UpdateLODLevel - GetCurrentCamera() == NULL");
				return;
			}

			D3DXVECTOR3 c_rv3TargetPosition = pcurCamera.GetTarget();
			D3DXVECTOR3 c_rv3CameraPosition = pcurCamera.GetEye();
			D3DXVECTOR3 c_v3Position = GetPosition();

			CGrannyLODController.FUpdateLODLevel update = new CGrannyLODController.FUpdateLODLevel();
			update.fDistanceFromCenter = sqrtf((c_rv3TargetPosition.x - c_v3Position.x) * (c_rv3TargetPosition.x - c_v3Position.x) + (c_rv3TargetPosition.y - c_v3Position.y) * (c_rv3TargetPosition.y - c_v3Position.y));
			update.fDistanceFromCamera = sqrtf((c_rv3CameraPosition.x - c_v3Position.x) * (c_rv3CameraPosition.x - c_v3Position.x) + (c_rv3CameraPosition.y - c_v3Position.y) * (c_rv3CameraPosition.y - c_v3Position.y) + (c_rv3CameraPosition.z - c_v3Position.z) * (c_rv3CameraPosition.z - c_v3Position.z));

			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), update);
		}

		public void UpdateTime()
		{
			m_fSecondElapsed = CTimer.Instance().GetElapsedSecond();

			if (m_fDelay > m_fSecondElapsed)
			{
				m_fDelay -= m_fSecondElapsed;
				m_fSecondElapsed = 0.0f;
			}
			else
			{
				m_fSecondElapsed -= m_fDelay;
				m_fDelay = 0.0f;
			}

			m_fLastLocalTime = m_fLocalTime;
			m_fLocalTime += m_fSecondElapsed;
			m_fAverageSecondElapsed = m_fAverageSecondElapsed + (m_fSecondElapsed - m_fAverageSecondElapsed) / 4.0f;

			CGrannyLODController.FUpdateTime update = new CGrannyLODController.FUpdateTime();
			update.fElapsedTime = m_fSecondElapsed;
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), update);
		}

		public void DeformAll()
		{
			m_bUpdated = true;

			for (List<CGrannyLODController>.size_type LaniatusDefVariables = 0; LaniatusDefVariables != m_LODControllerVector.size(); i++)
			{
				CGrannyLODController pkLOD = m_LODControllerVector[i];
				if (pkLOD != null && pkLOD.isModelInstance())
				{
					if (i == 5)
					{
						RecalcAccePositionMatrixFromBoneMatrix();
						pkLOD.DeformAll(m_matAbsoluteTrans);
					}
					else
					{
						pkLOD.DeformAll(m_worldMatrix);
					}
				}
			}
		}

		public bool LessRenderOrder(CGraphicThingInstance pkThingInst)
		{
			return (GetBaseThingPtr() < pkThingInst.GetBaseThingPtr());
		}

		public bool Picking(in D3DXVECTOR3 v, in D3DXVECTOR3 dir, ref float out_x, ref float out_y)
		{
			if (!m_pHeightAttributeInstance)
			{
				return false;
			}
			return m_pHeightAttributeInstance.Picking(v,dir,out_x,out_y);
		}

		public void OnInitialize()
		{
			m_bUpdated = false;
			m_fLastLocalTime = 0.0f;
			m_fLocalTime = 0.0f;
			m_fDelay = 0.0;
			m_fSecondElapsed = 0.0f;
			m_fAverageSecondElapsed = 0.03f;
			m_fRadius = -1.0f;
			m_v3Center = D3DXVECTOR3(0.0f, 0.0f, 0.0f);

			ResetLocalTime();
		}

		public bool CreateDeviceObjects()
		{
			CGrannyLODController.FCreateDeviceObjects createDeviceObjects = new CGrannyLODController.FCreateDeviceObjects();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), createDeviceObjects);
			return true;
		}

		public void DestroyDeviceObjects()
		{
			CGrannyLODController.FDestroyDeviceObjects destroyDeviceObjects = new CGrannyLODController.FDestroyDeviceObjects();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), destroyDeviceObjects);
		}

		public void ReserveModelInstance(int iCount)
		{
			Globals.stl_wipe(m_LODControllerVector);

			for (int LaniatusDefVariables = 0; LaniatusDefVariables < iCount; ++i)
			{
				CGrannyLODController pInstance = new CGrannyLODController();
				m_LODControllerVector.push_back(pInstance);
			}
		}

		public void ReserveModelThing(int iCount)
		{
			m_modelThingSetVector.resize(iCount);
		}

		public bool CheckModelInstanceIndex(int iModelInstance)
		{
			if (iModelInstance < 0)
			{
				return false;
			}

			int max = m_LODControllerVector.size();

			if (iModelInstance >= max)
			{
				return false;
			}

			return true;
		}

		public bool CheckModelThingIndex(int iModelThing)
		{
			if (iModelThing < 0)
			{
				return false;
			}

			int max = m_modelThingSetVector.size();

			if (iModelThing >= max)
			{
				return false;
			}

			return true;
		}

		public bool CheckMotionThingIndex(uint dwMotionKey)
		{
			SortedDictionary<uint, CGraphicThing.TRef >.Enumerator itor = m_roMotionThingMap.find(dwMotionKey);

			if (m_roMotionThingMap.end() == itor)
			{
				return false;
			}

			return true;
		}

		public bool GetMotionThingPointer(uint dwKey, CGraphicThing[] ppMotion)
		{
			if (!CheckMotionThingIndex(dwKey))
			{
				return false;
			}

			ppMotion[0] = m_roMotionThingMap[dwKey].GetPointer();
			return true;
		}

		public bool IsMotionThing()
		{
			return !m_roMotionThingMap.empty();
		}

		public void RegisterModelThing(int iModelThing, CGraphicThing pModelThing)
		{
			if (!CheckModelThingIndex(iModelThing))
			{
				TraceError("CGraphicThingInstance::RegisterModelThing(iModelThing=%d, pModelThing=%s)\n", iModelThing, pModelThing.GetFileName());
				return;
			}

			m_modelThingSetVector[iModelThing].Clear();

			if (pModelThing != null)
			{
				RegisterLODThing(iModelThing, pModelThing);
			}
		}

		public void RegisterLODThing(int iModelThing, CGraphicThing pModelThing)
		{
			Debug.Assert(CheckModelThingIndex(iModelThing));
			CGraphicThing.TRef pModelRef = new CGraphicThing.TRef();
			pModelRef.SetPointer(pModelThing);
			m_modelThingSetVector[iModelThing].m_pLODThingRefVector.push_back(pModelRef);
		}

		public void RegisterMotionThing(uint dwMotionKey, CGraphicThing pMotionThing)
		{
			CGraphicThing.TRef pMotionRef = new CGraphicThing.TRef();
			pMotionRef.SetPointer(pMotionThing);
			m_roMotionThingMap.insert(SortedDictionary<uint, CGraphicThing.TRef>.value_type(dwMotionKey, pMotionRef));
		}

		public bool SetModelInstance(int iDstModelInstance, int iSrcModelThing, int iSrcModel, int iSkelInstance = DONTUSEVALUE)
		{
			if (!CheckModelInstanceIndex(iDstModelInstance))
			{
				TraceError("CGraphicThingInstance::SetModelInstance(iDstModelInstance=%d, pModelThing=%d, iSrcModel=%d)\n", iDstModelInstance, iSrcModelThing, iSrcModel);
				return false;
			}
			if (!CheckModelThingIndex(iSrcModelThing))
			{
				TraceError("CGraphicThingInstance::SetModelInstance(iDstModelInstance=%d, pModelThing=%d, iSrcModel=%d)\n", iDstModelInstance, iSrcModelThing, iSrcModel);
				return false;
			}

			CGrannyLODController pController = m_LODControllerVector[iDstModelInstance];
			if (pController == null)
			{
				return false;
			}

			CGrannyLODController pSkelController = null;
			if (iSkelInstance != DONTUSEVALUE)
			{
				if (!CheckModelInstanceIndex(iSkelInstance))
				{
					TraceError("CGraphicThingInstance::SetModelInstanceByOtherSkeletonInstance(iSkelInstance=%d, iDstModelInstance=%d, pModelThing=%d, iSrcModel=%d)\n", iSkelInstance, iDstModelInstance, iSrcModelThing, iSrcModel);
					return false;
				}
				pSkelController = m_LODControllerVector[iSkelInstance];
				if (pSkelController == null)
				{
					return false;
				}
			}

			TModelThingSet rModelThingSet = m_modelThingSetVector[iSrcModelThing];

			pController.Clear();


			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < rModelThingSet.m_pLODThingRefVector.size(); ++i)
			{
				if (rModelThingSet.m_pLODThingRefVector[i].IsNull())
				{
					return false;
				}

				pController.AddModel(rModelThingSet.m_pLODThingRefVector[i].GetPointer(), iSrcModel, pSkelController);
			}
			return true;
		}

		public void SetEndStopMotion()
		{
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), CGrannyLODController.FEndStopMotionPointer());
		}

		public void SetMotionAtEnd()
		{
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), std::mem_fn(CGrannyLODController.SetMotionAtEnd));
		}

		public void AttachModelInstance(int iDstModelInstance, string c_szBoneName, int iSrcModelInstance)
		{
			if (!CheckModelInstanceIndex(iSrcModelInstance))
			{
				TraceError("CGraphicThingInstance::AttachModelInstance(iDstModelInstance=%d, c_szBoneName=%s, iSrcModelInstance=%d)", iDstModelInstance, c_szBoneName, iSrcModelInstance);
				return;
			}
			if (!CheckModelInstanceIndex(iDstModelInstance))
			{
				TraceError("CGraphicThingInstance::AttachModelInstance(iDstModelInstance=%d, c_szBoneName=%s, iSrcModelInstance=%d)", iDstModelInstance, c_szBoneName, iSrcModelInstance);
				return;
			}

			CGrannyLODController pSrcLODController = m_LODControllerVector[iSrcModelInstance];
			CGrannyLODController pDstLODController = m_LODControllerVector[iDstModelInstance];
			pDstLODController.AttachModelInstance(pSrcLODController, c_szBoneName);
		}

		public void AttachModelInstance(int iDstModelInstance, string c_szBoneName, CGraphicThingInstance rSrcInstance, int iSrcModelInstance)
		{
			if (!CheckModelInstanceIndex(iDstModelInstance))
			{
				TraceError("CGraphicThingInstance::AttachModelInstance(iDstModelInstance=%d, c_szBoneName=%s, iSrcModelInstance=%d)", iDstModelInstance, c_szBoneName, iSrcModelInstance);
				return;
			}
			if (!rSrcInstance.CheckModelInstanceIndex(iSrcModelInstance))
			{
				TraceError("CGraphicThingInstance::AttachModelInstance(iDstModelInstance=%d, c_szBoneName=%s, iSrcModelInstance=%d)", iDstModelInstance, c_szBoneName, iSrcModelInstance);
				return;
			}

			CGrannyLODController pDstLODController = m_LODControllerVector[iDstModelInstance];
			CGrannyLODController pSrcLODController = rSrcInstance.m_LODControllerVector[iSrcModelInstance];
			pDstLODController.AttachModelInstance(pSrcLODController, c_szBoneName);
		}

		public void DetachModelInstance(int iDstModelInstance, CGraphicThingInstance rSrcInstance, int iSrcModelInstance)
		{
			if (!CheckModelInstanceIndex(iDstModelInstance))
			{
				TraceError("CGraphicThingInstance::AttachModelInstance(iDstModelInstance=%d, iSrcModelInstance=%d)", iDstModelInstance, iSrcModelInstance);
				return;
			}
			if (!rSrcInstance.CheckModelInstanceIndex(iSrcModelInstance))
			{
				TraceError("CGraphicThingInstance::AttachModelInstance(iDstModelInstance=%d, iSrcModelInstance=%d)", iDstModelInstance, iSrcModelInstance);
				return;
			}

			CGrannyLODController pDstLODController = m_LODControllerVector[iDstModelInstance];
			CGrannyLODController pSrcLODController = rSrcInstance.m_LODControllerVector[iSrcModelInstance];
			pDstLODController.DetachModelInstance(pSrcLODController);
		}

		public bool FindBoneIndex(int iModelInstance, string c_szBoneName, ref int iRetBone)
		{
			Debug.Assert(CheckModelInstanceIndex(iModelInstance));

			CGrannyModelInstance pModelInstance = m_LODControllerVector[iModelInstance].GetModelInstance();

			if (pModelInstance == null)
			{
				return false;
			}

			return pModelInstance.GetBoneIndexByName(c_szBoneName, iRetBone);
		}

		public bool GetBonePosition(int iModelIndex, int iBoneIndex, ref float pfx, ref float pfy, ref float pfz)
		{
			Debug.Assert(CheckModelInstanceIndex(iModelIndex));

			CGrannyModelInstance pModelInstance = m_LODControllerVector[iModelIndex].GetModelInstance();

			if (pModelInstance == null)
			{
				return false;
			}

			float[] pfMatrix = pModelInstance.GetBoneMatrixPointer(iBoneIndex);

			pfx = pfMatrix[12];
			pfy = pfMatrix[13];
			pfz = pfMatrix[14];
			return true;
		}

		public void ResetLocalTime()
		{
			m_fLastLocalTime = 0.0f;
			m_fLocalTime = 0.0f;

			CGrannyLODController.FResetLocalTime resetLocalTime = new CGrannyLODController.FResetLocalTime();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), resetLocalTime);
		}

		public void InsertDelay(float fDelay)
		{
			m_fDelay = fDelay;
		}

		public void SetMaterialImagePointer(uint ePart, string c_szImageName, CGraphicImage pImage)
		{
			if (ePart >= m_LODControllerVector.size())
			{
				TraceError("CGraphicThingInstance::SetMaterialImagePointer(ePart(%d)<uPartCount(%d), c_szImageName=%s, pImage=%s) - ePart OUT OF RANGE", ePart, m_LODControllerVector.size(), c_szImageName, pImage.GetFileName());

				return;
			}

			if (!m_LODControllerVector[ePart])
			{
				TraceError("CGraphicThingInstance::SetMaterialImagePointer(ePart(%d), c_szImageName=%s, pImage=%s) - ePart Data is NULL", ePart, m_LODControllerVector.size(), c_szImageName, pImage.GetFileName());

				return;
			}

			m_LODControllerVector[ePart].SetMaterialImagePointer(c_szImageName, pImage);
		}

		public void SetMaterialData(uint ePart, string c_szImageName, SMaterialData kMaterialData)
		{
			if (ePart >= m_LODControllerVector.size())
			{
				TraceError("CGraphicThingInstance::SetMaterialData(ePart(%d)<uPartCount(%d)) - ePart OUT OF RANGE", ePart, m_LODControllerVector.size());

				return;
			}

			if (!m_LODControllerVector[ePart])
			{
				TraceError("CGraphicThingInstance::SetMaterialData(ePart(%d)) - ePart Data is NULL", ePart, m_LODControllerVector.size());

				return;
			}

			m_LODControllerVector[ePart].SetMaterialData(c_szImageName, kMaterialData);
		}

		public void SetSpecularInfo(uint ePart, string c_szMtrlName, bool bEnable, float fPower)
		{
			if (ePart >= m_LODControllerVector.size())
			{
				TraceError("CGraphicThingInstance::SetSpecularInfo(ePart(%d)<uPartCount(%d)) - ePart OUT OF RANGE", ePart, m_LODControllerVector.size());

				return;
			}

			if (!m_LODControllerVector[ePart])
			{
				TraceError("CGraphicThingInstance::SetSpecularInfo(ePart(%d)) - ePart Data is NULL", ePart, m_LODControllerVector.size());

				return;
			}

			m_LODControllerVector[ePart].SetSpecularInfo(c_szMtrlName, bEnable, fPower);
		}

		public void __SetLocalTime(float fLocalTime)
		{
			m_fLastLocalTime = m_fLocalTime;
			m_fLocalTime = fLocalTime;

			CGrannyLODController.FSetLocalTime SetLocalTime = new CGrannyLODController.FSetLocalTime();
			SetLocalTime.fLocalTime = fLocalTime;
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), SetLocalTime);
		}

		public float GetLastLocalTime()
		{
			return m_fLastLocalTime;
		}

		public float GetLocalTime()
		{
			return m_fLocalTime;
		}

		public float GetSecondElapsed()
		{
			return m_fSecondElapsed;
		}

		public float GetAverageSecondElapsed()
		{
			return m_fAverageSecondElapsed;
		}

		public byte GetLODLevel(uint dwModelInstance)
		{
			Debug.Assert(dwModelInstance < m_LODControllerVector.size());
			return (m_LODControllerVector[dwModelInstance].GetLODLevel());
		}

		public float GetHeight()
		{
			if (m_LODControllerVector.empty())
			{
				return 0.0f;
			}

			CGrannyModelInstance pModelInstance = m_LODControllerVector[0].GetModelInstance();
			if (pModelInstance == null)
			{
				return 0.0f;
			}

			D3DXVECTOR3 vtMin = new D3DXVECTOR3();
			D3DXVECTOR3 vtMax = new D3DXVECTOR3();
			pModelInstance.GetBoundBox(vtMin, vtMax);

			return Math.Abs(vtMin.z - vtMax.z);
		}

		public void RenderWithOneTexture()
		{
			if (!m_bUpdated)
			{
				return;
			}

			CGrannyLODController.FRenderWithOneTexture render = new CGrannyLODController.FRenderWithOneTexture();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), render);
		}

		public void RenderWithTwoTexture()
		{
			if (!m_bUpdated)
			{
				return;
			}

			CGrannyLODController.FRenderWithTwoTexture render = new CGrannyLODController.FRenderWithTwoTexture();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), render);
		}

		public void BlendRenderWithOneTexture()
		{
			if (!m_bUpdated)
			{
				return;
			}

			CGrannyLODController.FBlendRenderWithOneTexture blendRender = new CGrannyLODController.FBlendRenderWithOneTexture();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), blendRender);
		}

		public void BlendRenderWithTwoTexture()
		{
			if (!m_bUpdated)
			{
				return;
			}

			CGrannyLODController.FRenderWithTwoTexture blendRender = new CGrannyLODController.FRenderWithTwoTexture();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), blendRender);
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: uint GetLODControllerCount() const
		public uint GetLODControllerCount()
		{
			return (uint)m_LODControllerVector.size();
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: CGrannyLODController * GetLODControllerPointer(uint dwModelIndex) const
		public CGrannyLODController GetLODControllerPointer(uint dwModelIndex)
		{
			Debug.Assert(dwModelIndex < m_LODControllerVector.size());
			return m_LODControllerVector[dwModelIndex];
		}

		public CGrannyLODController GetLODControllerPointer(uint dwModelIndex)
		{
			Debug.Assert(dwModelIndex < m_LODControllerVector.size());
			return m_LODControllerVector[dwModelIndex];
		}

		public void ReloadTexture()
		{
			CGrannyLODController.FReloadTexture ReloadTexture = new CGrannyLODController.FReloadTexture();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), ReloadTexture);
		}

//# Laniatus Games Studio Inc. | WARN: 'const' methods are not available in C#:
//Original Metin2 CPlus Line: uint GetActorType() const
		public uint GetActorType()
		{
			return m_eActorType;
		}

		public void SetActorType(uint eType)
		{
			m_eActorType = eType;
		}

		protected uint m_eActorType;

		public CGraphicThing GetBaseThingPtr()
		{
			if (m_modelThingSetVector.empty())
			{
				return null;
			}

			TModelThingSet rkModelThingSet = m_modelThingSetVector[0];
			if (rkModelThingSet.m_pLODThingRefVector.empty())
			{
				return null;
			}

			CGraphicThing.TRef proThing = rkModelThingSet.m_pLODThingRefVector[0];
			if (proThing == null)
			{
				return null;
			}

			CGraphicThing.TRef roThing = proThing;
			return roThing.GetPointer();
		}

		public bool SetMotion(uint dwMotionKey, float blendTime = 0.0f, int loopCount = 0, float speedRatio = 1.0f)
		{
			if (!CheckMotionThingIndex(dwMotionKey))
			{
				return false;
			}

			SortedDictionary<uint, CGraphicThing.TRef >.Enumerator itor = m_roMotionThingMap.find(dwMotionKey);
//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
			CGraphicThing.TRef proMotionThing = itor.second;
			CGraphicThing pMotionThing = proMotionThing.GetPointer();

			if (pMotionThing == null)
			{
				return false;
			}

			if (!pMotionThing.CheckMotionIndex(0))
			{
				return false;
			}

			CGrannyLODController.FSetMotionPointer SetMotionPointer = new CGrannyLODController.FSetMotionPointer();
			SetMotionPointer.m_pMotion = pMotionThing.GetMotionPointer(0);
			SetMotionPointer.m_blendTime = blendTime;
			SetMotionPointer.m_loopCount = loopCount;
			SetMotionPointer.m_speedRatio = speedRatio;

			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), SetMotionPointer);
			return true;
		}

		public bool ChangeMotion(uint dwMotionKey, int loopCount = 0, float speedRatio = 1.0f)
		{
			if (!CheckMotionThingIndex(dwMotionKey))
			{
				return false;
			}

			SortedDictionary<uint, CGraphicThing.TRef >.Enumerator itor = m_roMotionThingMap.find(dwMotionKey);
//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
			CGraphicThing.TRef proMotionThing = itor.second;
			CGraphicThing pMotionThing = proMotionThing.GetPointer();

			if (pMotionThing == null)
			{
				return false;
			}

			if (!pMotionThing.CheckMotionIndex(0))
			{
				return false;
			}

			CGrannyLODController.FChangeMotionPointer ChangeMotionPointer = new CGrannyLODController.FChangeMotionPointer();
			ChangeMotionPointer.m_pMotion = pMotionThing.GetMotionPointer(0);
			ChangeMotionPointer.m_loopCount = loopCount;
			ChangeMotionPointer.m_speedRatio = speedRatio;

			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), ChangeMotionPointer);
			return true;
		}

		public bool Intersect(ref float pu, ref float pv, ref float pt)
		{
			if (!CGraphicObjectInstance.isShow())
			{
				return false;
			}
			if (!m_bUpdated)
			{
				return false;
			}

			if (m_LODControllerVector.empty())
			{
				return false;
			}

			return m_LODControllerVector[0].Intersect(GetTransform(), pu, pv, pt);
		}

		public void GetBoundBox(D3DXVECTOR3 vtMin, D3DXVECTOR3 vtMax)
		{
			vtMin.x = vtMin.y = vtMin.z = 100000.0f;
			vtMax.x = vtMax.y = vtMax.z = -100000.0f;
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), CGrannyLODController.FBoundBox(vtMin, vtMax));
		}

		public bool GetBoundBox(uint dwModelInstanceIndex, D3DXVECTOR3 vtMin, D3DXVECTOR3 vtMax)
		{
			if (!CheckModelInstanceIndex(dwModelInstanceIndex))
			{
				return false;
			}

			vtMin.x = vtMin.y = vtMin.z = 100000.0f;
			vtMax.x = vtMax.y = vtMax.z = -100000.0f;

			CGrannyLODController pController = m_LODControllerVector[dwModelInstanceIndex];
			if (!pController.isModelInstance())
			{
				return false;
			}

			CGrannyModelInstance pModelInstance = pController.GetModelInstance();
			pModelInstance.GetBoundBox(vtMin, vtMax);
			return true;
		}

		public bool GetBoneMatrix(uint dwModelInstanceIndex, uint dwBoneIndex, D3DXMATRIX[] ppMatrix)
		{
			if (!CheckModelInstanceIndex(dwModelInstanceIndex))
			{
				return false;
			}

			CGrannyModelInstance pModelInstance = m_LODControllerVector[dwModelInstanceIndex].GetModelInstance();
			if (pModelInstance == null)
			{
				return false;
			}

//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
//Original Metin2 CPlus Line: *ppMatrix = (D3DXMATRIX *)pModelInstance->GetBoneMatrixPointer(dwBoneIndex);
			ppMatrix[0].CopyFrom((D3DXMATRIX)pModelInstance.GetBoneMatrixPointer(dwBoneIndex));
			if (ppMatrix[0] == null)
			{
				return false;
			}

			return true;
		}

		public bool GetCompositeBoneMatrix(uint dwModelInstanceIndex, uint dwBoneIndex, D3DXMATRIX[] ppMatrix)
		{
			if (!CheckModelInstanceIndex(dwModelInstanceIndex))
			{
				return false;
			}

			CGrannyModelInstance pModelInstance = m_LODControllerVector[dwModelInstanceIndex].GetModelInstance();
			if (pModelInstance == null)
			{
				return false;
			}

//# Laniatus Games Studio Inc. | TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'CopyFrom' method should be created:
//Original Metin2 CPlus Line: *ppMatrix = (D3DXMATRIX *)pModelInstance->GetCompositeBoneMatrixPointer(dwBoneIndex);
			ppMatrix[0].CopyFrom((D3DXMATRIX)pModelInstance.GetCompositeBoneMatrixPointer(dwBoneIndex));

			return true;
		}

		public void UpdateTransform(D3DXMATRIX pMatrix, float fSecondsElapsed = 0.0f, int iModelInstanceIndex = 0)
		{
			int nLODCount = m_LODControllerVector.size();
			if (iModelInstanceIndex >= nLODCount)
			{
				return;
			}

			CGrannyLODController pkLODCtrl = m_LODControllerVector[iModelInstanceIndex];
			if (pkLODCtrl == null)
			{
				return;
			}

			CGrannyModelInstance pModelInstance = pkLODCtrl.GetModelInstance();
			if (pModelInstance == null)
			{
				return;
			}

			pModelInstance.UpdateTransform(pMatrix, fSecondsElapsed);
		}

//# Laniatus Games Studio Inc. | TODO TASK: The implementation of the following method could not be found:
//		void ProjectShadow(in CGraphicShadowTexture c_rShadowTexture);

		public void BuildBoundingSphere()
		{
			D3DXVECTOR3 v3Min = new D3DXVECTOR3();
			D3DXVECTOR3 v3Max = new D3DXVECTOR3();
			GetBoundBox(0, v3Min, v3Max);
			m_v3Center = (v3Min + v3Max) * 0.5f;
			D3DXVECTOR3 vDelta = (v3Max - v3Min);

			m_fRadius = D3DXVec3Length(vDelta) * 0.5f + 50.0f;
		}

		public void BuildBoundingAABB()
		{
			D3DXVECTOR3 v3Min = new D3DXVECTOR3();
			D3DXVECTOR3 v3Max = new D3DXVECTOR3();
			GetBoundBox(0, v3Min, v3Max);
			m_v3Center = (v3Min + v3Max) * 0.5f;
			m_v3Min = v3Min;
			m_v3Max = v3Max;
		}

		public virtual void CalculateBBox()
		{
			GetBoundBox(m_v3BBoxMin, m_v3BBoxMax);

			m_v4TBBox[0] = D3DXVECTOR4(m_v3BBoxMin.x, m_v3BBoxMin.y, m_v3BBoxMin.z, 1.0f);
			m_v4TBBox[1] = D3DXVECTOR4(m_v3BBoxMin.x, m_v3BBoxMax.y, m_v3BBoxMin.z, 1.0f);
			m_v4TBBox[2] = D3DXVECTOR4(m_v3BBoxMax.x, m_v3BBoxMin.y, m_v3BBoxMin.z, 1.0f);
			m_v4TBBox[3] = D3DXVECTOR4(m_v3BBoxMax.x, m_v3BBoxMax.y, m_v3BBoxMin.z, 1.0f);
			m_v4TBBox[4] = D3DXVECTOR4(m_v3BBoxMin.x, m_v3BBoxMin.y, m_v3BBoxMax.z, 1.0f);
			m_v4TBBox[5] = D3DXVECTOR4(m_v3BBoxMin.x, m_v3BBoxMax.y, m_v3BBoxMax.z, 1.0f);
			m_v4TBBox[6] = D3DXVECTOR4(m_v3BBoxMax.x, m_v3BBoxMin.y, m_v3BBoxMax.z, 1.0f);
			m_v4TBBox[7] = D3DXVECTOR4(m_v3BBoxMax.x, m_v3BBoxMax.y, m_v3BBoxMax.z, 1.0f);

			D3DXMATRIX c_rmatTransform = GetTransform();

			for (uint LaniatusDefVariables = 0; LaniatusDefVariables < 8; ++i)
			{
				D3DXVec4Transform(m_v4TBBox[i], m_v4TBBox[i], c_rmatTransform);
				if (0 == i)
				{
					m_v3TBBoxMin.x = m_v4TBBox[i].x;
					m_v3TBBoxMin.y = m_v4TBBox[i].y;
					m_v3TBBoxMin.z = m_v4TBBox[i].z;
					m_v3TBBoxMax.x = m_v4TBBox[i].x;
					m_v3TBBoxMax.y = m_v4TBBox[i].y;
					m_v3TBBoxMax.z = m_v4TBBox[i].z;
				}
				else
				{
					if (m_v3TBBoxMin.x > m_v4TBBox[i].x)
					{
						m_v3TBBoxMin.x = m_v4TBBox[i].x;
					}
					if (m_v3TBBoxMax.x < m_v4TBBox[i].x)
					{
						m_v3TBBoxMax.x = m_v4TBBox[i].x;
					}
					if (m_v3TBBoxMin.y > m_v4TBBox[i].y)
					{
						m_v3TBBoxMin.y = m_v4TBBox[i].y;
					}
					if (m_v3TBBoxMax.y < m_v4TBBox[i].y)
					{
						m_v3TBBoxMax.y = m_v4TBBox[i].y;
					}
					if (m_v3TBBoxMin.z > m_v4TBBox[i].z)
					{
						m_v3TBBoxMin.z = m_v4TBBox[i].z;
					}
					if (m_v3TBBoxMax.z < m_v4TBBox[i].z)
					{
						m_v3TBBoxMax.z = m_v4TBBox[i].z;
					}
				}
			}
		}

		public virtual bool GetBoundingSphere(ref D3DXVECTOR3 v3Center, ref float fRadius)
		{
			if (m_fRadius <= 0)
			{
				BuildBoundingSphere();

				fRadius = m_fRadius;
				v3Center = m_v3Center;
			}
			else
			{
				fRadius = m_fRadius;
				v3Center = m_v3Center;
			}

			D3DXVec3TransformCoord(v3Center, v3Center, GetTransform());
			return true;
		}

		public virtual bool GetBoundingAABB(ref D3DXVECTOR3 v3Min, ref D3DXVECTOR3 v3Max)
		{
			BuildBoundingAABB();

			v3Min = m_v3Min;
			v3Max = m_v3Max;

			D3DXVec3TransformCoord(m_v3Center, m_v3Center, GetTransform());
			return true;
		}

		protected void OnClear()
		{
			Globals.stl_wipe(m_LODControllerVector);
			Globals.stl_wipe_second(m_roMotionThingMap);

			for (uint d = 0; d < m_modelThingSetVector.size(); ++d)
			{
				m_modelThingSetVector[d].Clear();
			}
		}

		protected void OnDeform()
		{
			m_bUpdated = true;

			for (List<CGrannyLODController>.size_type LaniatusDefVariables = 0; LaniatusDefVariables != m_LODControllerVector.size(); i++)
			{
				CGrannyLODController pkLOD = m_LODControllerVector[i];
				if (pkLOD != null && pkLOD.isModelInstance())
				{
					if (i == 5)
					{
						RecalcAccePositionMatrixFromBoneMatrix();
						pkLOD.Deform(m_matAbsoluteTrans);
					}
					else
					{
						pkLOD.Deform(m_worldMatrix);
					}
				}
			}
		}

		protected void OnUpdate()
		{
			UpdateLODLevel();
			UpdateTime();
		}

		protected void OnRender()
		{
			RenderWithOneTexture();
		}

		protected void OnBlendRender()
		{
			BlendRenderWithOneTexture();
		}

		protected void OnRenderToShadowMap()
		{
			if (!m_bUpdated)
			{
				return;
			}

			CGrannyLODController.FRenderToShadowMap RenderToShadowMap = new CGrannyLODController.FRenderToShadowMap();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), RenderToShadowMap);
		}

		protected void OnRenderShadow()
		{
			CGrannyLODController.FRenderShadow RenderShadow = new CGrannyLODController.FRenderShadow();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), RenderShadow);
		}

		protected void OnRenderPCBlocker()
		{
			CGrannyLODController.FRenderWithOneTexture RenderPCBlocker = new CGrannyLODController.FRenderWithOneTexture();
			std::for_each(m_LODControllerVector.begin(), m_LODControllerVector.end(), RenderPCBlocker);
		}

		protected bool m_bUpdated;
		protected float m_fLastLocalTime;
		protected float m_fLocalTime;
		protected float m_fDelay;
		protected float m_fSecondElapsed;
		protected float m_fAverageSecondElapsed;
		protected float m_fRadius;
		protected D3DXVECTOR3 m_v3Center = new D3DXVECTOR3();
		protected D3DXVECTOR3 m_v3Min = new D3DXVECTOR3();
		protected D3DXVECTOR3 m_v3Max = new D3DXVECTOR3();

		protected List<CGrannyLODController > m_LODControllerVector = new List<CGrannyLODController >();
		protected List<SModelThingSet> m_modelThingSetVector = new List<SModelThingSet>();
		protected SortedDictionary<uint, CGraphicThing.TRef > m_roMotionThingMap = new SortedDictionary<uint, CGraphicThing.TRef >();

		protected virtual void OnUpdateCollisionData(List<CStaticCollisionData> pscdVector)
		{
			Debug.Assert(pscdVector);
			List<CStaticCollisionData>.Enumerator it;
//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
			for (it = pscdVector.GetEnumerator();it != pscdVector.end();++it)
			{
//# Laniatus Games Studio Inc. | TODO TASK: Iterators are only converted within the context of 'while' and 'for' loops:
				AddCollision((it), GetTransform());
			}
		}

		protected virtual void OnUpdateHeighInstance(CAttributeInstance pAttributeInstance)
		{
			Debug.Assert(pAttributeInstance);
			SetHeightInstance(pAttributeInstance);
		}

		protected virtual bool OnGetObjectHeight(float fX, float fY, ref float pfHeight)
		{
			if (m_pHeightAttributeInstance && m_pHeightAttributeInstance.GetHeight(fX, fY, pfHeight))
			{
				return true;
			}
			return false;
		}

		public static void CreateSystem(uint uCapacity)
		{
			ms_kPool.Create(uCapacity);
		}

		public static void DestroySystem()
		{
			ms_kPool.Destroy();
		}

		public static CGraphicThingInstance New()
		{
			return ms_kPool.Alloc();
		}

		public static void Delete(CGraphicThingInstance pkThingInst)
		{
			pkThingInst.Clear();
			ms_kPool.Free(pkThingInst);
		}

		public static CDynamicPool<CGraphicThingInstance> ms_kPool = new CDynamicPool<CGraphicThingInstance>();

		public bool HaveBlendThing()
		{
			for (int LaniatusDefVariables = 0; LaniatusDefVariables < m_LODControllerVector.size(); i++)
			{
				if (m_LODControllerVector[i].HaveBlendThing())
				{
					return true;
				}
			}
			return false;
		}

		public void RecalcAccePositionMatrixFromBoneMatrix()
		{
			if (m_LODControllerVector.empty())
			{
				return;
			}

			CGrannyModelInstance pModelInstance = m_LODControllerVector[0].GetModelInstance();
			if (pModelInstance == null)
			{
				return;
			}

			int iBoneIndex = 0;
			pModelInstance.GetBoneIndexByName("Bip01 Spine2", iBoneIndex);
			D3DXMATRIX cmatBoneMatrix = (D3DXMATRIX)pModelInstance.GetBoneMatrixPointer(iBoneIndex);
			if (cmatBoneMatrix != null)
			{
				D3DXVECTOR3 v3ScaleCenter = new D3DXVECTOR3(0.0f, 0.0f, 0.0f);
				float fAccePosX = cmatBoneMatrix._41;
				float fAccePosY = cmatBoneMatrix._42;
				float fAccePosZ = cmatBoneMatrix._43;
				D3DXMatrixIdentity(m_matScale);
				if (m_bAttachedAcceRace)
				{
					v3ScaleCenter.x = fAccePosX;
					v3ScaleCenter.y = fAccePosY;
				}
				else
				{
					v3ScaleCenter.x = fAccePosX - 18.0f;
					v3ScaleCenter.y = -40.0f;
				}
				v3ScaleCenter.z = fAccePosZ;
				D3DXQUATERNION qRot = new D3DXQUATERNION(0.0f, 0.0f, 0.0f, 0.0f);
				D3DXMatrixTransformation(m_matScale, v3ScaleCenter, qRot, m_v3ScaleAcce, null, null, null);
			}

			D3DXMATRIX matTemp = new D3DXMATRIX();
			D3DXMatrixMultiply(matTemp, m_matScaleWorld, m_matScale);
			m_matAbsoluteTrans = matTemp * m_mRotation;
			m_matAbsoluteTrans._41 += m_v3Position.x;
			m_matAbsoluteTrans._42 += m_v3Position.y;
			m_matAbsoluteTrans._43 += m_v3Position.z;
		}
}