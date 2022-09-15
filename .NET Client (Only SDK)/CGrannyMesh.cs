public class CGrannyMesh
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void DeformPNTVertices(object dstBaseVertices, _D3DMATRIX boneMatrices, granny_mesh_binding pgrnMeshBinding)
	{
		Debug.Assert(dstBaseVertices != null);
		Debug.Assert(boneMatrices != null);
		Debug.Assert(m_pgrnMeshDeformer != null);
    
		granny_mesh pgrnMesh = GetGrannyMeshPointer();
    
		SPNTVertex srcVertices = (SPNTVertex) GrannyGetMeshVertices(pgrnMesh);
		SPNTVertex dstVertices = ((SPNTVertex) dstBaseVertices) + m_vtxBasePos;
    
		int vtxCount = GrannyGetMeshVertexCount(pgrnMesh);
    
	//# Laniatus Games Studio Inc. | TODO TASK: C# does not have an equivalent to pointers to value types:
	//Original Metin2 CPlus Line: int * boneIndices = (int*)GrannyGetMeshBindingToBoneIndices(pgrnMeshBinding);
		int boneIndices = (int)GrannyGetMeshBindingToBoneIndices(pgrnMeshBinding);
    
		GrannyDeformVertices(m_pgrnMeshDeformer, boneIndices, (float)boneMatrices, vtxCount, srcVertices, dstVertices);
	}
}