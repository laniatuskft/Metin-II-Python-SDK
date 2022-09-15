public class CSpeedTreeForestDirectX8
{
//# Laniatus Games Studio Inc. | WARN: The original C++ declaration of the following method implementation was not found:
	public void UpdateCompundMatrix(in _D3DVECTOR c_rEyeVec, in _D3DMATRIX c_rmatView, in _D3DMATRIX c_rmatProj)
	{
		_D3DMATRIX matBlend = new _D3DMATRIX();
		D3DXMatrixIdentity(matBlend);
    
		_D3DMATRIX matBlendShader = new _D3DMATRIX();
		D3DXMatrixMultiply(matBlendShader, c_rmatView, c_rmatProj);
    
		float[] afDirection = new float[3];
		afDirection[0] = matBlendShader.m[0][2];
		afDirection[1] = matBlendShader.m[1][2];
		afDirection[2] = matBlendShader.m[2][2];
		CSpeedTreeRT.SetCamera(new _D3DVECTOR(c_rEyeVec), afDirection);
    
		D3DXMatrixTranspose(matBlendShader, matBlendShader);
		(CStateManager.Instance()).SetVertexShaderConstant(c_nVertexShader_CompoundMatrix, matBlendShader, 4);
	}
}